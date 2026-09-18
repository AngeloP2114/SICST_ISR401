# Publicación académica — SICST

Esta carpeta reúne los artefactos de publicación académica del proyecto
**Sistema Inteligente de Control y Seguimiento de Terapia Física (SICST)**,
correspondientes al experimento comparativo preregistrado entre Requisitos
Funcionales (RF) elicitados por humanos y RF generados por un LLM.

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

## Preregistro OSF y cronología

El experimento comparativo humano–LLM fue preregistrado en OSF:

- **DOI:** `10.17605/OSF.IO/82Q76`
- **Fecha de registro:** 12/09/2026 en hora de Ecuador continental
- **Copia verificable:** `../06_Experimento/registro_previo/osf_registration.pdf`

Las 18 entrevistas utilizadas como corpus fuente pertenecen a una etapa
anterior del proyecto, destinada a la elicitación y construcción del ERS.

El preregistro **no corresponde a la recolección de esas entrevistas**.
Corresponde específicamente al experimento comparativo humano–LLM.

La marca temporal del preregistro precede a:

- la generación documentada del conjunto de requisitos del LLM;
- la preparación y uso de la evaluación ciega;
- la recolección de las cuatro evaluaciones ciegas utilizadas en el análisis.

Las decisiones u operacionalizaciones estadísticas posteriores al registro se
documentan de forma transparente en:

`../06_Experimento/osf_deviations.pdf`

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
- 4 jueces independientes;
- 5 dimensiones de calidad en escala Likert de 1 a 5;
- 11 pares temáticos estrictos para el análisis pareado.

El análisis reproduce:

- κ de Fleiss por dimensión;
- análisis descriptivos por origen;
- comparación pareada;
- corrección de Holm-Bonferroni;
- intervalos de confianza y tamaños del efecto documentados por el script.

## Resultados reportados

El manuscrito informa que:

- el acuerdo interevaluador fue bajo a nulo según la dimensión;
- κ de Fleiss se ubicó aproximadamente entre `-0.011` y `0.167`;
- ninguna de las cinco dimensiones mostró diferencia estadísticamente
  significativa después de la corrección por comparaciones múltiples;
- la ausencia de significancia no se interpreta como prueba de equivalencia.

## Figuras

Las figuras utilizadas por el manuscrito se encuentran en `figuras/`:

- `figura_comparacion_pareada.png`
- `figura_perfiles.png`
- `figura_saturacion.png`
- `figura_subtemas.png`

La figura comparativa corresponde al resultado experimental principal. Las
demás aportan contexto descriptivo del corpus cualitativo.

## Compilación del manuscrito

Desde `07_Publicacion/` ejecutar:

```bash
pdflatex manuscrito_final.tex
bibtex manuscrito_final
pdflatex manuscrito_final.tex
pdflatex manuscrito_final.tex
```

El archivo resultante es `manuscrito_final.pdf`.

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

La bibliografía utilizada por el manuscrito se mantiene en `references.bib`.

No se establece en este README un número mínimo artificial de referencias; las
entradas deben corresponder a fuentes reales y utilizadas.

## Privacidad

El paquete público no incluye identificadores directos, consentimientos
firmados, firmas, rostros, audios ni videos identificables de participantes.

La evidencia sensible se mantiene separada en
`../02_Evidencias/00_Restringido/`.

## Estado de publicación

El manuscrito corresponde a la línea base de la Entrega Final 2B. El repositorio
no declara aceptación editorial ni publicación en revista científica.

El dataset cuenta con publicación independiente en Zenodo y el experimento
comparativo cuenta con preregistro en OSF.
