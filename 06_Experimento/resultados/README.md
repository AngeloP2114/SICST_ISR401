# Resultados del experimento SICST — Enfoque 1

Los resultados de esta carpeta son generados por:

`../scripts_analisis/analisis_experimento_llm_humano.py`

## Diseño del análisis

El análisis principal es **apareado**.

Se utilizan los **11 pares temáticos estrictos** identificados por
`tipo == "pareado"` en
`../datos_procesados/matriz_trazabilidad_tema_RF.csv`.

Esos 11 pares contienen 22 de los 66 ítems evaluados. Los **44 ítems
restantes** se conservan para trazabilidad y descriptivos, pero no se
incluyen en el contraste confirmatorio 1 a 1.

Para cada dimensión:

- Shapiro-Wilk sobre las diferencias por par.
- t apareada si no se rechaza normalidad.
- Wilcoxon de rangos con signo en caso contrario.
- corrección Holm-Bonferroni sobre las cinco dimensiones.
- diferencia media humano − LLM.
- IC bootstrap 95 % de la diferencia media.
- Cohen's dz.
- IC bootstrap 95 % de Cohen's dz.
- 10 000 remuestreos bootstrap, semilla 42.

## Archivos

- `fleiss_kappa.csv`  
  κ de Fleiss por dimensión sobre los 66 ítems.

- `descriptivos_por_grupo.csv`  
  Estadísticos descriptivos humano/LLM sobre los 66 ítems.

- `pares_estrictos_utilizados.csv`  
  Los 11 pares usados en el análisis confirmatorio.

- `prueba_hipotesis_apareada.csv`  
  Incluye prueba aplicada, estadístico, p crudo, p ajustado por Holm,
  diferencia media, IC 95 %, Cohen's dz e IC 95 % de Cohen's dz.

- `figura_comparacion_pareada.png`  
  Comparación visual del puntaje global de los 11 pares.

## Hallazgo principal documentado hasta la ejecución actual

El análisis apareado no mostró diferencias estadísticamente significativas
tras la corrección de Holm-Bonferroni en las cinco dimensiones.

El acuerdo entre evaluadores fue bajo en varias dimensiones y debe
mantenerse reportado como limitación metodológica.

## Reproducibilidad

Desde la raíz del repositorio:

```bash
python -m pip install -r 06_Experimento/scripts_analisis/requirements.txt

python 06_Experimento/scripts_analisis/analisis_experimento_llm_humano.py \
  --clave /ruta/local/clave_privada_desciego.csv
```

Después de ejecutar, estos archivos deben compararse con las cifras del ERS
y del manuscrito. Cualquier discrepancia debe corregirse en el documento que
haya quedado desactualizado.
