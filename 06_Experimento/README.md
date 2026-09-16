# Experimento SICST — Enfoque 1: calidad de RF humano vs. LLM

## Descripción

Este directorio contiene los artefactos del experimento comparativo del
**Sistema Inteligente de Control y Seguimiento de Terapia Física (SICST)**,
registrado en OSF con DOI `10.17605/OSF.IO/82Q76`.

El estudio compara dos fuentes de Requisitos Funcionales (RF):

1. **33 RF humanos**, obtenidos durante el proceso normal de ingeniería de
   requisitos del SICST.
2. **33 RF generados por GPT-5.5-mini**, usando como corpus fuente las mismas
   18 transcripciones anonimizadas empleadas durante la elicitación.

Las entrevistas pertenecen a una etapa previa de levantamiento de requisitos.
Posteriormente, sus transcripciones anonimizadas se reutilizaron como un
**corpus fuente fijo** para el brazo LLM del experimento.

## Pregunta de investigación

¿Existen diferencias significativas en la calidad de los requisitos
funcionales obtenidos mediante un proceso humano de ingeniería de requisitos
y aquellos generados mediante un modelo de lenguaje (LLM)?

**H0:** No existen diferencias estadísticamente significativas.  
**H1:** Existen diferencias estadísticamente significativas.

## Registro previo

El experimento comparativo está registrado en OSF:

- **ID:** `82q76`
- **DOI:** `10.17605/OSF.IO/82Q76`
- **Fecha UTC reportada por OSF:** `2026-09-13T00:50:38.265668Z`
- **Hora Ecuador continental (UTC-5):** `2026-09-12 19:50:38`

El registro previo corresponde al experimento comparativo humano-LLM y
precede a la generación documentada del conjunto LLM y a la recolección de
las puntuaciones de la evaluación ciega utilizadas en el análisis.

Las entrevistas originales ya existían porque fueron producidas durante la
etapa previa de elicitación. No se presentan como datos experimentales
recogidos después del preregistro.

La evidencia verificable está en:

```text
registro_previo/
├── README.md
├── consulta.json
└── osf_registration.pdf
```

## Diseño

- 66 RF evaluados: 33 humanos + 33 LLM.
- 4 evaluadores independientes.
- Evaluación ciega.
- 5 dimensiones Likert de 1 a 5:
  - completitud;
  - ausencia de ambigüedad;
  - verificabilidad;
  - corrección respecto a la fuente;
  - consistencia interna.
- κ de Fleiss sobre los 66 ítems.
- Análisis confirmatorio sobre **11 pares temáticos estrictos**.
- Shapiro-Wilk sobre las diferencias de cada par.
- t de Student apareada o Wilcoxon de rangos con signo.
- Corrección Holm-Bonferroni sobre las cinco dimensiones.
- Diferencia media humano − LLM con IC bootstrap del 95 %.
- Cohen's dz con IC bootstrap del 95 %.
- 10 000 remuestreos bootstrap con semilla 42.

## Estructura

```text
06_Experimento/
├── README.md
├── protocolo.pdf
├── osf_deviations.pdf
├── justificacion_muestra.md
├── registro_previo/
│   ├── README.md
│   ├── consulta.json
│   └── osf_registration.pdf
├── instrumentos/
│   ├── README.md
│   └── rubrica_evaluacion_requisitos.md
├── prompts_llm/
│   └── prompt_generacion_RF_llm.md
├── datos_crudos/
│   ├── requisitos_llm.csv
│   ├── hoja_evaluacion_ciega.csv
│   └── evaluaciones_ciegas/
│       ├── Evaluacion_Mishell.xlsx
│       ├── Evaluacion_Angel.xlsx
│       ├── Evaluacion_Dayana.xlsx
│       └── Evaluacion_sebas.xlsx
├── datos_procesados/
│   ├── README.md
│   └── matriz_trazabilidad_tema_RF.csv
├── scripts_analisis/
│   ├── README.md
│   ├── analisis_experimento_llm_humano.py
│   └── requirements.txt
└── resultados/
    ├── README.md
    ├── descriptivos_por_grupo.csv
    ├── fleiss_kappa.csv
    ├── pares_estrictos_utilizados.csv
    ├── prueba_hipotesis_apareada.csv
    └── figura_comparacion_pareada.png
```

## Clave de desciego

La relación entre el identificador ciego y el origen real de cada RF no se
publica en texto plano. La copia maestra se conserva en la zona restringida
cifrada del proyecto.

Para reproducir el análisis, una persona autorizada debe extraer localmente
`clave_privada_desciego.csv` y pasar su ruta mediante `--clave`.

La clave **no debe añadirse al repositorio público**.

## Reproducción

Desde la raíz del repositorio:

```bash
python -m pip install -r 06_Experimento/scripts_analisis/requirements.txt

python 06_Experimento/scripts_analisis/analisis_experimento_llm_humano.py \
  --clave /ruta/local/clave_privada_desciego.csv
```

El script resuelve automáticamente las rutas de los XLSX, de la matriz
temática y de la carpeta `resultados/`.

## Regla de consistencia

Los archivos de `resultados/`, las cifras del ERS y las cifras del manuscrito
deben provenir de la misma ejecución reproducible. Si una cifra cambia al
regenerar los resultados, debe actualizarse el documento desfasado; no deben
editarse manualmente las salidas para forzar coincidencias.
