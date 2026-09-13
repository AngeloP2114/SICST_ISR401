# Experimento SICST — Enfoque 1: Calidad de RF humano vs. LLM

## Descripción

Este directorio contiene los artefactos del experimento comparativo
registrado en OSF (https://doi.org/10.17605/OSF.IO/82Q76): evaluación de la
calidad de los Requisitos Funcionales (RF) del **Sistema Inteligente de
Control y Seguimiento de Terapia Física (SICST)**, comparando dos fuentes
de generación:

1. RF elicitados mediante el proceso humano de ingeniería de requisitos, a
   partir de 18 entrevistas con fisioterapeutas, familiares/cuidadores y
   pacientes.
2. RF generados por el modelo GPT-5.5-mini a partir de las mismas 18
   transcripciones anonimizadas.

## Pregunta de investigación

¿Existen diferencias significativas en la calidad de los requisitos
funcionales generados mediante un proceso humano de ingeniería de
requisitos y aquellos generados mediante un modelo de lenguaje (LLM)?

**H0:** No existen diferencias estadísticamente significativas.
**H1:** Existen diferencias estadísticamente significativas.

## Diseño

Estudio comparativo no experimental, con evaluación ciega: 66 requisitos
(33 humanos + 33 del LLM) fueron anonimizados y organizados en un único
listado, evaluado independientemente por 4 jueces (Mishell, Angel, Dayana,
Sebas) mediante una rúbrica de 5 dimensiones en escala Likert de 1 a 5:
completitud, ausencia de ambigüedad, verificabilidad, corrección respecto a
la fuente, y consistencia interna.

## Metodología, etapa por etapa

### 1. Generación de RF por LLM

El modelo GPT-5.5-mini generó los 33 RF a partir de las mismas transcripciones
usadas en la elicitación humana. Prompt exacto, modelo, fecha y confirmación
de no uso de información externa documentados en:

```
prompts_llm/prompt_generacion_RF_llm.md
```

### 2. Anonimización y evaluación ciega

Los 66 RF (humanos + LLM) se organizaron en un listado único sin indicar su
origen, entregado a 4 evaluadores independientes:

```
datos_crudos/hoja_evaluacion_ciega.csv
datos_crudos/evaluaciones_ciegas/Evaluacion_Mishell.xlsx
datos_crudos/evaluaciones_ciegas/Evaluacion_Angel.xlsx
datos_crudos/evaluaciones_ciegas/Evaluacion_Dayana.xlsx
datos_crudos/evaluaciones_ciegas/Evaluacion_sebas.xlsx
```

La clave que revela el origen real de cada ítem (`clave_privada_desciego.csv`)
se mantiene cifrada en `02_Evidencias/00_Restringido/`, nunca en texto plano
en esta carpeta, para preservar la integridad del cegado frente a cualquiera
que audite el repositorio.

### 3. Pareo temático humano-LLM

```
datos_procesados/matriz_trazabilidad_tema_RF.csv
```

### 4. Análisis estadístico

```
scripts_analisis/analisis_experimento_llm_humano.py
```

Calcula acuerdo entre evaluadores (κ de Fleiss), pruebas de normalidad,
comparación de grupos (t de Student o U de Mann-Whitney según corresponda),
y tamaño del efecto (δ de Cliff con IC 95% por bootstrap). Ver
`scripts_analisis/README.md` para el detalle de ejecución.

### 5. Resultados

```
resultados/descriptivos_por_grupo.csv
resultados/fleiss_kappa.csv
resultados/prueba_hipotesis.csv
resultados/figura_comparacion_grupos.png
```

Ver `resultados/README.md` para la interpretación de estos hallazgos.

## Estructura del experimento

```
06_Experimento/
├── README.md                        (este archivo)
├── protocolo.pdf
├── osf_registration.pdf
├── osf_deviations.pdf
├── justificacion_muestra.md
├── referencias.bib
│
├── instrumentos/
│   ├── README.md
│   └── rubrica_evaluacion_requisitos.md
│
├── prompts_llm/
│   └── prompt_generacion_RF_llm.md
│
├── datos_crudos/
│   ├── requisitos_llm.csv
│   ├── hoja_evaluacion_ciega.csv
│   └── evaluaciones_ciegas/
│       ├── Evaluacion_Mishell.xlsx
│       ├── Evaluacion_Angel.xlsx
│       ├── Evaluacion_Dayana.xlsx
│       └── Evaluacion_sebas.xlsx
│
├── datos_procesados/
│   ├── README.md
│   └── matriz_trazabilidad_tema_RF.csv
│
├── scripts_analisis/
│   ├── README.md
│   ├── analisis_experimento_llm_humano.py
│   └── requirements.txt
│
└── resultados/
    ├── README.md
    ├── descriptivos_por_grupo.csv
    ├── fleiss_kappa.csv
    ├── prueba_hipotesis.csv
    └── figura_comparacion_grupos.png
```

## Reproducibilidad

```bash
cd scripts_analisis
pip install -r requirements.txt
python analisis_experimento_llm_humano.py
```

Los archivos generados en `resultados/` deben coincidir exactamente con los
ya versionados en este repositorio y con las cifras citadas en el
manuscrito.

## Documentación adicional

- `justificacion_muestra.md` — justificación del tamaño de muestra y de
  evaluadores.
- `protocolo.pdf` — diseño experimental completo (pregunta, hipótesis,
  cegado, plan de análisis).
- `osf_registration.pdf` — comprobante externo del pre-registro
  (DOI 10.17605/OSF.IO/82Q76, fecha 2026-09-12).
- `osf_deviations.pdf` — comparación entre lo registrado y lo ejecutado.
- `referencias.bib` — soporte bibliográfico.

## Nota sobre un enfoque anterior descartado

Una exploración inicial sobre explicabilidad percibida del sistema (con
datos sintéticos de simulación) fue descartada en una etapa previa del
proyecto, en favor de este Enfoque 1 (LLM vs. humano), que es el
formalmente pre-registrado en OSF y evaluado en esta entrega.

