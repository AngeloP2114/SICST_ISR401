# Scripts de análisis — SICST, Enfoque 1 (RF humano vs LLM)

Esta carpeta contiene el script reproducible del experimento comparativo
registrado en OSF (https://doi.org/10.17605/OSF.IO/82Q76): calidad de
Requisitos Funcionales (RF) elicitados por humanos vs. generados por un LLM,
evaluados de forma ciega por 4 jueces independientes.

## Script principal

`analisis_experimento_llm_humano.py`

El script lee:

- `../datos_crudos/hoja_evaluacion_ciega.csv`
- `../datos_crudos/evaluaciones_ciegas/Evaluacion_*.xlsx` (4 evaluadores)
- `../../02_Evidencias/00_Restringido/` (clave de desciego, cifrada)

Y calcula:

- Acuerdo entre evaluadores (κ de Fleiss) por dimensión
- Estadísticos descriptivos por grupo (humano vs LLM)
- Prueba de normalidad (Shapiro-Wilk) y prueba de hipótesis correspondiente
  (t de Student o U de Mann-Whitney según corresponda)
- Tamaño del efecto (δ de Cliff) con intervalo de confianza al 95% por
  bootstrap
- Figura comparativa (boxplot) entre ambos grupos

## Ejecución

Desde la carpeta `06_Experimento/scripts_analisis/`:

```bash
pip install pandas scipy openpyxl matplotlib
python analisis_experimento_llm_humano.py
```

Genera en `../resultados/`:
- `descriptivos_por_grupo.csv`
- `fleiss_kappa.csv`
- `prueba_hipotesis.csv`
- `figura_comparacion_grupos.png`

## Nota sobre resultados

El acuerdo inter-evaluador (κ de Fleiss) resultó bajo en varias dimensiones
(rango entre -0.01 y 0.17). No se encontraron diferencias estadísticamente
significativas entre RF humanos y RF del LLM en ninguna dimensión (todos los
valores p > 0.05). Ambos hallazgos se reportan tal como salieron del
análisis, sin ajustes posteriores, y se discuten como limitaciones y
resultado principal respectivamente en el manuscrito.
