"""
Análisis del experimento comparativo: RF humanos vs. RF generados por LLM
Proyecto SICST - ISR-401 - Enfoque 1

OSF: https://doi.org/10.17605/OSF.IO/82Q76

Análisis confirmatorio:
- 11 pares temáticos estrictos (tipo == "pareado")
- Shapiro-Wilk sobre diferencias por par
- t apareada o Wilcoxon de rangos con signo
- Holm-Bonferroni sobre 5 dimensiones
- diferencia media + IC bootstrap 95 %
- Cohen's dz + IC bootstrap 95 %
- 10 000 remuestreos, semilla 42

La clave de desciego se proporciona mediante --clave y no se publica.
"""

import argparse
from pathlib import Path
import warnings

import numpy as np
import pandas as pd
from scipy import stats
from statsmodels.stats.multitest import multipletests

warnings.filterwarnings("ignore")

DIMENSIONES = [
    "completitud",
    "ausencia_ambiguedad",
    "verificabilidad",
    "correccion_fuente",
    "consistencia_interna",
]

EVALUADORES = {
    "Mishell": "Evaluacion_Mishell.xlsx",
    "Angel": "Evaluacion_Angel.xlsx",
    "Dayana": "Evaluacion_Dayana.xlsx",
    "sebas": "Evaluacion_sebas.xlsx",
}

RUTA_SCRIPT = Path(__file__).resolve().parent
RUTA_EXPERIMENTO = RUTA_SCRIPT.parent
RUTA_EVALUACIONES = RUTA_EXPERIMENTO / "datos_crudos" / "evaluaciones_ciegas"
RUTA_MATRIZ = RUTA_EXPERIMENTO / "datos_procesados" / "matriz_trazabilidad_tema_RF.csv"
RUTA_RESULTADOS = RUTA_EXPERIMENTO / "resultados"

N_BOOT = 10_000
SEED_BOOT = 42


def validar_archivos(ruta_clave: Path) -> None:
    faltantes = []

    for archivo in EVALUADORES.values():
        ruta = RUTA_EVALUACIONES / archivo
        if not ruta.is_file():
            faltantes.append(str(ruta))

    if not RUTA_MATRIZ.is_file():
        faltantes.append(str(RUTA_MATRIZ))

    if not ruta_clave.is_file():
        faltantes.append(str(ruta_clave))

    if faltantes:
        detalle = "\n".join(f" - {x}" for x in faltantes)
        raise FileNotFoundError(f"Faltan archivos requeridos:\n{detalle}")


def cargar_evaluaciones() -> pd.DataFrame:
    filas = []

    for nombre, archivo in EVALUADORES.items():
        ruta = RUTA_EVALUACIONES / archivo
        df = pd.read_excel(ruta, sheet_name="Evaluación")

        columnas_necesarias = {"item_id", *DIMENSIONES}
        faltan = columnas_necesarias - set(df.columns)
        if faltan:
            raise ValueError(
                f"{archivo}: faltan columnas requeridas: {sorted(faltan)}"
            )

        df = df[df["item_id"] != "EJEMPLO"].copy()

        for _, row in df.iterrows():
            for dim in DIMENSIONES:
                filas.append(
                    {
                        "item_id": row["item_id"],
                        "evaluador": nombre,
                        "dimension": dim,
                        "puntaje": row[dim],
                    }
                )

    largo = pd.DataFrame(filas)

    if largo["puntaje"].isna().any():
        raise ValueError("Existen puntuaciones faltantes en las hojas de evaluación.")

    fuera_rango = ~largo["puntaje"].between(1, 5)
    if fuera_rango.any():
        raise ValueError("Existen puntuaciones fuera de la escala Likert 1-5.")

    return largo


def cargar_clave(ruta_clave: Path) -> pd.DataFrame:
    clave = pd.read_csv(ruta_clave)

    requeridas = {"item_id", "origen_real", "id_real"}
    faltan = requeridas - set(clave.columns)
    if faltan:
        raise ValueError(
            f"La clave de desciego no contiene: {sorted(faltan)}"
        )

    if clave["item_id"].duplicated().any():
        raise ValueError("La clave contiene item_id duplicados.")

    return clave


def cargar_matriz_trazabilidad() -> pd.DataFrame:
    matriz = pd.read_csv(RUTA_MATRIZ)

    requeridas = {"tema_id", "rf_humano_id", "rf_llm_id", "tipo"}
    faltan = requeridas - set(matriz.columns)
    if faltan:
        raise ValueError(
            f"La matriz de trazabilidad no contiene: {sorted(faltan)}"
        )

    return matriz


def fleiss_kappa(tabla_conteos: np.ndarray) -> float:
    n_items, _ = tabla_conteos.shape
    n_evaluadores = tabla_conteos.sum(axis=1)[0]

    p_j = tabla_conteos.sum(axis=0) / (n_items * n_evaluadores)
    p_e = (p_j ** 2).sum()

    p_i = (
        (tabla_conteos * (tabla_conteos - 1)).sum(axis=1)
        / (n_evaluadores * (n_evaluadores - 1))
    )

    p_bar = p_i.mean()
    return (p_bar - p_e) / (1 - p_e) if (1 - p_e) != 0 else np.nan


def calcular_fleiss_por_dimension(df_largo: pd.DataFrame) -> pd.DataFrame:
    resultados = []

    for dim in DIMENSIONES:
        sub = df_largo[df_largo["dimension"] == dim]

        tabla = sub.pivot_table(
            index="item_id",
            columns="puntaje",
            aggfunc="size",
            fill_value=0,
        )

        for cat in range(1, 6):
            if cat not in tabla.columns:
                tabla[cat] = 0

        tabla = tabla[[1, 2, 3, 4, 5]].values
        kappa = fleiss_kappa(tabla)

        resultados.append(
            {"dimension": dim, "fleiss_kappa": round(kappa, 4)}
        )

    return pd.DataFrame(resultados)


def construir_tabla_por_item(
    df_largo: pd.DataFrame, clave: pd.DataFrame
) -> pd.DataFrame:
    prom = (
        df_largo.groupby(["item_id", "dimension"])["puntaje"]
        .mean()
        .reset_index()
        .pivot(index="item_id", columns="dimension", values="puntaje")
        .reset_index()
    )

    prom = prom.merge(clave, on="item_id", how="left", validate="one_to_one")

    if prom[["origen_real", "id_real"]].isna().any().any():
        faltantes = prom.loc[
            prom["origen_real"].isna() | prom["id_real"].isna(), "item_id"
        ].tolist()
        raise ValueError(
            "La clave de desciego no cubre estos item_id: "
            + ", ".join(map(str, faltantes))
        )

    prom["puntaje_global"] = prom[DIMENSIONES].mean(axis=1)

    return prom


def construir_pares(
    tabla_item: pd.DataFrame, matriz: pd.DataFrame
) -> pd.DataFrame:
    pares_estrictos = matriz[matriz["tipo"] == "pareado"].copy()

    if len(pares_estrictos) != 11:
        raise ValueError(
            f"Se esperaban 11 pares estrictos y se encontraron {len(pares_estrictos)}."
        )

    tabla_item_idx = tabla_item.set_index(["origen_real", "id_real"])

    filas = []

    for _, fila in pares_estrictos.iterrows():
        clave_h = ("human", fila["rf_humano_id"])
        clave_l = ("llm", fila["rf_llm_id"])

        if clave_h not in tabla_item_idx.index:
            raise KeyError(f"No se encontró el RF humano {fila['rf_humano_id']} en la clave.")
        if clave_l not in tabla_item_idx.index:
            raise KeyError(f"No se encontró el RF LLM {fila['rf_llm_id']} en la clave.")

        score_h = tabla_item_idx.loc[clave_h]
        score_l = tabla_item_idx.loc[clave_l]

        registro = {
            "tema_id": fila["tema_id"],
            "rf_humano_id": fila["rf_humano_id"],
            "rf_llm_id": fila["rf_llm_id"],
        }

        for dim in DIMENSIONES + ["puntaje_global"]:
            registro[f"{dim}_humano"] = score_h[dim]
            registro[f"{dim}_llm"] = score_l[dim]

        filas.append(registro)

    return pd.DataFrame(filas)


def descriptivos_por_grupo(tabla_item: pd.DataFrame) -> pd.DataFrame:
    filas = []

    for dim in DIMENSIONES + ["puntaje_global"]:
        for origen in ["human", "llm"]:
            datos = tabla_item.loc[tabla_item["origen_real"] == origen, dim]

            filas.append(
                {
                    "dimension": dim,
                    "grupo": origen,
                    "n": len(datos),
                    "media": round(datos.mean(), 3),
                    "mediana": round(datos.median(), 3),
                    "de": round(datos.std(), 3),
                    "min": datos.min(),
                    "max": datos.max(),
                    "iqr": round(
                        datos.quantile(0.75) - datos.quantile(0.25), 3
                    ),
                }
            )

    return pd.DataFrame(filas)


def cohen_dz(diffs: np.ndarray) -> float:
    de = np.std(diffs, ddof=1)

    if np.isclose(de, 0):
        return np.nan

    return float(np.mean(diffs) / de)


def bootstrap_metricas(
    diffs: np.ndarray,
    n_boot: int = N_BOOT,
    seed: int = SEED_BOOT,
):
    rng = np.random.default_rng(seed)

    medias = np.empty(n_boot, dtype=float)
    dz_vals = []

    n = len(diffs)

    for i in range(n_boot):
        muestra = rng.choice(diffs, size=n, replace=True)
        medias[i] = np.mean(muestra)

        dz = cohen_dz(muestra)
        if not np.isnan(dz) and np.isfinite(dz):
            dz_vals.append(dz)

    media_lo, media_hi = np.percentile(medias, [2.5, 97.5])

    if dz_vals:
        dz_lo, dz_hi = np.percentile(np.asarray(dz_vals), [2.5, 97.5])
    else:
        dz_lo, dz_hi = np.nan, np.nan

    return float(media_lo), float(media_hi), float(dz_lo), float(dz_hi)


def analisis_apareado(pares: pd.DataFrame) -> pd.DataFrame:
    n = len(pares)
    resultados = []
    p_valores_crudos = []

    for indice_dim, dim in enumerate(DIMENSIONES + ["puntaje_global"]):
        h = pares[f"{dim}_humano"].to_numpy(dtype=float)
        l = pares[f"{dim}_llm"].to_numpy(dtype=float)
        diffs = h - l

        if np.allclose(diffs, 0):
            stat = np.nan
            p = 1.0
            prueba = "sin variacion"
            normal = None
            p_norm = np.nan
            media_diff = 0.0
            dz = 0.0
            ci_lo = ci_hi = 0.0
            dz_lo = dz_hi = 0.0
        else:
            _, p_norm = stats.shapiro(diffs)
            normal = bool(p_norm > 0.05)

            if normal:
                stat, p = stats.ttest_rel(h, l)
                prueba = "t apareada"
            else:
                stat, p = stats.wilcoxon(h, l)
                prueba = "Wilcoxon rangos con signo"

            media_diff = float(np.mean(diffs))
            dz = cohen_dz(diffs)

            # Semilla distinta pero determinista por fila para evitar secuencias
            # bootstrap idénticas entre dimensiones.
            ci_lo, ci_hi, dz_lo, dz_hi = bootstrap_metricas(
                diffs, seed=SEED_BOOT + indice_dim
            )

        resultados.append(
            {
                "dimension": dim,
                "n_pares": n,
                "prueba": prueba,
                "shapiro_p_diferencias": (
                    round(float(p_norm), 4) if not np.isnan(p_norm) else np.nan
                ),
                "normal_shapiro_diffs": normal,
                "estadistico": (
                    round(float(stat), 4) if not np.isnan(stat) else np.nan
                ),
                "valor_p_crudo": round(float(p), 4),
                "media_diferencia_humano_menos_llm": round(media_diff, 4),
                "ic95_diferencia_lo": round(ci_lo, 4),
                "ic95_diferencia_hi": round(ci_hi, 4),
                "cohen_dz": round(float(dz), 4) if not np.isnan(dz) else np.nan,
                "ic95_cohen_dz_lo": (
                    round(float(dz_lo), 4) if not np.isnan(dz_lo) else np.nan
                ),
                "ic95_cohen_dz_hi": (
                    round(float(dz_hi), 4) if not np.isnan(dz_hi) else np.nan
                ),
                "bootstrap_remuestreos": N_BOOT,
                "bootstrap_semilla_base": SEED_BOOT,
            }
        )

        p_valores_crudos.append(float(p))

    p_dims = p_valores_crudos[: len(DIMENSIONES)]

    rechazado, p_ajustado, _, _ = multipletests(
        p_dims,
        alpha=0.05,
        method="holm",
    )

    df_resultados = pd.DataFrame(resultados)

    df_resultados["valor_p_holm"] = list(p_ajustado) + [np.nan]
    df_resultados["significativo_holm_0.05"] = list(rechazado) + [None]

    return df_resultados


def generar_figura(pares: pd.DataFrame, ruta_salida: Path) -> None:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(7, 5))

    h = pares["puntaje_global_humano"].to_numpy(dtype=float)
    l = pares["puntaje_global_llm"].to_numpy(dtype=float)

    for i in range(len(pares)):
        ax.plot([0, 1], [h[i], l[i]], alpha=0.4, linewidth=1)

    ax.scatter([0] * len(h), h, zorder=3, label="Humano")
    ax.scatter([1] * len(l), l, zorder=3, label="LLM")

    ax.set_xticks([0, 1])
    ax.set_xticklabels(["Humano", "LLM"])
    ax.set_ylabel("Puntaje global (promedio de 5 dimensiones, escala 1-5)")
    ax.set_title(f"Comparación pareada por tema (n={len(pares)} pares) — SICST")
    ax.legend()

    plt.tight_layout()
    plt.savefig(ruta_salida, dpi=150)
    plt.close()


def parse_args():
    parser = argparse.ArgumentParser(
        description=(
            "Análisis apareado del experimento RF humano vs. LLM "
            "(SICST, Enfoque 1)."
        )
    )

    parser.add_argument(
        "--clave",
        required=True,
        type=Path,
        help=(
            "Ruta local a clave_privada_desciego.csv ya extraída/descifrada. "
            "No debe versionarse en el repositorio público."
        ),
    )

    return parser.parse_args()


def main():
    args = parse_args()
    ruta_clave = args.clave.expanduser().resolve()

    validar_archivos(ruta_clave)

    df_largo = cargar_evaluaciones()
    clave = cargar_clave(ruta_clave)
    matriz = cargar_matriz_trazabilidad()

    fleiss = calcular_fleiss_por_dimension(df_largo)
    tabla_item = construir_tabla_por_item(df_largo, clave)
    descriptivos = descriptivos_por_grupo(tabla_item)
    pares = construir_pares(tabla_item, matriz)
    resultado_apareado = analisis_apareado(pares)

    RUTA_RESULTADOS.mkdir(parents=True, exist_ok=True)

    fleiss.to_csv(RUTA_RESULTADOS / "fleiss_kappa.csv", index=False)
    descriptivos.to_csv(
        RUTA_RESULTADOS / "descriptivos_por_grupo.csv", index=False
    )
    resultado_apareado.to_csv(
        RUTA_RESULTADOS / "prueba_hipotesis_apareada.csv", index=False
    )
    pares.to_csv(
        RUTA_RESULTADOS / "pares_estrictos_utilizados.csv", index=False
    )
    generar_figura(
        pares,
        RUTA_RESULTADOS / "figura_comparacion_pareada.png",
    )

    print("=== SICST: análisis reproducible completado ===")
    print(f"Evaluadores: {len(EVALUADORES)}")
    print(f"Ítems evaluados: {tabla_item['item_id'].nunique()}")
    print(f"Pares estrictos: {len(pares)}")
    print(f"Resultados: {RUTA_RESULTADOS}")
    print()
    print("=== Fleiss kappa ===")
    print(fleiss.to_string(index=False))
    print()
    print("=== Análisis apareado ===")
    print(resultado_apareado.to_string(index=False))


if __name__ == "__main__":
    main()
