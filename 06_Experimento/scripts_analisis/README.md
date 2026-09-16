# Scripts de análisis — SICST, Enfoque 1

## Script principal

`analisis_experimento_llm_humano.py`

El script implementa el análisis reproducible del experimento humano vs. LLM.

## Entradas públicas

El script resuelve automáticamente estas rutas a partir de su propia
ubicación:

- `../datos_crudos/evaluaciones_ciegas/Evaluacion_Mishell.xlsx`
- `../datos_crudos/evaluaciones_ciegas/Evaluacion_Angel.xlsx`
- `../datos_crudos/evaluaciones_ciegas/Evaluacion_Dayana.xlsx`
- `../datos_crudos/evaluaciones_ciegas/Evaluacion_sebas.xlsx`
- `../datos_procesados/matriz_trazabilidad_tema_RF.csv`

## Entrada restringida

También necesita:

`clave_privada_desciego.csv`

La clave **no se publica** en esta carpeta. Debe extraerse localmente de la
zona restringida cifrada por una persona autorizada y pasarse mediante
`--clave`.

El script no descifra automáticamente el contenedor restringido.

## Cálculos

- κ de Fleiss por dimensión sobre los 66 ítems.
- descriptivos humano/LLM sobre los 66 ítems.
- construcción de los 11 pares estrictos.
- Shapiro-Wilk sobre las diferencias por par.
- t apareada o Wilcoxon de rangos con signo.
- Holm-Bonferroni sobre las cinco dimensiones.
- diferencia media humano − LLM.
- IC bootstrap 95 % de la diferencia media.
- Cohen's dz.
- IC bootstrap 95 % de Cohen's dz.
- 10 000 remuestreos bootstrap con semilla 42.
- figura de comparación pareada.

## Instalación

Desde la raíz del repositorio:

```bash
python -m pip install -r 06_Experimento/scripts_analisis/requirements.txt
```

## Ejecución

```bash
python 06_Experimento/scripts_analisis/analisis_experimento_llm_humano.py \
  --clave /ruta/local/clave_privada_desciego.csv
```

## Salidas

El script escribe automáticamente en `06_Experimento/resultados/`:

- `descriptivos_por_grupo.csv`
- `fleiss_kappa.csv`
- `prueba_hipotesis_apareada.csv`
- `pares_estrictos_utilizados.csv`
- `figura_comparacion_pareada.png`

## Comprobación mínima

Una ejecución correcta debe informar:

- 4 evaluadores cargados;
- 11 pares estrictos;
- creación de las cinco salidas;
- ausencia de errores por rutas o columnas faltantes.
