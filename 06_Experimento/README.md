# Experimento SICST — Enfoque 1: calidad de RF humano vs. LLM

## Descripción

Este directorio contiene los artefactos del experimento comparativo del
**Sistema Inteligente de Control y Seguimiento de Terapia Física (SICST)**,
registrado en OSF con DOI `10.17605/OSF.IO/82Q76`.

El estudio compara:

1. **33 RF humanos**, obtenidos durante el proceso normal de ingeniería de
   requisitos del SICST.
2. **33 RF generados por GPT-5.5-mini**, usando como corpus fuente las mismas
   transcripciones anonimizadas empleadas durante la elicitación.

Las entrevistas pertenecen a una etapa previa de levantamiento de requisitos.
Posteriormente, sus transcripciones anonimizadas se reutilizaron como corpus
fuente fijo para el brazo LLM.

## Pregunta de investigación

¿Existen diferencias significativas en la calidad de los requisitos
funcionales obtenidos mediante un proceso humano de ingeniería de requisitos
y aquellos generados mediante un modelo de lenguaje?

**H0:** No existen diferencias estadísticamente significativas.  
**H1:** Existen diferencias estadísticamente significativas.

## Registro previo

- **OSF ID:** `82q76`
- **DOI:** `10.17605/OSF.IO/82Q76`
- **Fecha UTC:** `2026-09-13T00:50:38.265668Z`
- **Ecuador continental (UTC-5):** `2026-09-12 19:50:38`

El preregistro corresponde al experimento comparativo humano-LLM. Las
entrevistas originales ya existían previamente como parte de la elicitación.
La fase comparativa utiliza esas transcripciones como corpus fuente fijo.

La evidencia verificable se conserva en:

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
- Análisis confirmatorio sobre 11 pares temáticos estrictos.
- Shapiro-Wilk sobre las diferencias.
- t de Student apareada o Wilcoxon de rangos con signo.
- Corrección Holm-Bonferroni sobre las cinco dimensiones.
- Diferencia media humano − LLM con IC bootstrap del 95 %.
- Cohen's dz con IC bootstrap del 95 %.
- 10 000 remuestreos bootstrap con semilla base 42.

## Cegado y reconstrucción post-evaluación

Las hojas entregadas a los evaluadores contienen identificadores `ITEM-xxx`
y el texto del requisito, pero no una columna que revele si el requisito
proviene del proceso humano o del LLM.

Una vez terminada la evaluación, el script reconstruye de forma determinista
la correspondencia:

`ITEM -> origen -> RF real`

comparando el texto de:

- `datos_crudos/hoja_evaluacion_ciega.csv`
- `datos_procesados/matriz_trazabilidad_tema_RF.csv`

Por tanto, **no se requiere un archivo externo llamado
`clave_privada_desciego.csv`**.

La reconstrucción se valida automáticamente: deben obtenerse exactamente
66 ítems, distribuidos en 33 humanos y 33 LLM, sin coincidencias faltantes
ni ambiguas.

El mapa reconstruido se guarda en:

`resultados/mapa_origen_items_reconstruido.csv`

## Reproducción

Desde la raíz del repositorio:

```bash
python -m pip install -r 06_Experimento/scripts_analisis/requirements.txt
python 06_Experimento/scripts_analisis/analisis_experimento_llm_humano.py
```

El script resuelve automáticamente todas las rutas y escribe las salidas en
`06_Experimento/resultados/`.

## Regla de consistencia

Los resultados, el ERS y el manuscrito deben utilizar las cifras producidas
por la misma ejecución reproducible. Si una cifra cambia al regenerar el
análisis, debe actualizarse el documento desfasado; no deben editarse los
CSV manualmente para forzar coincidencias.
