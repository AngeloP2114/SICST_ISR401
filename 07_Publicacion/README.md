# Publicación académica — SICST

Esta carpeta reúne los artefactos de publicación académica del proyecto
**Sistema Inteligente de Control y Seguimiento de Terapia Física (SICST)**,
correspondientes al Enfoque 1: comparación empírica de calidad de
Requisitos Funcionales (RF) elicitados por humanos vs. generados por un
LLM.

## Autores actuales

- Contreras Chávez Kevin Germán
- Zambrano Moya Angelo Paul (ORCID: 0009-0006-0056-8482)

## Manuscrito científico

El manuscrito final del proyecto se encuentra en:

- `manuscrito_final.pdf` (8 páginas, compilado)
- `manuscrito_final.tex` (fuente LaTeX completa)
- `manuscrito_final.bbl` (bibliografía compilada)
- `references.bib` (33 entradas, en progreso hacia el mínimo de 40)

**Título:** *An Empirical Comparison of Human-Elicited and LLM-Generated
Functional Requirements in a Physical Therapy Follow-Up System: A
Paired-Analyst Study in Ecuador*

**Revista objetivo:** Requirements Engineering (Springer Nature). El
análisis completo de revistas objetivo se encuentra en `analisis_revistas.md`.

## Diseño del estudio reportado

- **Pregunta de investigación:** ¿Difieren en calidad los RF elicitados
  por un proceso humano de los generados por un LLM, cuando ambos parten
  de las mismas transcripciones anonimizadas?
- **Registro previo:** OSF, DOI [10.17605/OSF.IO/82Q76](https://doi.org/10.17605/OSF.IO/82Q76)
  (2026-09-12, antes de generar los datos).
- **Diseño:** comparativo no experimental, ciego, 66 ítems (33 humanos +
  33 LLM) evaluados por 4 jueces independientes en 5 dimensiones (escala
  Likert 1-5).
- **Análisis confirmatorio:** 11 pares con correspondencia temática
  estricta, prueba t apareada / Wilcoxon con corrección de
  Holm-Bonferroni.
- **Hallazgo principal:** acuerdo inter-evaluador bajo (κ de Fleiss entre
  -0.011 y 0.167); ninguna dimensión mostró diferencia estadísticamente
  significativa (todos los p ajustados > 0.05).

## Figuras

Las figuras utilizadas por el manuscrito se encuentran en `figuras/`:

- `figura_comparacion_pareada.png` — comparación pareada por tema (Figura 1
  del manuscrito, resultado principal).
- `figura_perfiles.png`, `figura_saturacion.png`, `figura_subtemas.png` —
  evidencia descriptiva del corpus cualitativo de 18 entrevistas que
  alimentó tanto la elicitación humana como la generación por LLM (no son
  el resultado principal, sirven de contexto del dominio).

Las rutas relativas de las figuras deben mantenerse sin cambios para
permitir la compilación correcta del manuscrito.

## Compilación del manuscrito LaTeX

Desde esta carpeta ejecutar:

```bash
pdflatex manuscrito_final.tex
bibtex manuscrito_final
pdflatex manuscrito_final.tex
pdflatex manuscrito_final.tex
```

El PDF resultante es `manuscrito_final.pdf`.

### Paquetes requeridos

`graphicx`, `booktabs`, `array`, `tabularx`, `longtable`, `enumitem`,
`natbib`, `hyperref`, `url`, `caption`, `float`, `setspace`, `xcolor`,
`amsmath`, `amssymb`, `titlesec`, `microtype` (con `expansion=false` si el
motor LaTeX no tiene fuentes escalables disponibles).

### Archivos mínimos necesarios para compilar

```text
07_Publicacion/
├── manuscrito_final.tex
├── references.bib
└── figuras/
    ├── figura_comparacion_pareada.png
    ├── figura_perfiles.png
    ├── figura_saturacion.png
    └── figura_subtemas.png
```

## Evidencia utilizada por el manuscrito

Todos los datos, tablas y figuras citados en el manuscrito provienen de
scripts versionados y reproducibles en `06_Experimento/`:

- Prompt exacto del LLM y confirmación del modelo:
  `06_Experimento/prompts_llm/prompt_generacion_RF_llm.md`
- Datos crudos (RF del LLM, hoja de evaluación ciega, 4 evaluaciones):
  `06_Experimento/datos_crudos/`
- Matriz de pareo temático: `06_Experimento/datos_procesados/matriz_trazabilidad_tema_RF.csv`
- Script de análisis reproducible: `06_Experimento/scripts_analisis/analisis_experimento_llm_humano.py`
- Resultados (Tablas 1-2 y Figura 1 del manuscrito): `06_Experimento/resultados/`

Ejecutar el script reproduce exactamente las cifras citadas en el
manuscrito, a partir de los datos crudos.

## Reproducibilidad de los datos generales del proyecto

La fuente reproducible del cuestionario general del proyecto (no del
experimento comparativo) se encuentra en `../07_Datos/`:

```bash
python 07_Datos/scripts/orquestar.py
```

## Dataset publicado

El paquete reproducible del proyecto SICST está publicado en Zenodo.

- **DOI:** `10.5281/zenodo.22315298`
- **URL DOI:** `https://doi.org/10.5281/zenodo.22315298`
- **Versión:** 1.0
- **Acceso:** Público / Open

Los metadatos y el contenido del depósito se encuentran en `dataset_zenodo/`.

## Alcance del manuscrito

El manuscrito reporta un estudio empírico de pequeña muestra (n=11 pares),
preregistrado, ciego, sobre calidad de requisitos funcionales. No afirma
que los LLM igualen a los analistas humanos en general, ni en otros
dominios, idiomas o modelos — las conclusiones se restringen explícitamente
al alcance de este estudio.

## Privacidad y protección de datos

El paquete público de publicación no contiene identificadores directos,
consentimientos firmados, firmas, rostros, audios o videos identificables
de participantes. La clave que revela el origen real (humano/LLM) de cada
ítem evaluado se mantiene cifrada en `02_Evidencias/00_Restringido/`.

## Relación con el repositorio

- ERS/SRS: `../01_ERS/`
- Evidencias: `../02_Evidencias/`
- Trazabilidad: `../04_Trazabilidad/`
- MVP: `../05_MVP/`
- Experimento (Enfoque 1): `../06_Experimento/`
- Datos reproducibles generales: `../07_Datos/`

## Estado de publicación

El manuscrito corresponde a la línea base vigente de la Entrega Final 2B.
Se encuentra preparado como artefacto académico de publicación; el
repositorio no declara aceptación editorial ni publicación en una revista
científica. El dataset reproducible cuenta con publicación independiente
en Zenodo (DOI persistente) y el protocolo con registro previo en OSF
(DOI persistente).
