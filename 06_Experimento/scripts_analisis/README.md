# Scripts de análisis — SICST, Enfoque 1

## Script principal

`analisis_experimento_llm_humano.py`

## Entradas

El script utiliza:

- `../datos_crudos/hoja_evaluacion_ciega.csv`
- `../datos_crudos/requisitos_llm.csv`
- `../datos_crudos/evaluaciones_ciegas/Evaluacion_Mishell.xlsx`
- `../datos_crudos/evaluaciones_ciegas/Evaluacion_Angel.xlsx`
- `../datos_crudos/evaluaciones_ciegas/Evaluacion_Dayana.xlsx`
- `../datos_crudos/evaluaciones_ciegas/Evaluacion_sebas.xlsx`
- `../datos_procesados/matriz_trazabilidad_tema_RF.csv`

## Reconstrucción del origen

No se requiere `clave_privada_reconstrucción del origen.csv`.

Después de finalizada la evaluación, el script reconstruye
`ITEM -> origen -> RF real` comparando la hoja ciega con dos fuentes
canónicas:

- para los RF humanos, la matriz de trazabilidad;
- para los RF LLM, el archivo completo `requisitos_llm.csv`.

Se usa el CSV completo del LLM porque la matriz temática solo documenta
correspondencias y puede omitir RF que no participan en ningún pareo. Ese era
el caso de RF-18, que corresponde a ITEM-045.

La ejecución se detiene si no obtiene exactamente 66 ITEM, 33 humanos,
33 LLM, o si existe una coincidencia faltante o ambigua.

## Cálculos

- κ de Fleiss por dimensión sobre los 66 ítems;
- descriptivos por origen;
- 11 pares temáticos estrictos;
- Shapiro-Wilk;
- t apareada o Wilcoxon;
- Holm-Bonferroni;
- diferencia media e IC bootstrap 95 %;
- Cohen's dz e IC bootstrap 95 %;
- 10 000 remuestreos con semilla base 42.

## Ejecución

Con el entorno Python 3.12 activado:

```bash
python 06_Experimento/scripts_analisis/analisis_experimento_llm_humano.py
```

## Salidas

Se generan en `../resultados/`:

- `mapa_origen_items_reconstruido.csv`
- `descriptivos_por_grupo.csv`
- `fleiss_kappa.csv`
- `pares_estrictos_utilizados.csv`
- `prueba_hipotesis_apareada.csv`
- `figura_comparacion_pareada.png`
