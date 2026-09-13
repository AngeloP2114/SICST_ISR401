# Datos procesados — SICST, Enfoque 1

## `matriz_trazabilidad_tema_RF.csv`

Pareo temático entre los Requisitos Funcionales (RF) elicitados por el
equipo humano y los generados por el LLM, agrupados por tema común. Cada
fila representa un tema identificado en las transcripciones de entrevista,
con el RF humano y el RF del LLM que lo abordan.

Columnas:

- `tema_id` — identificador del tema (ej. TEMA-01)
- `rf_humano_id` — identificador del RF elicitado por el equipo humano
- `rf_humano_texto` — texto completo del RF humano
- `rf_llm_id` — identificador del RF generado por el LLM
- `rf_llm_texto` — texto completo del RF del LLM
- `tipo` — tipo de pareo (`pareado` cuando ambos RF cubren el mismo tema con
  claridad equivalente, `pareado_debil` cuando el pareo temático es parcial)

Este archivo se usa como referencia de trazabilidad temática entre ambos
conjuntos de RF, complementario al análisis estadístico principal (que
compara los grupos humano/LLM en su conjunto, no ítem por ítem pareado).

