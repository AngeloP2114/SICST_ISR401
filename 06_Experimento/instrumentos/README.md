# Instrumentos del experimento SICST — Enfoque 1

## Rúbrica

Archivo:

`rubrica_evaluacion_requisitos.md`

Cada requisito se puntúa de 1 a 5 en cinco dimensiones:

- completitud;
- ausencia de ambigüedad;
- verificabilidad;
- corrección respecto a la fuente;
- consistencia interna.

## Evaluación ciega

La hoja:

`../datos_crudos/hoja_evaluacion_ciega.csv`

contiene 66 ítems anonimizados con identificadores `ITEM-001` a `ITEM-066`.
La hoja no incluye una columna que revele el origen humano/LLM.

Las evaluaciones individuales están en:

```text
../datos_crudos/evaluaciones_ciegas/
├── Evaluacion_Mishell.xlsx
├── Evaluacion_Angel.xlsx
├── Evaluacion_Dayana.xlsx
└── Evaluacion_sebas.xlsx
```

Los cuatro evaluadores calificaron los mismos 66 ítems.

## Desciego para el análisis

Una vez finalizada la evaluación, el análisis reconstruye la correspondencia
de cada `ITEM` con su RF real mediante coincidencia exacta normalizada del
texto entre:

- `../datos_crudos/hoja_evaluacion_ciega.csv`
- `../datos_procesados/matriz_trazabilidad_tema_RF.csv`

No se requiere ni se afirma la existencia de una clave privada externa.

El script exige que la reconstrucción produzca exactamente:

- 66 ítems;
- 33 RF humanos;
- 33 RF LLM;
- cero coincidencias faltantes;
- cero coincidencias ambiguas.

Esto preserva el cegado durante la evaluación y permite reproducir el
desciego después de finalizada.
