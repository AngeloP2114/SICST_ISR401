# SICST — Sistema Inteligente de Control y Seguimiento de Terapia Física

Repositorio de la **Entrega Final 2B** del Proyecto Integrador de la asignatura **Ingeniería de Requerimientos — ISR-401**.

**Universidad:** Universidad Técnica Estatal de Quevedo
**Carrera:** Ingeniería de Software
**Asignatura:** Ingeniería de Requerimientos ISR-401
**Periodo académico:** 2026–2027
**Versión documental:** 2.0 — Entrega Final 2B

## Integrantes

- Contreras Chávez Kevin Germán
- Zambrano Moya Angelo Paul (ORCID: [0009-0006-0056-8482](https://orcid.org/0009-0006-0056-8482))

**Nota sobre integración del equipo:** el repositorio conserva en su historial commits de un tercer colaborador, **Morán Pilaguano Frixon Fernando** (usuario `FrixonMP`), quien dejó de formar parte del equipo el **06/09/2026**. Su aporte histórico se mantiene en el historial de Git y en `.mailmap` por transparencia y trazabilidad, pero no figura como autor en la entrega final ni en `CITATION.cff`, en concordancia con la composición del equipo al momento del cierre.

---

## Identificadores persistentes

| Recurso | Identificador |
|---|---|
| Registro previo del experimento (OSF) | [10.17605/OSF.IO/82Q76](https://doi.org/10.17605/OSF.IO/82Q76) |
| Dataset reproducible (Zenodo, v1.0) | [10.5281/zenodo.22315298](https://doi.org/10.5281/zenodo.22315298) |
| Repositorio (GitHub) | https://github.com/gleiston-guerrero/SICST_ISR401 |

---

# Descripción del proyecto

El **Sistema Inteligente de Control y Seguimiento de Terapia Física (SICST)** es un prototipo académico orientado a apoyar el seguimiento de pacientes que realizan parte de sus rutinas terapéuticas fuera del centro de rehabilitación.

El proyecto integra actividades de:

- ingeniería de requisitos;
- elicitación y validación;
- evidencia de trabajo de campo;
- modelado UML;
- trazabilidad;
- producto mínimo viable;
- experimentación empírica preregistrada (Enfoque 1: RF humano vs. LLM);
- preparación de publicación académica;
- privacidad y gestión ética;
- defensa final.

SICST se plantea como una herramienta de apoyo y no sustituye la valoración, diagnóstico ni decisión del profesional de salud.

---

# Línea base vigente

La línea base vigente del repositorio corresponde a:

**Entrega Final 2B — versión 2.0**

La carpeta `PE5_Informe_Final/` se conserva únicamente como **antecedente histórico** correspondiente a la Práctica Experimental 5. Los documentos, simulaciones, métricas y materiales almacenados en PE5 no sustituyen los artefactos finales requeridos para la Entrega Final 2B.

---

# Estructura principal

```
SICST_ISR401/
│
├── 01_ERS/
├── 02_Evidencias/
├── 03_Modelado/
├── 04_Trazabilidad/
├── 05_MVP/
├── 06_Experimento/
├── 07_Datos/
├── 07_Publicacion/
├── 08_Etica/
├── 09_Defensa/
├── 10_Autoria/
├── PE5_Informe_Final/
│
├── CHANGELOG.md
├── CITATION.cff
├── LICENSE
├── README.md
├── checksums.sha256
├── fair_assessment.pdf
├── .mailmap
├── .gitignore
└── .gitattributes
```

---

# 1. ERS / SRS — Entrega Final 2B

La especificación vigente del proyecto se encuentra en:

```
01_ERS/
├── ERS_SRS_2B_v2.0.pdf
├── ERS_SRS_2B_v2.0.tex
├── referencias.bib
├── assets/
└── README.md
```

## Compilación del ERS/SRS

El documento debe compilarse utilizando **pdfLaTeX**. Desde la carpeta `01_ERS/` ejecutar:

```bash
pdflatex -interaction=nonstopmode -halt-on-error ERS_SRS_2B_v2.0.tex
pdflatex -interaction=nonstopmode -halt-on-error ERS_SRS_2B_v2.0.tex
```

La segunda compilación permite estabilizar referencias y elementos internos del documento.

---

# 2. Evidencias del trabajo de campo

Las evidencias se encuentran organizadas en `02_Evidencias/`:

```
02_Evidencias/
├── 00_Restringido/
├── Codificacion_Tematica/
├── Consentimientos/
├── Cuestionario/
├── Documentos_Organizacion/
├── Fotos_Aplicacion/
├── Fotos_Entorno/
├── Member_Checking/
├── Respuestas/
├── Transcripciones/
├── Validacion_Walkthrough/
├── fichas_tecnicas.csv
└── README.md
```

Las evidencias incluyen consentimientos informados, cuestionario de necesidades, respuestas del cuestionario, fotografías de contexto y de aplicación, documentos de la organización, sesiones walkthrough, Member Checking, transcripciones, análisis cualitativo, y archivos multimedia.

## Evidencia multimedia

El inventario técnico de la evidencia multimedia se encuentra en `02_Evidencias/fichas_tecnicas.csv`, con nombre, tipo, ruta relativa, duración, formato, códec, tamaño y hash SHA-256 por archivo.

---

# 3. Evidencia restringida

Los materiales originales que pueden contener información identificable se mantienen separados de la evidencia pública. El contenedor cifrado se distribuye como asset del Release `evidencias-2B`; la carpeta `02_Evidencias/00_Restringido/` conserva la documentación y el checksum de verificación. La contraseña de acceso no se publica en el repositorio.

---

# 4. Privacidad

No se publican abiertamente datos que permitan identificar directamente a los participantes (cédulas, teléfonos, correos, direcciones, firmas, voces o rostros identificables, diagnósticos asociados directamente a una persona). Las versiones públicas utilizan códigos de participante y mecanismos de anonimización.

---

# 5. Trazabilidad

Los artefactos de trazabilidad se encuentran en `04_Trazabilidad/`, incluida la matriz consolidada `Matriz_Trazabilidad_Final_PE5_Rubrica.csv` (58 trazas documentales: RF, RNF generales, RNF de IA) y la priorización MoSCoW/Kano en `priorizacion_moscow_kano.csv`.

---

# 6. Modelado

Los modelos del sistema se encuentran en `03_Modelado/`: contexto, i* SD/SR, casos de uso, secuencia, actividad, estados, clases, componentes, despliegue, procesos, DFD y mockups.

---

# 7. Producto Mínimo Viable

El prototipo del sistema se encuentra en `05_MVP/`, con aplicaciones diferenciadas para paciente y fisioterapeuta.

---

# 8. Experimento — Enfoque 1: RF humano vs. LLM (Entrega Final 2B)

El material experimental se encuentra en `06_Experimento/`.

## Diseño y resultado

Estudio comparativo, ciego y **preregistrado en OSF** (DOI [10.17605/OSF.IO/82Q76](https://doi.org/10.17605/OSF.IO/82Q76), registrado 2026-09-12), sobre la calidad de Requisitos Funcionales (RF) elicitados por el equipo humano vs. generados por un LLM (GPT-5.5-mini), a partir de las mismas 18 transcripciones anonimizadas.

- 66 RF (33 humanos + 33 LLM) evaluados de forma ciega por 4 jueces independientes, en 5 dimensiones de calidad (escala Likert 1-5).
- Acuerdo entre evaluadores: κ de Fleiss bajo a nulo (entre -0.011 y 0.167 según dimensión).
- Análisis confirmatorio pareado (n=11 pares temáticos estrictos): prueba t apareada con corrección de Holm-Bonferroni. **Ninguna dimensión mostró diferencia estadísticamente significativa** (todos los p ajustados > 0.05).

```
06_Experimento/
├── protocolo.pdf
├── osf_registration.pdf
├── osf_deviations.pdf
├── instrumentos/
├── prompts_llm/
├── datos_crudos/
├── datos_procesados/
├── resultados/
└── scripts_analisis/
```

Reproducción:

```bash
python 06_Experimento/scripts_analisis/analisis_experimento_llm_humano.py
```

Los ejercicios sintéticos realizados durante PE5 (etapa anterior del proyecto, con un enfoque de explicabilidad descartado) se conservan únicamente como antecedentes metodológicos en `PE5_Informe_Final/` y **no se presentan como resultados empíricos** de esta entrega.

---

# 9. Antecedente histórico PE5

La carpeta `PE5_Informe_Final/` contiene el cierre correspondiente a la Práctica Experimental 5 (informe, fuente LaTeX, bibliografía, figuras, métricas de simulaciones controladas, presentación de esa etapa). Se conserva para mantener trazabilidad histórica del desarrollo del proyecto; no constituye por sí solo la Entrega Final 2B, y sus simulaciones sintéticas no deben interpretarse como evidencia empírica humana.

---

# 10. Publicación académica

La preparación para publicación académica se encuentra en `07_Publicacion/`:

```
07_Publicacion/
├── manuscrito_final.pdf
├── manuscrito_final.tex
├── manuscrito_final.bbl
├── references.bib
├── analisis_revistas.md
├── README.md
├── README_manuscrito.md
├── figuras/
├── transcripciones/
└── dataset_zenodo/
```

**Título del manuscrito:** *An Empirical Comparison of Human-Elicited and LLM-Generated Functional Requirements in a Physical Therapy Follow-Up System: A Paired-Analyst Study in Ecuador*

**Revista objetivo:** Requirements Engineering (Springer Nature). Ver análisis completo en `07_Publicacion/analisis_revistas.md`.

## Dataset publicado en Zenodo

`07_Publicacion/dataset_zenodo/` contiene la documentación y materiales del conjunto de datos reproducible publicado en Zenodo (cuestionario general del proyecto + material del experimento comparativo: prompts del LLM, script de análisis, matriz de pareo temático, transcripciones anonimizadas).

- **DOI:** `10.5281/zenodo.22315298`
- **Versión publicada:** 1.0 (2026-09-05) — pendiente de actualizar a v2.0 con el material del experimento comparativo.
- **Acceso:** Público / Open

La reproducción de los datos generales del proyecto se realiza desde la raíz del repositorio mediante:

```bash
python 07_Datos/scripts/orquestar.py
```

---

# 11. Ética

La documentación ética se encuentra en `08_Etica/`: protocolo de investigación, instrumentos de recolección, consentimiento informado, plan de gestión de datos, documentación de aval, declaraciones de conflicto de intereses, análisis de riesgos, cronograma y registros relacionados. Las aprobaciones que no hayan sido emitidas oficialmente no se presentan como aprobadas.

---

# 12. Defensa

Los materiales se encuentran en `09_Defensa/`: presentación en PDF y editable, guion, folleto de una hoja, y README de la defensa. El video de defensa se incorpora cuando exista una grabación real.

---

# 13. Inteligencia Artificial

SICST contempla componentes inteligentes orientados al apoyo del seguimiento terapéutico (análisis de movimiento por visión por computadora, priorización de alertas). Los requisitos asociados consideran rendimiento, privacidad, equidad, explicabilidad, supervisión humana, monitoreo y manejo de fallos. Las salidas del sistema no se presentan como diagnóstico médico ni sustituyen la evaluación del fisioterapeuta.

Adicionalmente, un LLM (GPT-5.5-mini) fue usado como **objeto de estudio** en el experimento comparativo del punto 8 (documentado en `06_Experimento/prompts_llm/`), y un asistente de IA (Claude, Anthropic) se usó como apoyo en la organización del repositorio, desarrollo de scripts de procesamiento de datos reales, y redacción del manuscrito — sin fabricar ni alterar ningún participante, respuesta o resultado empírico.

---

# 14. Autoría y evidencia de proceso

La documentación de autoría y proceso de trabajo se encuentra en `10_Autoria/`:

```
10_Autoria/
├── declaracion_uso_ia.md / .docx
├── aporte_individual.docx
├── doble_codificacion/
├── correspondencia/
├── notas_campo/
├── bitacora_sesiones/
├── inventario_exif/
├── verificacion_previa/
├── capturas/
├── fuentes_editables/
├── grabaciones/
└── fotos_equipo/
```

---

# 15. Reproducibilidad

## Reproducción del ERS

```bash
cd 01_ERS
pdflatex -interaction=nonstopmode -halt-on-error ERS_SRS_2B_v2.0.tex
pdflatex -interaction=nonstopmode -halt-on-error ERS_SRS_2B_v2.0.tex
```

## Reproducción del cuestionario general

```bash
python 07_Datos/scripts/orquestar.py
```

## Reproducción del experimento comparativo (Enfoque 1)

```bash
python 06_Experimento/scripts_analisis/analisis_experimento_llm_humano.py
```

## Verificación SHA-256

```bash
sha256sum -c checksums.sha256
```

o en PowerShell:

```powershell
Get-FileHash -Algorithm SHA256 "ruta\archivo"
```

---

# 16. Integridad del repositorio

Los hashes generales del repositorio se encuentran en `checksums.sha256` (137 archivos verificados). Este archivo se regenera después de cada cambio relevante a los artefactos evaluables, para no mantener checksums desactualizados.

---

# 17. Citación

La información de citación del proyecto se encuentra en `CITATION.cff`, versión **2.0**, sincronizada con la línea base vigente.

Identificadores persistentes incorporados:

- DOI de Zenodo (dataset): `10.5281/zenodo.22315298`
- DOI de OSF (registro previo del experimento): `10.17605/OSF.IO/82Q76`
- SWHID (Software Heritage): **pendiente** — se incorporará una vez archivado el repositorio en [Software Heritage](https://archive.softwareheritage.org) mediante el botón "Save code now".

---

# 18. Licencia

La licencia general del repositorio se encuentra en `LICENSE` (MIT). La licencia aplicada al código fuente no implica autorización automática para redistribuir evidencia sensible o identificable. Los datasets y materiales específicos pueden incluir condiciones adicionales dentro de sus respectivas carpetas (ver `07_Datos/LICENSE-DATA.txt`). El material restringido no debe redistribuirse públicamente.

---

# 19. Control de versiones

Las modificaciones relevantes del proyecto se documentan en `CHANGELOG.md`.

La línea base de la Entrega Final 2B está identificada con la etiqueta anotada:

```
v2.0-entrega4
```

---

# 20. Estado de la Entrega Final

**Proyecto:** Sistema Inteligente de Control y Seguimiento de Terapia Física — SICST
**Entrega:** Final 2B
**Versión:** 2.0
**Estado:** integración y cierre documental del paquete académico.

Los artefactos pendientes de aprobación institucional o de ejecución real se identifican expresamente como pendientes y no se presentan como completados.

---

# Repositorio oficial

https://github.com/gleiston-guerrero/SICST_ISR401
