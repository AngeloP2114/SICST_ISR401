# Resultados del experimento SICST — Enfoque 1

Resultados de la evaluación ciega comparativa de calidad de Requisitos
Funcionales (RF) elicitados por humanos vs. generados por el LLM
GPT-5.5-mini, generados por
`../scripts_analisis/analisis_experimento_llm_humano.py`.

## Diseño del análisis (corregido según Sección 4.1 de la guía)

El Enfoque 1 exige un **análisis apareado**, no una comparación de grupos
independientes. Se usaron los **11 pares temáticos estrictos** identificados
en `../datos_procesados/matriz_trazabilidad_tema_RF.csv` (columna
`tipo == "pareado"`): cada par corresponde a un RF humano y un RF del LLM
que abordan exactamente el mismo tema. Los 22 ítems restantes de los 66
totales (parejas parciales, débiles, o sin contrapartida temática) se
excluyeron del análisis estadístico principal por no ser comparables 1 a 1,
y se conservan solo como referencia descriptiva en la matriz de
trazabilidad.

Para cada dimensión, se aplicó prueba t apareada (si las diferencias por
par no rechazaban normalidad según Shapiro-Wilk) o Wilcoxon de rangos con
signo (en caso contrario), con corrección de **Holm-Bonferroni** por las 5
comparaciones múltiples (una por dimensión).

## Archivos

- **`fleiss_kappa.csv`** — Acuerdo entre los 4 evaluadores (κ de Fleiss),
  calculado sobre los 66 ítems totales (no depende del pareo).
- **`descriptivos_por_grupo.csv`** — Estadísticos descriptivos por grupo
  (humano/LLM) sobre los 66 ítems totales, para contexto general.
- **`pares_estrictos_utilizados.csv`** — Los 11 pares temáticos usados en
  el análisis principal, con el puntaje de cada RF humano y su contraparte
  LLM en las 5 dimensiones.
- **`prueba_hipotesis_apareada.csv`** — Prueba de normalidad de las
  diferencias, prueba aplicada, estadístico, valor p crudo y valor p
  ajustado por Holm-Bonferroni, para cada dimensión.
- **`figura_comparacion_pareada.png`** — Gráfico de líneas pareadas
  (humano-LLM) por cada uno de los 11 temas.

## Hallazgos principales

**Acuerdo entre evaluadores bajo.** El κ de Fleiss osciló entre -0.01 y
0.17 según la dimensión. Se reporta como limitación metodológica en el
manuscrito.

**Sin diferencia estadísticamente significativa (análisis apareado, n=11,
Holm-Bonferroni).** Ninguna de las 5 dimensiones mostró diferencia
significativa tras la corrección por comparaciones múltiples (todos los
valores p ajustados entre 0.76 y 1.00). No se pudo rechazar H0. Este es el
resultado principal del estudio, reportado tal como se obtuvo, sin ajustes
posteriores.

## Reproducibilidad

```bash
cd ../scripts_analisis
python analisis_experimento_llm_humano.py
```

## Nota sobre una versión anterior de este análisis

Una versión previa del script comparó los 33 RF humanos contra los 33 RF
del LLM como grupos independientes (t/Mann-Whitney), sin usar el pareo
temático. Se corrigió porque la Sección 4.1 de la guía exige explícitamente
un diseño apareado para el Enfoque 1. La conclusión sustantiva no cambió
(sin diferencia significativa), pero el método ahora sigue exactamente lo
que exige la guía.
