"""
Analisis del experimento comparativo: RF elicitados por humanos vs generados por LLM
Proyecto SICST - ISR-401

Registrado en OSF: https://doi.org/10.17605/OSF.IO/82Q76

Entradas (todas en datos_crudos/):
  - hoja_evaluacion_ciega.csv        : items anonimizados enviados a evaluadores
  - evaluaciones_ciegas/*.xlsx       : 4 evaluadores independientes, escala Likert 1-5,
                                       5 dimensiones: completitud, ausencia_ambiguedad,
                                       verificabilidad, correccion_fuente, consistencia_interna
  - matriz_trazabilidad_tema_RF.csv : pareo humano<->LLM por tema (en datos_procesados/)

Entrada RESTRINGIDA (02_Evidencias/00_Restringido/, cifrada):
  - clave_privada_desciego.csv       : mapea item_id -> origen_real (human/llm) + id_real

Salidas (todas a resultados/):
  - descriptivos_por_grupo.csv
  - fleiss_kappa.csv
  - prueba_hipotesis.csv
  - tabla_resultados_manuscrito.csv
  - figura_comparacion_grupos.png

Ejecucion:
  python analisis_experimento_llm_humano.py
"""

import pandas as pd
import numpy as np
from scipy import stats
import itertools
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

RUTA_DATOS = "."  # ajustar si se ejecuta desde otra carpeta


# ---------------------------------------------------------------------------
# 1. Carga de datos
# ---------------------------------------------------------------------------

def cargar_evaluaciones():
    """Devuelve un DataFrame largo: item_id, evaluador, dimension, puntaje."""
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
# 2. Acuerdo entre evaluadores -- Fleiss' kappa
# ---------------------------------------------------------------------------

def fleiss_kappa(tabla_conteos):
    """
    tabla_conteos: matriz (n_items x n_categorias) con el numero de evaluadores
    que asignaron cada categoria (1-5) a cada item.
    """
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
        tabla = (
            sub.pivot_table(index="item_id", columns="puntaje",
                             aggfunc="size", fill_value=0)
        )
        for cat in range(1, 6):
            if cat not in tabla.columns:
                tabla[cat] = 0
        tabla = tabla[[1, 2, 3, 4, 5]].values
        k = fleiss_kappa(tabla)
        resultados.append({"dimension": dim, "fleiss_kappa": round(k, 4)})
    return pd.DataFrame(resultados)


# ---------------------------------------------------------------------------
# 3. Union con el origen real (via clave privada) y promedio entre evaluadores
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
# 4. Descriptivos por grupo (humano vs LLM)
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
# 5. Tamaño del efecto -- delta de Cliff (no parametrico, robusto)
# ---------------------------------------------------------------------------

def cliffs_delta(x, y):
    x, y = np.asarray(x), np.asarray(y)
    mayor = sum((xi > yj) for xi in x for yj in y)
    menor = sum((xi < yj) for xi in x for yj in y)
    return (mayor - menor) / (len(x) * len(y))


def bootstrap_ci_delta(x, y, n_boot=10000, seed=42):
    rng = np.random.default_rng(seed)
    deltas = []
    for _ in range(n_boot):
        xs = rng.choice(x, size=len(x), replace=True)
        ys = rng.choice(y, size=len(y), replace=True)
        deltas.append(cliffs_delta(xs, ys))
    lo, hi = np.percentile(deltas, [2.5, 97.5])
    return lo, hi


# ---------------------------------------------------------------------------
# 6. Comparacion entre grupos (independiente) por dimension
# ---------------------------------------------------------------------------

def comparar_grupos(tabla_item):
    filas = []
    for dim in DIMENSIONES + ["puntaje_global"]:
        human = tabla_item.loc[tabla_item["origen_real"] == "human", dim].values
        llm = tabla_item.loc[tabla_item["origen_real"] == "llm", dim].values

        _, p_norm_h = stats.shapiro(human)
        _, p_norm_l = stats.shapiro(llm)
        normal = (p_norm_h > 0.05) and (p_norm_l > 0.05)

        if normal:
            stat, p = stats.ttest_ind(human, llm)
            prueba = "t de Student (muestras independientes)"
        else:
            stat, p = stats.mannwhitneyu(human, llm, alternative="two-sided")
            prueba = "U de Mann-Whitney"

        delta = cliffs_delta(human, llm)
        ci_lo, ci_hi = bootstrap_ci_delta(human, llm)

        filas.append({
            "dimension": dim,
            "prueba": prueba,
            "normal_shapiro": normal,
            "p_shapiro_human": round(p_norm_h, 4),
            "p_shapiro_llm": round(p_norm_l, 4),
            "estadistico": round(stat, 4),
            "valor_p": round(p, 4),
            "cliffs_delta": round(delta, 4),
            "ic95_lo": round(ci_lo, 4),
            "ic95_hi": round(ci_hi, 4),
        })
    return pd.DataFrame(filas)


# ---------------------------------------------------------------------------
# 7. Figura de resultados
# ---------------------------------------------------------------------------

def generar_figura(tabla_item, ruta_salida):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(8, 5))
    datos_plot = [
        tabla_item.loc[tabla_item["origen_real"] == "human", "puntaje_global"],
        tabla_item.loc[tabla_item["origen_real"] == "llm", "puntaje_global"],
    ]
    ax.boxplot(datos_plot, labels=["Humano", "LLM"])
    ax.set_ylabel("Puntaje global (promedio de 5 dimensiones, escala 1-5)")
    ax.set_title("Comparación de calidad de RF: humano vs LLM (SICST)")
    plt.tight_layout()
    plt.savefig(ruta_salida, dpi=150)
    plt.close()


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------

def main():
    df_largo = cargar_evaluaciones()
    clave = cargar_clave()

    fleiss = calcular_fleiss_por_dimension(df_largo)
    tabla_item = construir_tabla_por_item(df_largo, clave)
    descriptivos = descriptivos_por_grupo(tabla_item)
    comparacion = comparar_grupos(tabla_item)

    fleiss.to_csv("fleiss_kappa.csv", index=False)
    descriptivos.to_csv("descriptivos_por_grupo.csv", index=False)
    comparacion.to_csv("prueba_hipotesis.csv", index=False)
    generar_figura(tabla_item, "figura_comparacion_grupos.png")

    print("=== ACUERDO ENTRE EVALUADORES (Fleiss' kappa) ===")
    print(fleiss.to_string(index=False))
    print()
    print("=== DESCRIPTIVOS (puntaje_global) ===")
    print(descriptivos[descriptivos["dimension"] == "puntaje_global"].to_string(index=False))
    print()
    print("=== COMPARACION HUMANO vs LLM (puntaje_global) ===")
    print(comparacion[comparacion["dimension"] == "puntaje_global"].to_string(index=False))
    print()
    print("Archivos generados: descriptivos_por_grupo.csv, fleiss_kappa.csv,")
    print("prueba_hipotesis.csv, figura_comparacion_grupos.png")


if __name__ == "__main__":
    main()
