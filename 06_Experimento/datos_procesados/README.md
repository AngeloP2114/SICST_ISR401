# Datos procesados — SICST, Enfoque 1

## `matriz_trazabilidad_tema_RF.csv`

Este archivo documenta la correspondencia temática entre RF humanos y RF
generados por LLM.

Columnas principales:

- `tema_id`: identificador del tema.
- `rf_humano_id`: identificador del RF humano.
- `rf_humano_texto`: texto del RF humano.
- `rf_llm_id`: identificador del RF LLM.
- `rf_llm_texto`: texto del RF LLM.
- `tipo`: clasificación de la correspondencia temática.

Valores observados de `tipo`:

- `pareado` — 11 filas.
- `pareado_parcial` — 10 filas.
- `pareado_debil` — 6 filas.
- `solo_humano` — 12 filas.
- `solo_llm` — 5 filas.

Solo las **11 filas `tipo == "pareado"`** entran al análisis confirmatorio
apareado. Esas filas representan **22 ítems: 11 humanos + 11 LLM**.

De los 66 ítems evaluados, los **44 ítems restantes** se mantienen para
trazabilidad y descriptivos, pero no entran en el contraste confirmatorio
1 a 1.

No se reetiquetan pares parciales o débiles como estrictos con el objetivo
de aumentar artificialmente el tamaño de muestra.
