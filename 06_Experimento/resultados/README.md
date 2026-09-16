# Resultados del experimento SICST — Enfoque 1

## Diseño del análisis

El análisis confirmatorio utiliza los **11 pares temáticos estrictos**
identificados por `tipo == "pareado"`.

Esos pares contienen 22 de los 66 ítems evaluados. Los otros 44 ítems se
conservan para trazabilidad y descriptivos, pero no se fuerzan a una
comparación 1 a 1.

Para cada dimensión se reportan:

- Shapiro-Wilk sobre las diferencias;
- t apareada o Wilcoxon;
- valor p crudo;
- valor p ajustado por Holm;
- diferencia media humano − LLM;
- IC bootstrap 95 % de la diferencia;
- Cohen's dz;
- IC bootstrap 95 % de Cohen's dz.

Bootstrap: 10 000 remuestreos con semilla base 42.

## Archivos

- `mapa_origen_items_reconstruido.csv`  
  Correspondencia post-evaluación reconstruida automáticamente entre
  `ITEM`, origen real y RF real.

- `fleiss_kappa.csv`  
  Acuerdo entre los cuatro evaluadores sobre los 66 ítems.

- `descriptivos_por_grupo.csv`  
  Estadísticos descriptivos humano/LLM sobre los 66 ítems.

- `pares_estrictos_utilizados.csv`  
  Los 11 pares temáticos utilizados en el análisis confirmatorio.

- `prueba_hipotesis_apareada.csv`  
  Resultados de normalidad, contraste, Holm, diferencia media, IC 95 %,
  Cohen's dz e IC 95 % de Cohen's dz.

- `figura_comparacion_pareada.png`  
  Comparación visual de los 11 pares.

## Reproducción

Desde la raíz del repositorio:

```bash
python -m pip install -r 06_Experimento/scripts_analisis/requirements.txt
python 06_Experimento/scripts_analisis/analisis_experimento_llm_humano.py
```

Una ejecución válida debe reconstruir:

- 66 ITEM;
- 33 humanos;
- 33 LLM;
- 11 pares estrictos.

Después de regenerar los archivos, las cifras deben compararse con el ERS y
el manuscrito antes del cierre final.
