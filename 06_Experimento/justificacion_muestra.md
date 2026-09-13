# Justificación de la muestra del experimento — Enfoque 1

## Unidad de análisis

La unidad de análisis corresponde a los Requisitos Funcionales (RF) del
Sistema Inteligente de Control y Seguimiento de Terapia Física (SICST),
comparando dos fuentes de generación:

- **33 RF elicitados por el equipo humano**, a partir de 18 entrevistas con
  fisioterapeutas, familiares/cuidadores y pacientes.
- **33 RF generados por el modelo GPT-5.5-mini**, a partir de las mismas 18
  transcripciones anonimizadas.

Total: 66 ítems evaluados.

## Justificación del tamaño de muestra

El objetivo del experimento es comparar la calidad percibida de ambos
conjuntos de RF, no evaluar la percepción de usuarios finales del sistema.
Por eso la muestra corresponde directamente a los RF generados por cada
fuente, en igual cantidad (33 y 33), para que la comparación entre grupos
sea equilibrada.

## Evaluadores

4 evaluadores independientes (Mishell, Angel, Dayana, Sebas) evaluaron los
66 ítems de forma ciega, sin conocer el origen (humano o LLM) de cada uno,
puntuando en escala Likert 1-5 sobre 5 dimensiones de calidad (ver
`instrumentos/rubrica_evaluacion_requisitos.md`).

## Método de evaluación

La evaluación fue ciega e independiente por evaluador. Los resultados
individuales se promediaron por ítem y se compararon por grupo (humano vs.
LLM) mediante pruebas estadísticas apropiadas según normalidad (t de
Student o U de Mann-Whitney), documentado en
`scripts_analisis/analisis_experimento_llm_humano.py` y reportado en
`resultados/`.

## Nota sobre una justificación anterior descartada

Esta justificación reemplaza una versión anterior basada en revisión
experta individual con rúbrica binaria, descartada en favor de este diseño
comparativo ciego, formalmente pre-registrado en OSF
(https://doi.org/10.17605/OSF.IO/82Q76).
