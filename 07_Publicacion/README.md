# Publicación académica — SICST

Esta carpeta reúne los artefactos de publicación académica del proyecto
**Sistema Inteligente de Control y Seguimiento de Terapia Física (SICST)**,
correspondientes al estudio comparativo entre Requisitos Funcionales (RF)
elicitados mediante un proceso humano y RF generados por un LLM.

El protocolo del experimento fue registrado retrospectivamente en OSF. Por
tanto, el estudio no se presenta como un experimento confirmatorio
prerregistrado y sus comparaciones inferenciales se interpretan como
exploratorias.

## Autores actuales

- Contreras Chávez Kevin Germán
- Zambrano Moya Angelo Paul (ORCID: 0009-0006-0056-8482)

## Manuscrito científico

El manuscrito vigente del proyecto se encuentra en:

- `manuscrito_final.pdf`
- `manuscrito_final.tex`
- `manuscrito_final.bbl`
- `references.bib`

**Título:** *An Empirical Comparison of Human-Elicited and LLM-Generated
Functional Requirements in a Physical Therapy Follow-Up System: A
Paired-Analyst Study in Ecuador*

**Revista objetivo:** Requirements Engineering (Springer Nature).

El análisis de revistas objetivo se encuentra en `analisis_revistas.md`.

La versión actual del manuscrito incorpora las correcciones realizadas después
de la revisión del 18/09/2026, entre ellas:

- corrección de la cronología real del experimento;
- declaración explícita del carácter retrospectivo del registro OSF;
- tratamiento de los análisis inferenciales como exploratorios;
- ampliación de las amenazas a la validez;
- documentación de las limitaciones de procedencia de las evaluaciones ciegas;
- ampliación del soporte bibliográfico.

El manuscrito cita actualmente 20 referencias distintas incluidas en
`references.bib`.

## Registro OSF y cronología

El protocolo del experimento comparativo humano–LLM fue registrado en OSF:

- **DOI:** `10.17605/OSF.IO/82Q76`
- **Fecha y hora UTC:** `2026-09-13T00:50:38Z`
- **Fecha y hora Ecuador continental:** `2026-09-12 19:50:38`
- **Copia verificable:** `../06_Experimento/registro_previo/osf_registration.pdf`

La evidencia del repositorio permite reconstruir la siguiente cronología:

1. realización de las entrevistas de campo y elicitación de requisitos;
2. generación del conjunto de requisitos mediante el LLM;
3. realización de las cuatro evaluaciones ciegas;
4. registro del protocolo experimental en OSF;
5. análisis estadístico y documentación posterior.

Por tanto, cuando se realizó el registro OSF ya existían:

- las entrevistas utilizadas como corpus fuente;
- el conjunto de requisitos generado mediante GPT-5.5-mini;
- las cuatro hojas de evaluación ciega utilizadas posteriormente en el análisis.

El registro OSF se documenta en este repositorio como un
**registro retrospectivo del protocolo** y no como una prerregistración
confirmatoria previa a la generación de los datos experimentales.

La ficha documental del prompt LLM también fue corregida para reflejar esta
cronología. La hora exacta de generación del conjunto LLM no fue preservada,
pero los metadatos de las hojas de evaluación ciega permiten establecer que el
conjunto ya existía antes de aproximadamente las 13:11 del 12/09/2026.

Las decisiones y operacionalizaciones estadísticas posteriores al registro se
documentan de forma transparente en:

`../06_Experimento/osf_deviations.pdf`

Debido a esta cronología, los resultados inferenciales del estudio se
interpretan como **exploratorios y no confirmatorios**.

## Diseño del estudio

La pregunta de investigación es:

> ¿Difieren en calidad los requisitos funcionales elicitados por un proceso
> humano de los generados por un LLM cuando ambos parten de las mismas
> transcripciones anonimizadas?

El estudio utiliza:

- 18 transcripciones anonimizadas como corpus fuente común;
- 33 RF elicitados por el equipo humano;
- 33 RF generados por GPT-5.5-mini;
- 66 ítems evaluados de forma ciega;
- 4 evaluadores ciegos al origen de los requisitos;
- 5 dimensiones de calidad en escala Likert de 1 a 5;
- 11 pares temáticos estrictos para el análisis pareado.

Las cuatro evaluaciones fueron realizadas secuencialmente durante una misma
sesión utilizando el mismo computador. Cada evaluador completó su propia hoja.
El organizador verificó únicamente que los campos de evaluación estuvieran
completos y guardó cada archivo antes de continuar con el siguiente evaluador.

Este procedimiento explica que los cuatro archivos presenten el mismo editor
final en sus metadatos. Sin embargo, esos metadatos por sí solos no permiten
demostrar quién introdujo cada puntuación individual. El uso de una misma
sesión y un mismo equipo se reconoce como una limitación de procedencia de la
evidencia.

El análisis reproduce:

- κ de Fleiss por dimensión;
- análisis descriptivos por origen;
- comparación pareada;
- corrección de Holm-Bonferroni;
- intervalos de confianza;
- resultados reproducibles mediante el script versionado.

## Resultados reportados

El manuscrito informa que:

- el acuerdo interevaluador fue bajo a prácticamente nulo según la dimensión;
- κ de Fleiss se ubicó entre aproximadamente `-0.013` y `0.167`;
- ninguna de las cinco dimensiones mostró diferencia estadísticamente
  significativa después de la corrección por comparaciones múltiples;
- la ausencia de significancia no se interpreta como prueba de equivalencia;
- los resultados se consideran exploratorios debido al tamaño de muestra,
  la baja concordancia entre evaluadores y la cronología retrospectiva del
  registro OSF.

## Figuras

Las figuras utilizadas por el manuscrito se encuentran en `figuras/`:

- `figura_comparacion_pareada.png`
- `figura_perfiles.png`
- `figura_saturacion.png`
- `figura_subtemas.png`

La figura comparativa corresponde al resultado experimental principal. Las
demás aportan contexto descriptivo del corpus cualitativo.

## Compilación del manuscrito

La compilación recomendada desde `07_Publicacion/` es:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error manuscrito_final.tex
```

También puede realizarse manualmente mediante:

```bash
pdflatex manuscrito_final.tex
bibtex manuscrito_final
pdflatex manuscrito_final.tex
pdflatex manuscrito_final.tex
```

El archivo resultante es:

`manuscrito_final.pdf`

La versión corregida fue compilada nuevamente el 18/09/2026 sin citas
indefinidas ni errores fatales de LaTeX.

## Fuentes reproducibles del experimento

Los artefactos principales se encuentran en `../06_Experimento/`:

- `prompts_llm/prompt_generacion_RF_llm.md`
- `datos_crudos/`
- `datos_procesados/`
- `datos_procesados/matriz_trazabilidad_tema_RF.csv`
- `scripts_analisis/analisis_experimento_llm_humano.py`
- `resultados/`
- `registro_previo/`
- `osf_deviations.pdf`

La reproducción del experimento se ejecuta desde la raíz con:

```bash
python 06_Experimento/scripts_analisis/analisis_experimento_llm_humano.py
```

## Reproducibilidad de los datos generales

La cadena reproducible del cuestionario general se ejecuta desde la raíz con:

```bash
python 07_Datos/scripts/orquestar.py
```

## Dataset publicado

- **DOI:** `10.5281/zenodo.22315298`
- **Versión publicada:** 1.0
- **Fecha de publicación:** 05/09/2026
- **Acceso:** Público / Open

## Bibliografía

La bibliografía utilizada por el manuscrito se mantiene en:

`references.bib`

La versión actual del manuscrito utiliza 20 referencias distintas relacionadas
con ingeniería de requisitos, calidad de requisitos, estudios empíricos,
telerehabilitación, confiabilidad interevaluador, investigación cualitativa,
privacidad y uso de inteligencia artificial.

Las referencias incluidas deben corresponder a fuentes reales utilizadas en el
texto; no se incluyen entradas únicamente para aumentar artificialmente el
número de referencias.

## Privacidad

El paquete público no incluye identificadores directos, consentimientos
firmados, firmas, rostros, audios ni videos identificables de participantes.

La evidencia sensible se mantiene separada en:

`../02_Evidencias/00_Restringido/`

## Interpretación metodológica

La evidencia disponible permite reproducir el análisis y verificar los
resultados reportados, pero existen limitaciones que deben conservarse
explícitamente:

- el registro OSF ocurrió después de la generación LLM y de las evaluaciones
  ciegas;
- la hora exacta de generación LLM no fue preservada;
- las cuatro evaluaciones se realizaron durante una misma sesión y con un mismo
  computador;
- los metadatos de los archivos no demuestran por sí solos la autoría de cada
  puntuación;
- los evaluadores no eran especialistas profesionales en ingeniería de
  requisitos;
- únicamente 11 pares cumplieron el criterio estricto de correspondencia
  temática;
- el bajo acuerdo interevaluador introduce incertidumbre adicional;
- las pruebas inferenciales deben interpretarse como exploratorias.

Estas limitaciones se mantienen visibles para evitar presentar el estudio con
un nivel de control experimental superior al que realmente tuvo.

## Estado de publicación

El manuscrito corresponde a la versión corregida posterior a la evaluación del
18/09/2026.

El repositorio no declara aceptación editorial ni publicación del artículo en
una revista científica.

El dataset cuenta con publicación independiente en Zenodo.

El protocolo experimental cuenta con un registro OSF realizado el
12/09/2026 a las 19:50:38 hora de Ecuador continental. Debido a que la
generación LLM y las evaluaciones ciegas ocurrieron antes de ese registro, este
repositorio lo describe como un **registro retrospectivo del protocolo** y no
como una prerregistración confirmatoria.
