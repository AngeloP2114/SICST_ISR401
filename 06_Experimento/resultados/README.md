# Resultados del experimento SICST — Enfoque 1

Resultados obtenidos mediante la evaluación ciega comparativa de calidad de
Requisitos Funcionales (RF) elicitados por humanos vs. generados por el LLM
GPT-5.5-mini, generados por
`../scripts_analisis/analisis_experimento_llm_humano.py`.

## Archivos

- **`fleiss_kappa.csv`** — Acuerdo entre los 4 evaluadores (κ de Fleiss) por
  cada una de las 5 dimensiones.
- **`descriptivos_por_grupo.csv`** — Media, mediana, desviación estándar,
  mínimo, máximo y rango intercuartílico por grupo (humano/LLM) y dimensión.
- **`prueba_hipotesis.csv`** — Prueba de normalidad (Shapiro-Wilk), prueba de
  hipótesis aplicada (t de Student o U de Mann-Whitney), valor p, y tamaño
  del efecto (δ de Cliff) con intervalo de confianza al 95%.
- **`figura_comparacion_grupos.png`** — Boxplot comparativo del puntaje
  global entre ambos grupos.

## Hallazgos principales

**Acuerdo entre evaluadores bajo.** El κ de Fleiss osciló entre -0.01 y 0.17
según la dimensión, indicando un acuerdo débil a prácticamente nulo más allá
del azar entre los 4 jueces. Se reporta como limitación metodológica en el
manuscrito (sección de amenazas a la validez), no se ocultó ni se
recalculó excluyendo evaluadores.

**Sin diferencia estadísticamente significativa.** Ninguna de las 5
dimensiones mostró diferencia significativa entre RF humanos y RF del LLM
(todos los valores p > 0.05; el más cercano fue consistencia_interna,
p = 0.067). No se pudo rechazar H0. Este es el resultado principal del
estudio, reportado tal como se obtuvo.

## Reproducibilidad

```bash
cd ../scripts_analisis
python analisis_experimento_llm_humano.py
```

Debe regenerar exactamente estos 4 archivos a partir de los datos crudos.

## Nota sobre resultados anteriores descartados

Esta carpeta contenía previamente resultados de una exploración de
explicabilidad basada en datos sintéticos, descartada en favor de este
experimento real (Enfoque 1), formalmente pre-registrado en OSF.

