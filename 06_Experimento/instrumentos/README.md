# Instrumentos del experimento SICST — Enfoque 1

## Objetivo

Definir el instrumento utilizado para evaluar comparativamente la calidad de
los Requisitos Funcionales (RF) del Sistema Inteligente de Control y
Seguimiento de Terapia Física (SICST), tanto los elicitados por el equipo
humano como los generados por el LLM.

## Instrumento utilizado

### Rúbrica de evaluación de calidad de RF (escala Likert 1-5)

Archivo: `rubrica_evaluacion_requisitos.md`

5 dimensiones de calidad, cada una puntuada de 1 (no cumple en absoluto) a
5 (cumple totalmente):

- Completitud
- Ausencia de ambigüedad
- Verificabilidad
- Corrección respecto a la fuente
- Consistencia interna

### Listado de ítems a evaluar (anonimizado)

Archivo: `../datos_crudos/hoja_evaluacion_ciega.csv`

66 ítems (33 RF humanos + 33 RF del LLM), organizados en un único listado
sin indicar el origen de cada uno, para preservar el cegado de los
evaluadores.

### Hojas de evaluación por juez

Archivos: `../datos_crudos/evaluaciones_ciegas/Evaluacion_*.xlsx`

Cada uno de los 4 evaluadores independientes (Mishell, Angel, Dayana, Sebas)
completó su propia hoja, puntuando los 66 ítems en las 5 dimensiones.

## Procedimiento de aplicación

1. Se generaron los 33 RF del LLM a partir de las mismas transcripciones
   usadas en la elicitación humana (ver `../prompts_llm/`).
2. Se organizaron los 66 RF (humanos + LLM) en un listado único anonimizado.
3. El listado se entregó a 4 evaluadores independientes, sin revelar el
   origen de cada ítem.
4. Cada evaluador puntuó los 66 ítems en las 5 dimensiones mediante escala
   Likert 1-5.
5. Los resultados se procesaron mediante el script en `../scripts_analisis/`,
   que descifra el origen real de cada ítem (mediante la clave privada
   cifrada en `02_Evidencias/00_Restringido/`) solo después de calcular el
   acuerdo entre evaluadores, para el análisis comparativo final.

## Nota sobre un instrumento anterior descartado

Este instrumento reemplaza una rúbrica binaria (1=cumple/0=no cumple) usada
en una exploración anterior del proyecto, descartada en favor de este
diseño de evaluación ciega comparativa, que es el efectivamente
pre-registrado en OSF y ejecutado.

