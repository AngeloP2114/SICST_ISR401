"""
Análisis reproducible del experimento comparativo SICST:
RF humanos vs. RF generados por LLM.

El origen de los ITEM se reconstruye después de la evaluación a partir de:
- datos_crudos/hoja_evaluacion_ciega.csv
- datos_procesados/matriz_trazabilidad_tema_RF.csv

No requiere una clave externa.
"""

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
RUTA_CRUDOS = RUTA_EXPERIMENTO / "datos_crudos"
RUTA_EVALUACIONES = RUTA_CRUDOS / "evaluaciones_ciegas"
RUTA_HOJA_CIEGA = RUTA_CRUDOS / "hoja_evaluacion_ciega.csv"
RUTA_MATRIZ = (
    RUTA_EXPERIMENTO / "datos_procesados" / "matriz_trazabilidad_tema_RF.csv"
)
RUTA_RESULTADOS = RUTA_EXPERIMENTO / "resultados"

N_BOOT = 10_000
SEED_BOOT = 42


def normalizar_texto(valor) -> str:
    if pd.isna(valor):
        return ""
    return " ".join(str(valor).strip().split())


def validar_archivos() -> None:
    faltantes = []

    for archivo in EVALUADORES.values():
        ruta = RUTA_EVALUACIONES / archivo
        if not ruta.is_file():
            faltantes.append(str(ruta))

    for ruta in (RUTA_HOJA_CIEGA, RUTA_MATRIZ):
        if not ruta.is_file():
            faltantes.append(str(ruta))

    if faltantes:
        detalle = "\n".join(f" - {ruta}" for ruta in faltantes)
        raise FileNotFoundError(f"Faltan archivos requeridos:\n{detalle}")


def cargar_evaluaciones() -> pd.DataFrame:
    filas = []

    for nombre, archivo in EVALUADORES.items():
        df = pd.read_excel(
            RUTA_EVALUACIONES / archivo,
            sheet_name="Evaluación",
        )

        requeridas = {"item_id", *DIMENSIONES}
        faltan = requeridas - set(df.columns)

        if faltan:
            raise ValueError(
                f"{archivo}: faltan columnas requeridas: {sorted(faltan)}"
            )

        df = df[df["item_id"] != "EJEMPLO"].copy()

        for _, row in df.iterrows():
            for dimension in DIMENSIONES:
                filas.append(
                    {
                        "item_id": row["item_id"],
                        "evaluador": nombre,
                        "dimension": dimension,
                        "puntaje": row[dimension],
                    }
                )

    largo = pd.DataFrame(filas)

    if largo["puntaje"].isna().any():
        raise ValueError("Existen puntuaciones faltantes.")

    if (~largo["puntaje"].between(1, 5)).any():
        raise ValueError("Existen puntuaciones fuera de la escala Likert 1-5.")

    return largo


def cargar_matriz() -> pd.DataFrame:
    matriz = pd.read_csv(RUTA_MATRIZ)

    requeridas = {
        "tema_id",
        "rf_humano_id",
        "rf_humano_texto",
        "rf_llm_id",
        "rf_llm_texto",
        "tipo",
    }
    faltan = requeridas - set(matriz.columns)

    if faltan:
        raise ValueError(
            f"La matriz no contiene estas columnas: {sorted(faltan)}"
        )

    return matriz


def reconstruir_mapa_origen(matriz: pd.DataFrame) -> pd.DataFrame:
    """
    Reconstruye ITEM -> origen_real -> id_real mediante coincidencia del texto
    de la hoja ciega con los textos canónicos de la matriz temática.
    """
    hoja = pd.read_csv(RUTA_HOJA_CIEGA)

    if not {"item_id", "descripcion"}.issubset(hoja.columns):
        raise ValueError(
            "hoja_evaluacion_ciega.csv debe contener item_id y descripcion."
        )

    candidatos = {}

    def agregar(texto, origen, id_real):
        texto_norm = normalizar_texto(texto)
        id_norm = normalizar_texto(id_real)

        if not texto_norm or not id_norm:
            return

        candidatos.setdefault(texto_norm, set()).add((origen, id_norm))

    for _, row in matriz.iterrows():
        agregar(row["rf_humano_texto"], "human", row["rf_humano_id"])
        agregar(row["rf_llm_texto"], "llm", row["rf_llm_id"])

    filas = []
    sin_coincidencia = []
    ambiguos = []

    for _, row in hoja.iterrows():
        texto = normalizar_texto(row["descripcion"])
        coincidencias = sorted(candidatos.get(texto, set()))

        if len(coincidencias) == 0:
            sin_coincidencia.append(row["item_id"])
            continue

        if len(coincidencias) > 1:
            ambiguos.append((row["item_id"], coincidencias))
            continue

        origen, id_real = coincidencias[0]

        filas.append(
            {
                "item_id": row["item_id"],
                "origen_real": origen,
                "id_real": id_real,
            }
        )

    if sin_coincidencia:
        raise ValueError(
            "ITEM sin coincidencia en la matriz: "
            + ", ".join(map(str, sin_coincidencia))
        )

    if ambiguos:
        raise ValueError(
            "ITEM con coincidencia ambigua: " + repr(ambiguos)
        )

    mapa = pd.DataFrame(filas)

    if len(mapa) != 66:
        raise ValueError(
            f"Se esperaban 66 ITEM y se reconstruyeron {len(mapa)}."
        )

    if mapa["item_id"].duplicated().any():
        raise ValueError("La reconstrucción contiene item_id duplicados.")

    conteos = mapa["origen_real"].value_counts().to_dict()

    if conteos.get("human", 0) != 33 or conteos.get("llm", 0) != 33:
        raise ValueError(
            "La reconstrucción debe producir 33 human y 33 llm; "
            f"se obtuvo: {conteos}"
        )

    return mapa


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

    for dimension in DIMENSIONES:
        sub = df_largo[df_largo["dimension"] == dimension]

        tabla = sub.pivot_table(
            index="item_id",
            columns="puntaje",
            aggfunc="size",
            fill_value=0,
        )

        for categoria in range(1, 6):
            if categoria not in tabla.columns:
                tabla[categoria] = 0

        kappa = fleiss_kappa(tabla[[1, 2, 3, 4, 5]].values)

        resultados.append(
            {
                "dimension": dimension,
                "fleiss_kappa": round(kappa, 4),
            }
        )

    return pd.DataFrame(resultados)


def construir_tabla_por_item(
    df_largo: pd.DataFrame,
    mapa: pd.DataFrame,
) -> pd.DataFrame:
    promedios = (
        df_largo.groupby(["item_id", "dimension"])["puntaje"]
        .mean()
        .reset_index()
        .pivot(index="item_id", columns="dimension", values="puntaje")
        .reset_index()
    )

    promedios = promedios.merge(
        mapa,
        on="item_id",
        how="left",
        validate="one_to_one",
    )

    if promedios[["origen_real", "id_real"]].isna().any().any():
        raise ValueError(
            "El mapa reconstruido no cubre todos los ITEM evaluados."
        )

    promedios["puntaje_global"] = promedios[DIMENSIONES].mean(axis=1)

    return promedios


def construir_pares(
    tabla_item: pd.DataFrame,
    matriz: pd.DataFrame,
) -> pd.DataFrame:
    pares_estrictos = matriz[matriz["tipo"] == "pareado"].copy()

    if len(pares_estrictos) != 11:
        raise ValueError(
            f"Se esperaban 11 pares estrictos y se encontraron "
            f"{len(pares_estrictos)}."
        )

    indice = tabla_item.set_index(["origen_real", "id_real"])
    filas = []

    for _, row in pares_estrictos.iterrows():
        clave_h = ("human", row["rf_humano_id"])
        clave_l = ("llm", row["rf_llm_id"])

        if clave_h not in indice.index:
            raise KeyError(
                f"No se encontró el RF humano {row['rf_humano_id']}."
            )

        if clave_l not in indice.index:
            raise KeyError(
                f"No se encontró el RF LLM {row['rf_llm_id']}."
            )

        humano = indice.loc[clave_h]
        llm = indice.loc[clave_l]

        registro = {
            "tema_id": row["tema_id"],
            "rf_humano_id": row["rf_humano_id"],
            "rf_llm_id": row["rf_llm_id"],
        }

        for dimension in DIMENSIONES + ["puntaje_global"]:
            registro[f"{dimension}_humano"] = humano[dimension]
            registro[f"{dimension}_llm"] = llm[dimension]

        filas.append(registro)

    return pd.DataFrame(filas)


def descriptivos_por_grupo(tabla_item: pd.DataFrame) -> pd.DataFrame:
    filas = []

    for dimension in DIMENSIONES + ["puntaje_global"]:
        for origen in ("human", "llm"):
            datos = tabla_item.loc[
                tabla_item["origen_real"] == origen,
                dimension,
            ]

            filas.append(
                {
                    "dimension": dimension,
                    "grupo": origen,
                    "n": len(datos),
                    "media": round(datos.mean(), 3),
                    "mediana": round(datos.median(), 3),
                    "de": round(datos.std(), 3),
                    "min": datos.min(),
                    "max": datos.max(),
                    "iqr": round(
                        datos.quantile(0.75) - datos.quantile(0.25),
                        3,
                    ),
                }
            )

    return pd.DataFrame(filas)


def cohen_dz(diferencias: np.ndarray) -> float:
    desviacion = np.std(diferencias, ddof=1)

    if np.isclose(desviacion, 0):
        return np.nan

    return float(np.mean(diferencias) / desviacion)


def bootstrap_metricas(
    diferencias: np.ndarray,
    n_boot: int = N_BOOT,
    seed: int = SEED_BOOT,
):
    rng = np.random.default_rng(seed)

    medias = np.empty(n_boot, dtype=float)
    dz_validos = []

    for indice in range(n_boot):
        muestra = rng.choice(
            diferencias,
            size=len(diferencias),
            replace=True,
        )

        medias[indice] = np.mean(muestra)

        dz = cohen_dz(muestra)

        if np.isfinite(dz):
            dz_validos.append(dz)

    media_lo, media_hi = np.percentile(medias, [2.5, 97.5])

    if dz_validos:
        dz_lo, dz_hi = np.percentile(
            np.asarray(dz_validos),
            [2.5, 97.5],
        )
    else:
        dz_lo = np.nan
        dz_hi = np.nan

    return media_lo, media_hi, dz_lo, dz_hi


def analisis_apareado(pares: pd.DataFrame) -> pd.DataFrame:
    resultados = []
    p_crudos = []

    for posicion, dimension in enumerate(
        DIMENSIONES + ["puntaje_global"]
    ):
        humano = pares[f"{dimension}_humano"].to_numpy(dtype=float)
        llm = pares[f"{dimension}_llm"].to_numpy(dtype=float)
        diferencias = humano - llm

        if np.allclose(diferencias, 0):
            p_normalidad = np.nan
            normal = None
            estadistico = np.nan
            p_valor = 1.0
            prueba = "sin variacion"
            media = 0.0
            dz = 0.0
            media_lo = 0.0
            media_hi = 0.0
            dz_lo = 0.0
            dz_hi = 0.0
        else:
            _, p_normalidad = stats.shapiro(diferencias)
            normal = bool(p_normalidad > 0.05)

            if normal:
                estadistico, p_valor = stats.ttest_rel(humano, llm)
                prueba = "t apareada"
            else:
                estadistico, p_valor = stats.wilcoxon(humano, llm)
                prueba = "Wilcoxon rangos con signo"

            media = float(np.mean(diferencias))
            dz = cohen_dz(diferencias)

            media_lo, media_hi, dz_lo, dz_hi = bootstrap_metricas(
                diferencias,
                seed=SEED_BOOT + posicion,
            )

        resultados.append(
            {
                "dimension": dimension,
                "n_pares": len(pares),
                "prueba": prueba,
                "shapiro_p_diferencias": (
                    round(float(p_normalidad), 4)
                    if np.isfinite(p_normalidad)
                    else np.nan
                ),
                "normal_shapiro_diffs": normal,
                "estadistico": (
                    round(float(estadistico), 4)
                    if np.isfinite(estadistico)
                    else np.nan
                ),
                "valor_p_crudo": round(float(p_valor), 4),
                "media_diferencia_humano_menos_llm": round(media, 4),
                "ic95_diferencia_lo": round(float(media_lo), 4),
                "ic95_diferencia_hi": round(float(media_hi), 4),
                "cohen_dz": (
                    round(float(dz), 4)
                    if np.isfinite(dz)
                    else np.nan
                ),
                "ic95_cohen_dz_lo": (
                    round(float(dz_lo), 4)
                    if np.isfinite(dz_lo)
                    else np.nan
                ),
                "ic95_cohen_dz_hi": (
                    round(float(dz_hi), 4)
                    if np.isfinite(dz_hi)
                    else np.nan
                ),
                "bootstrap_remuestreos": N_BOOT,
                "bootstrap_semilla_base": SEED_BOOT,
            }
        )

        p_crudos.append(float(p_valor))

    rechazado, p_holm, _, _ = multipletests(
        p_crudos[:5],
        alpha=0.05,
        method="holm",
    )

    salida = pd.DataFrame(resultados)

    salida["valor_p_holm"] = list(p_holm) + [np.nan]
    salida["significativo_holm_0.05"] = list(rechazado) + [None]

    return salida


def generar_figura(
    pares: pd.DataFrame,
    ruta_salida: Path,
) -> None:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    humano = pares["puntaje_global_humano"].to_numpy(dtype=float)
    llm = pares["puntaje_global_llm"].to_numpy(dtype=float)

    fig, ax = plt.subplots(figsize=(7, 5))

    for indice in range(len(pares)):
        ax.plot(
            [0, 1],
            [humano[indice], llm[indice]],
            alpha=0.4,
            linewidth=1,
        )

    ax.scatter(
        [0] * len(humano),
        humano,
        zorder=3,
        label="Humano",
    )
    ax.scatter(
        [1] * len(llm),
        llm,
        zorder=3,
        label="LLM",
    )

    ax.set_xticks([0, 1])
    ax.set_xticklabels(["Humano", "LLM"])
    ax.set_ylabel(
        "Puntaje global (promedio de 5 dimensiones, escala 1-5)"
    )
    ax.set_title(
        f"Comparación pareada por tema "
        f"(n={len(pares)} pares) — SICST"
    )
    ax.legend()

    plt.tight_layout()
    plt.savefig(ruta_salida, dpi=150)
    plt.close()


def main() -> None:
    validar_archivos()

    matriz = cargar_matriz()
    mapa = reconstruir_mapa_origen(matriz)
    evaluaciones = cargar_evaluaciones()

    tabla_item = construir_tabla_por_item(evaluaciones, mapa)
    fleiss = calcular_fleiss_por_dimension(evaluaciones)
    descriptivos = descriptivos_por_grupo(tabla_item)
    pares = construir_pares(tabla_item, matriz)
    resultado = analisis_apareado(pares)

    RUTA_RESULTADOS.mkdir(parents=True, exist_ok=True)

    mapa.to_csv(
        RUTA_RESULTADOS / "mapa_origen_items_reconstruido.csv",
        index=False,
    )
    fleiss.to_csv(
        RUTA_RESULTADOS / "fleiss_kappa.csv",
        index=False,
    )
    descriptivos.to_csv(
        RUTA_RESULTADOS / "descriptivos_por_grupo.csv",
        index=False,
    )
    pares.to_csv(
        RUTA_RESULTADOS / "pares_estrictos_utilizados.csv",
        index=False,
    )
    resultado.to_csv(
        RUTA_RESULTADOS / "prueba_hipotesis_apareada.csv",
        index=False,
    )
    generar_figura(
        pares,
        RUTA_RESULTADOS / "figura_comparacion_pareada.png",
    )

    conteos = mapa["origen_real"].value_counts()

    print("=== SICST: análisis reproducible completado ===")
    print(f"ITEM reconstruidos: {len(mapa)}")
    print(f"RF humanos: {int(conteos.get('human', 0))}")
    print(f"RF LLM: {int(conteos.get('llm', 0))}")
    print(f"Pares estrictos: {len(pares)}")
    print(f"Resultados: {RUTA_RESULTADOS}")
    print()
    print(resultado.to_string(index=False))


if __name__ == "__main__":
    main()
