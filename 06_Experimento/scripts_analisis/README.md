# Scripts de análisis — SICST, Enfoque 1

## Script principal

`analisis_experimento_llm_humano.py`

## Entradas

El script usa automáticamente:

- `../datos_crudos/hoja_evaluacion_ciega.csv`
- `../datos_crudos/evaluaciones_ciegas/Evaluacion_Mishell.xlsx`
- `../datos_crudos/evaluaciones_ciegas/Evaluacion_Angel.xlsx`
- `../datos_crudos/evaluaciones_ciegas/Evaluacion_Dayana.xlsx`
- `../datos_crudos/evaluaciones_ciegas/Evaluacion_sebas.xlsx`
- `../datos_procesados/matriz_trazabilidad_tema_RF.csv`

## Reconstrucción del origen

No se usa `clave_privada_desciego.csv`.

El script reconstruye `ITEM -> origen -> RF real` después de la evaluación,
comparando el texto de la hoja ciega con los textos canónicos de la matriz.

La ejecución se detiene si:

- no se reconstruyen 66 ITEM;
- no resultan exactamente 33 humanos y 33 LLM;
- algún texto no tiene coincidencia;
- algún texto tiene más de una coincidencia posible.

El mapa derivado se guarda en:

`../resultados/mapa_origen_items_reconstruido.csv`

## Cálculos

- κ de Fleiss por dimensión sobre los 66 ítems.
- descriptivos por origen sobre los 66 ítems.
- construcción de los 11 pares temáticos estrictos.
- Shapiro-Wilk sobre las diferencias por par.
- t apareada o Wilcoxon de rangos con signo.
- Holm-Bonferroni sobre las cinco dimensiones.
- diferencia media humano − LLM.
- IC bootstrap 95 % de la diferencia media.
- Cohen's dz.
- IC bootstrap 95 % de Cohen's dz.
- 10 000 remuestreos bootstrap con semilla base 42.
- figura de comparación pareada.

## Instalación y ejecución

Desde la raíz del repositorio:

```bash
python -m pip install -r 06_Experimento/scripts_analisis/requirements.txt
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
