# Justificación de la muestra del experimento — Enfoque 1

## Corpus disponible

El estudio compara dos conjuntos de requisitos funcionales derivados del
mismo dominio y del mismo corpus fuente anonimizado:

- **33 RF humanos**, obtenidos mediante el proceso normal de ingeniería de
  requisitos del SICST.
- **33 RF generados por GPT-5.5-mini**, usando las mismas 18 transcripciones
  anonimizadas como corpus fuente.

Los 66 ítems se utilizaron en la evaluación ciega y en los descriptivos
generales.

## Evaluadores

Cuatro evaluadores (Mishell, Angel, Dayana y Sebas) puntuaron
los 66 ítems en una escala Likert de 1 a 5 sobre cinco dimensiones:

- completitud;
- ausencia de ambigüedad;
- verificabilidad;
- corrección respecto a la fuente;
- consistencia interna.

## Unidad del análisis exploratorio

El análisis exploratorio no trata los 33 RF humanos y los 33 RF LLM como
dos muestras independientes.

La matriz de trazabilidad temática identifica **11 pares estrictos**
(`tipo == "pareado"`). Cada par contiene un RF humano y un RF LLM que
abordan el mismo tema y constituye una unidad de comparación.

Por tanto, el tamaño efectivo del contraste exploratorio es **n = 11 pares**.

Los demás ítems se conservan para trazabilidad y descriptivos, pero no se
fuerzan artificialmente a una correspondencia 1 a 1.

## Método de comparación

Para cada una de las cinco dimensiones:

1. se calcula la diferencia humano − LLM dentro de cada uno de los 11 pares;
2. se prueba la normalidad de esas diferencias mediante Shapiro-Wilk;
3. si no se rechaza normalidad, se utiliza t de Student apareada;
4. en caso contrario, se utiliza Wilcoxon de rangos con signo;
5. los cinco valores p de las dimensiones se ajustan mediante
   Holm-Bonferroni;
6. se reporta la diferencia media humano − LLM con IC bootstrap del 95 %;
7. se reporta Cohen's dz como tamaño del efecto pareado, también con IC
   bootstrap del 95 %.

El bootstrap utiliza **10 000 remuestreos** y **semilla 42**.

El índice global se reporta como resumen complementario y no se incluye como
una sexta comparación dentro del ajuste Holm de las cinco dimensiones.

## Acuerdo entre evaluadores

El κ de Fleiss se calcula separadamente sobre los **66 ítems completos** y
los cuatro evaluadores. Este cálculo no depende del pareo temático.

## Limitación

Con 11 pares, la potencia estadística es limitada. Por ello, los resultados
deben interpretarse junto con los intervalos de confianza, el tamaño del
efecto y el acuerdo interevaluador, sin convertir la ausencia de
significancia estadística en evidencia de equivalencia.
