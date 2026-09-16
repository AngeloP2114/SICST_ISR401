# Instrumentos del experimento SICST — Enfoque 1

## Objetivo

Definir el instrumento empleado para evaluar comparativamente la calidad de
los RF humanos y los RF generados por LLM.

## Rúbrica

Archivo:

`rubrica_evaluacion_requisitos.md`

Cada RF se puntúa de 1 a 5 en cinco dimensiones:

- completitud;
- ausencia de ambigüedad;
- verificabilidad;
- corrección respecto a la fuente;
- consistencia interna.

## Ítems evaluados

Archivo:

`../datos_crudos/hoja_evaluacion_ciega.csv`

Contiene 66 ítems anonimizados:

- 33 RF humanos;
- 33 RF LLM.

La hoja no revela el origen de cada ítem.

## Evaluadores

Las hojas individuales están en:

```text
../datos_crudos/evaluaciones_ciegas/
├── Evaluacion_Mishell.xlsx
├── Evaluacion_Angel.xlsx
├── Evaluacion_Dayana.xlsx
└── Evaluacion_sebas.xlsx
```

Los cuatro evaluadores puntuaron independientemente los 66 ítems.

## Procedimiento

1. Se prepararon los dos conjuntos de 33 RF.
2. Se anonimizaron y mezclaron en un listado común.
3. Los evaluadores recibieron los ítems sin conocer su origen.
4. Cada evaluador puntuó las cinco dimensiones.
5. Finalizada la evaluación, el análisis utiliza una clave privada de
   desciego para recuperar el origen real de cada `item_id`.
6. La clave se pasa al script mediante `--clave`.

## Clave de desciego

La clave no se publica en texto plano.

La copia maestra se conserva en la zona restringida cifrada del proyecto.
El script de análisis **no descifra el contenedor**; únicamente lee una copia
local autorizada de `clave_privada_desciego.csv` proporcionada mediante el
argumento `--clave`.

Esto mantiene separada la evidencia pública de evaluación y la
correspondencia privada necesaria para el análisis.
