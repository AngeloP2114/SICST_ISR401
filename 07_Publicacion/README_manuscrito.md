# Manuscrito final SICST — Enfoque 1 (LLM vs. humano)

## Objetivo

Este manuscrito reporta el componente empírico terminal del proyecto
SICST: una comparación ciega y pareada entre la calidad de
los Requisitos Funcionales (RF) elicitados por el equipo humano y los
generados por un LLM (GPT-5.5-mini), a partir de las mismas 18
transcripciones de entrevista anonimizadas.

**Revista objetivo:** Requirements Engineering — Springer Nature.

## Autores actuales

- Contreras Chávez Kevin Germán
- Zambrano Moya Angelo Paul (ORCID: 0009-0006-0056-8482)

## Archivos

- `manuscrito_final.tex`: fuente LaTeX completa.
- `manuscrito_final.pdf`: PDF compilado desde la fuente (15 páginas).
- `manuscrito_final.bbl`: bibliografía compilada con BibTeX.
- `references.bib`: bibliografía propia del manuscrito (33 entradas).
- `figuras/figura_comparacion_pareada.png`: resultado principal (Figura 1
  del manuscrito).
- `figuras/figura_perfiles.png`, `figura_saturacion.png`,
  `figura_subtemas.png`: evidencia descriptiva del corpus cualitativo de
  origen (contexto, no resultado principal).

## Compilación

Desde esta carpeta ejecutar:

```bash
pdflatex manuscrito_final.tex
bibtex manuscrito_final
pdflatex manuscrito_final.tex
pdflatex manuscrito_final.tex
```

El PDF resultante es `manuscrito_final.pdf`.

## Resumen de la evidencia utilizada

El manuscrito utiliza únicamente resultados respaldados por scripts
reproducibles del repositorio (`06_Experimento/`):

- Protocolo registrado retrospectivamente en OSF (DOI 10.17605/OSF.IO/82Q76), después de la generación del conjunto LLM y de las cuatro evaluaciones ciegas.
- 33 RF elicitados por el equipo humano + 33 RF generados por GPT-5.5-mini
  a partir de las mismas 18 transcripciones anonimizadas (prompt completo
  documentado en `06_Experimento/prompts_llm/`).
- 66 ítems evaluados de forma ciega por 4 evaluadores, en 5
  dimensiones de calidad (escala Likert 1-5).
- Acuerdo entre evaluadores: κ de Fleiss entre -0.013 y 0.167 según la
  dimensión (bajo a nulo).
- Análisis exploratorio pareado (n=11 pares con correspondencia temática
  estricta): prueba t apareada, corrección de Holm-Bonferroni. Ninguna
  dimensión significativa (todos los p ajustados > 0.05).
- No se pudo rechazar H0: sin diferencia de calidad detectable entre RF
  humanos y RF del LLM, en esta muestra pequeña.

## Nota sobre un manuscrito anterior descartado

Una versión anterior de este manuscrito reportaba un estudio distinto
(consolidación de necesidades de campo mediante codificación temática y
trazabilidad, sin componente comparativo LLM vs. humano). Ese estudio no
correspondía a la pregunta de investigación asignada al proyecto SICST
(Enfoque 1, según la Sección 6 de la guía de la asignatura) ni al
protocolo efectivamente registrado en OSF. El corpus cualitativo de esa
versión (18 entrevistas, codificación temática, curva de saturación) se
conserva como evidencia del corpus de origen que alimentó la generación
de RF por ambas vías (humana y LLM), pero ya no es el resultado principal
reportado.

## Ubicación en GitHub

`07_Publicacion/`
