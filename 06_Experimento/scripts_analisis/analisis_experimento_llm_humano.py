"""
Analisis del experimento comparativo: RF elicitados por humanos vs generados por LLM
Proyecto SICST - ISR-401 - Enfoque 1

Registrado en OSF: https://doi.org/10.17605/OSF.IO/82Q76

CORRECCION METODOLOGICA (respecto de la version anterior del script):
La Seccion 4.1 de la guia exige un ANALISIS APAREADO para el Enfoque 1, no un
analisis de grupos independientes. Este script usa los 11 pares estrictos
("pareado") de matriz_trazabilidad_tema_RF.csv -- RF humano y RF LLM que
abordan el mismo tema -- y aplica prueba t apareada o Wilcoxon de rangos con
signo segun corresponda, con correccion de Holm-Bonferroni por comparaciones
multiples (5 dimensiones evaluadas simultaneamente), tal como exige la guia.

Los items sin contrapartida tematica ("solo_humano", "solo_llm") y los pares
debiles o parciales ("pareado_parcial", "pareado_debil") se excluyen del
analisis principal por no ser comparables 1 a 1, y se reportan aparte como
nota descriptiva, no como evidencia estadistica.

Entradas (todas en datos_crudos/ y datos_procesados/):
  - hoja_evaluacion_ciega.csv
  - evaluaciones_ciegas/*.xlsx (4 evaluadores)
  - matriz_trazabilidad_tema_RF.csv

Entrada RESTRINGIDA (02_Evidencias/00_Restringido/, cifrada):
  - clave_privada_desciego.csv

Salidas (a resultados/):
  - descriptivos_por_grupo.csv
  - fleiss_kappa.csv
  - prueba_hipotesis_apareada.csv
  - figura_comparacion_pareada.png

Ejecucion:
  python analisis_experimento_llm_humano.py
"""

import pandas as pd
import numpy as np
from scipy import stats
from statsmodels.stats.multitest import multipletests
import warnings
warnings.filterwarnings("ignore")

DIMENSIONES = [
    "completitud", "ausencia_ambiguedad", "verificabilidad",
    "correccion_fuente", "consistencia_interna",
]

EVALUADORES = {
    "Mishell": "Evaluacion_Mishell.xlsx",
    "Angel": "Evaluacion_Angel.xlsx",
    "Dayana": "Evaluacion_Dayana.xlsx",
    "sebas": "Evaluacion_sebas.xlsx",
}

RUTA_DATOS = "."


# ---------------------------------------------------------------------------
# 1. Carga de datos
# ---------------------------------------------------------------------------

def cargar_evaluaciones():
    filas = []
    for nombre, archivo in EVALUADORES.items():
        df = pd.read_excel(f"{RUTA_DATOS}/{archivo}", sheet_name="Evaluación")
        df = df[df["item_id"] != "EJEMPLO"].copy()
        for _, row in df.iterrows():
            for dim in DIMENSIONES:
                filas.append({
                    "item_id": row["item_id"],
                    "evaluador": nombre,
                    "dimension": dim,
                    "puntaje": row[dim],
                })
    return pd.DataFrame(filas)


def cargar_clave():
    return pd.read_csv(f"{RUTA_DATOS}/clave_privada_desciego.csv")


def cargar_matriz_trazabilidad():
    return pd.read_csv(f"{RUTA_DATOS}/matriz_trazabilidad_tema_RF.csv")


# ---------------------------------------------------------------------------
# 2. Acuerdo entre evaluadores -- Fleiss' kappa (sin cambios, es sobre TODOS
#    los items, no depende del pareo)
# ---------------------------------------------------------------------------

def fleiss_kappa(tabla_conteos):
    n_items, n_categorias = tabla_conteos.shape
    n_evaluadores = tabla_conteos.sum(axis=1)[0]
    p_j = tabla_conteos.sum(axis=0) / (n_items * n_evaluadores)
    P_e = (p_j ** 2).sum()
    P_i = (
        (tabla_conteos * (tabla_conteos - 1)).sum(axis=1)
        / (n_evaluadores * (n_evaluadores - 1))
    )
    P_bar = P_i.mean()
    kappa = (P_bar - P_e) / (1 - P_e) if (1 - P_e) != 0 else np.nan
    return kappa


def calcular_fleiss_por_dimension(df_largo):
    resultados = []
    for dim in DIMENSIONES:
        sub = df_largo[df_largo["dimension"] == dim]
        tabla = sub.pivot_table(index="item_id", columns="puntaje",
                                 aggfunc="size", fill_value=0)
        for cat in range(1, 6):
            if cat not in tabla.columns:
                tabla[cat] = 0
        tabla = tabla[[1, 2, 3, 4, 5]].values
        k = fleiss_kappa(tabla)
        resultados.append({"dimension": dim, "fleiss_kappa": round(k, 4)})
    return pd.DataFrame(resultados)


# ---------------------------------------------------------------------------
# 3. Tabla de puntaje promedio por item (promedio de los 4 evaluadores)
# ---------------------------------------------------------------------------

def construir_tabla_por_item(df_largo, clave):
    prom = (
        df_largo.groupby(["item_id", "dimension"])["puntaje"]
        .mean()
        .reset_index()
        .pivot(index="item_id", columns="dimension", values="puntaje")
        .reset_index()
    )
    prom = prom.merge(clave, on="item_id", how="left")
    prom["puntaje_global"] = prom[DIMENSIONES].mean(axis=1)
    return prom


# ---------------------------------------------------------------------------
# 4. Construir los pares reales humano-LLM (solo tipo == 'pareado')
# ---------------------------------------------------------------------------

def construir_pares(tabla_item, matriz):
    pares_estrictos = matriz[matriz["tipo"] == "pareado"].copy()

    # tabla_item tiene una fila por item_id anonimizado; necesitamos indexar
    # por (origen_real, id_real) para encontrar el puntaje de cada RF real.
    tabla_item_idx = tabla_item.set_index(["origen_real", "id_real"])

    filas = []
    for _, fila in pares_estrictos.iterrows():
        try:
            score_h = tabla_item_idx.loc[("human", fila["rf_humano_id"])]
            score_l = tabla_item_idx.loc[("llm", fila["rf_llm_id"])]
        except KeyError:
            continue  # el RF no fue evaluado (no deberia pasar, pero por si acaso)
        registro = {"tema_id": fila["tema_id"],
                    "rf_humano_id": fila["rf_humano_id"],
                    "rf_llm_id": fila["rf_llm_id"]}
        for dim in DIMENSIONES + ["puntaje_global"]:
            registro[f"{dim}_humano"] = score_h[dim]
            registro[f"{dim}_llm"] = score_l[dim]
        filas.append(registro)

    return pd.DataFrame(filas)


# ---------------------------------------------------------------------------
# 5. Descriptivos por grupo (sobre TODOS los items, para contexto general)
# ---------------------------------------------------------------------------

def descriptivos_por_grupo(tabla_item):
    filas = []
    for dim in DIMENSIONES + ["puntaje_global"]:
        for origen in ["human", "llm"]:
            datos = tabla_item.loc[tabla_item["origen_real"] == origen, dim]
            filas.append({
                "dimension": dim, "grupo": origen, "n": len(datos),
                "media": round(datos.mean(), 3),
                "mediana": round(datos.median(), 3),
                "de": round(datos.std(), 3),
                "min": datos.min(), "max": datos.max(),
                "iqr": round(datos.quantile(0.75) - datos.quantile(0.25), 3),
            })
    return pd.DataFrame(filas)


# ---------------------------------------------------------------------------
# 6. Tamaño del efecto -- delta de Cliff (para datos apareados, usamos las
#    diferencias por par)
# ---------------------------------------------------------------------------

def bootstrap_ci_media_diff(diffs, n_boot=10000, seed=42):
    rng = np.random.default_rng(seed)
    medias = []
    for _ in range(n_boot):
        muestra = rng.choice(diffs, size=len(diffs), replace=True)
        medias.append(muestra.mean())
    lo, hi = np.percentile(medias, [2.5, 97.5])
    return lo, hi


# ---------------------------------------------------------------------------
# 7. Analisis apareado con Holm-Bonferroni (el corregido)
# ---------------------------------------------------------------------------

def analisis_apareado(pares):
    n = len(pares)
    resultados = []
    p_valores_crudos = []

    for dim in DIMENSIONES + ["puntaje_global"]:
        h = pares[f"{dim}_humano"].values
        l = pares[f"{dim}_llm"].values
        diffs = h - l

        if np.all(diffs == 0):
            # scipy no permite Wilcoxon si todas las diferencias son 0
            stat, p, prueba, normal = np.nan, 1.0, "sin variacion", None
        else:
            _, p_norm = stats.shapiro(diffs)
            normal = p_norm > 0.05
            if normal:
                stat, p = stats.ttest_rel(h, l)
                prueba = "t apareada"
            else:
                stat, p = stats.wilcoxon(h, l)
                prueba = "Wilcoxon rangos con signo"

        media_diff = diffs.mean()
        ci_lo, ci_hi = bootstrap_ci_media_diff(diffs) if not np.all(diffs == 0) else (0, 0)

        resultados.append({
            "dimension": dim, "n_pares": n, "prueba": prueba,
            "normal_shapiro_diffs": normal,
            "estadistico": round(stat, 4) if not np.isnan(stat) else np.nan,
            "valor_p_crudo": round(p, 4),
            "media_diferencia_humano_menos_llm": round(media_diff, 4),
            "ic95_diferencia_lo": round(ci_lo, 4),
            "ic95_diferencia_hi": round(ci_hi, 4),
        })
        p_valores_crudos.append(p)

    # Correccion de Holm-Bonferroni por comparaciones multiples (5 dimensiones
    # + el puntaje global se corrige aparte, ya que no es una dimension nueva
    # independiente sino un resumen -- se reporta sin corregir, marcado como tal)
    p_dims = p_valores_crudos[:-1]  # las 5 dimensiones, sin el puntaje_global
    rechazado, p_ajustado, _, _ = multipletests(p_dims, alpha=0.05, method="holm")

    df_resultados = pd.DataFrame(resultados)
    df_resultados["valor_p_holm"] = list(p_ajustado) + [np.nan]  # NaN para puntaje_global
    df_resultados["significativo_holm_0.05"] = list(rechazado) + [None]

    return df_resultados


# ---------------------------------------------------------------------------
# 8. Figura
# ---------------------------------------------------------------------------

def generar_figura(pares, ruta_salida):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(7, 5))
    h = pares["puntaje_global_humano"].values
    l = pares["puntaje_global_llm"].values

    for i in range(len(pares)):
        ax.plot([0, 1], [h[i], l[i]], color="gray", alpha=0.4, linewidth=1)
    ax.scatter([0] * len(h), h, color="#2563eb", zorder=3, label="Humano")
    ax.scatter([1] * len(l), l, color="#dc2626", zorder=3, label="LLM")
    ax.set_xticks([0, 1])
    ax.set_xticklabels(["Humano", "LLM"])
    ax.set_ylabel("Puntaje global (promedio 5 dimensiones, escala 1-5)")
    ax.set_title(f"Comparación pareada por tema (n={len(pares)} pares) — SICST")
    ax.legend()
    plt.tight_layout()
    plt.savefig(ruta_salida, dpi=150)
    plt.close()


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------

def main():
    df_largo = cargar_evaluaciones()
    clave = cargar_clave()
    matriz = cargar_matriz_trazabilidad()

    fleiss = calcular_fleiss_por_dimension(df_largo)
    tabla_item = construir_tabla_por_item(df_largo, clave)
    descriptivos = descriptivos_por_grupo(tabla_item)

    pares = construir_pares(tabla_item, matriz)
    resultado_apareado = analisis_apareado(pares)

    fleiss.to_csv("fleiss_kappa.csv", index=False)
    descriptivos.to_csv("descriptivos_por_grupo.csv", index=False)
    resultado_apareado.to_csv("prueba_hipotesis_apareada.csv", index=False)
    pares.to_csv("pares_estrictos_utilizados.csv", index=False)
    generar_figura(pares, "figura_comparacion_pareada.png")

    print("=== ACUERDO ENTRE EVALUADORES (Fleiss' kappa, todos los items) ===")
    print(fleiss.to_string(index=False))
    print()
    print(f"=== ANALISIS APAREADO (n={len(pares)} pares estrictos, tipo='pareado') ===")
    print(resultado_apareado.to_string(index=False))
    print()
    print("Archivos generados: descriptivos_por_grupo.csv, fleiss_kappa.csv,")
    print("prueba_hipotesis_apareada.csv, pares_estrictos_utilizados.csv,")
    print("figura_comparacion_pareada.png")


if __name__ == "__main__":
    main()
