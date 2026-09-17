# Resultados del experimento SICST — Enfoque 1

## Diseño del análisis

El análisis confirmatorio utiliza los **11 pares temáticos estrictos**
identificados por `tipo == "pareado"`.

Esos pares contienen 22 de los 66 ítems evaluados. Los otros 44 ítems se
conservan para trazabilidad y análisis descriptivos, pero no se fuerzan a una
comparación 1 a 1.

Para cada dimensión se reportan:

- Shapiro-Wilk sobre las diferencias entre cada par;
- t de Student apareada o Wilcoxon de rangos con signo, según corresponda;
- valor p crudo;
- valor p ajustado mediante Holm-Bonferroni;
- diferencia media humano − LLM;
- intervalo de confianza bootstrap del 95 % de la diferencia;
- Cohen's dz como tamaño del efecto para datos apareados;
- intervalo de confianza bootstrap del 95 % de Cohen's dz.

El procedimiento bootstrap utiliza **10 000 remuestreos** con semilla base
**42** para favorecer la reproducibilidad.

El índice global se reporta como un resumen complementario. La corrección
Holm-Bonferroni se aplica a las cinco dimensiones principales del estudio.

## Archivos generados

### `mapa_origen_items_reconstruido.csv`

Contiene la correspondencia post-evaluación entre:

`ITEM-xxx → origen real → RF real`

La correspondencia se reconstruye automáticamente utilizando la matriz de
trazabilidad para los requisitos humanos y `requisitos_llm.csv` para el
conjunto completo de requisitos generados por LLM.

**Nota sobre el cegamiento:** los cuatro evaluadores calificaron únicamente
la hoja ciega (`hoja_evaluacion_ciega.csv`), que contenía identificadores
`ITEM-xxx` y el texto de cada requisito. La hoja entregada a los evaluadores
no incluía ninguna columna que indicara si el requisito había sido obtenido
mediante el proceso humano o generado por el LLM.

Las columnas correspondientes a completitud, ausencia de ambigüedad,
verificabilidad, corrección respecto a la fuente y consistencia interna se
entregaron vacías para que cada evaluador registrara independientemente sus
puntuaciones de 1 a 5.

El archivo `mapa_origen_items_reconstruido.csv` se generó **después de
finalizadas las cuatro evaluaciones**, exclusivamente para realizar el
análisis estadístico y facilitar su reproducibilidad. Por tanto, esta
correspondencia no estuvo disponible para los evaluadores antes ni durante
su calificación.

### `fleiss_kappa.csv`

Contiene el coeficiente κ de Fleiss por dimensión, calculado sobre los
66 ítems y los cuatro evaluadores.

Este análisis permite describir el nivel de acuerdo existente entre los
evaluadores y se mantiene separado del contraste estadístico de los
11 pares temáticos.

### `descriptivos_por_grupo.csv`

Contiene los estadísticos descriptivos correspondientes a los grupos humano
y LLM sobre el conjunto completo de 66 requisitos evaluados.

Incluye, entre otros:

- número de observaciones;
- media;
- mediana;
- desviación estándar;
- mínimo;
- máximo;
- rango intercuartílico.

### `pares_estrictos_utilizados.csv`

Contiene los **11 pares temáticos estrictos** utilizados en el análisis
confirmatorio.

Cada fila relaciona un requisito humano con un requisito LLM que aborda un
tema suficientemente equivalente para permitir una comparación apareada.

Los requisitos clasificados como `pareado_parcial`, `pareado_debil`,
`solo_humano` o `solo_llm` no se incluyen en este contraste principal.

### `prueba_hipotesis_apareada.csv`

Contiene los resultados completos del análisis inferencial.

Para cada dimensión incluye:

- número de pares;
- prueba estadística aplicada;
- valor p de Shapiro-Wilk sobre las diferencias;
- resultado de normalidad;
- estadístico de contraste;
- valor p crudo;
- diferencia media humano − LLM;
- IC bootstrap del 95 % de la diferencia media;
- Cohen's dz;
- IC bootstrap del 95 % de Cohen's dz;
- número de remuestreos bootstrap;
- semilla utilizada;
- valor p ajustado mediante Holm-Bonferroni;
- decisión de significancia con α = 0.05.

### `figura_comparacion_pareada.png`

Representa gráficamente los puntajes globales de los **11 pares temáticos
estrictos**, mostrando la relación entre el requisito humano y el requisito
LLM correspondiente.

## Resultado general de la ejecución actual

En la ejecución reproducible actual se obtuvieron:

- **66 ITEM reconstruidos**;
- **33 requisitos humanos**;
- **33 requisitos LLM**;
- **11 pares temáticos estrictos**.

En las cinco dimensiones analizadas no se observaron diferencias
estadísticamente significativas después de aplicar la corrección
Holm-Bonferroni.

La ausencia de significancia estadística no debe interpretarse como prueba de
equivalencia entre ambos procedimientos. Los resultados deben considerarse
junto con los intervalos de confianza, los tamaños del efecto, el tamaño
efectivo de 11 pares y el acuerdo entre evaluadores.

## Reproducción

Para reproducir el análisis se recomienda utilizar **Python 3.12**.

Desde la raíz del repositorio:

```bash
python3.12 -m venv .venv-sicst
source .venv-sicst/bin/activate
python -m pip install --upgrade pip
python -m pip install -r 06_Experimento/scripts_analisis/requirements.txt
python 06_Experimento/scripts_analisis/analisis_experimento_llm_humano.py
