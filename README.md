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

**Nota sobre integración del equipo:** la composición final de la Entrega Final 2B corresponde a Kevin Germán Contreras Chávez y Angelo Paul Zambrano Moya. El repositorio conserva aportes históricos de **Morán Pilaguano Frixon Fernando** (usuario `FrixonMP`) cuando existen en el historial de Git; **Viteri García Jonathan Enrique** también dejó de formar parte del equipo antes del cierre. La situación se documenta de forma expresa en `10_Autoria/declaracion_cambio_composicion_equipo.md` y en su versión PDF firmada. Los aportes históricos se mantienen bajo su autoría original y no se reasignan.

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
- experimentación empírica registrada en OSF (Enfoque 1: RF humano vs. LLM);
- preparación de publicación académica;
- privacidad y gestión ética;
- defensa final.

SICST se plantea como una herramienta de apoyo y no sustituye la valoración, diagnóstico ni decisión del profesional de salud.

---

# Línea base vigente

La línea base vigente del repositorio corresponde a:

**Entrega Final 2B — versión 2.0**

y queda identificada mediante la etiqueta anotada:

```text
v2.0-entrega4
```

La etiqueta debe apuntar al último commit que integra todas las correcciones del examen suspenso.

La carpeta `PE5_Informe_Final/` se conserva únicamente como **antecedente histórico** correspondiente a la Práctica Experimental 5. Los documentos, simulaciones, métricas y materiales almacenados en PE5 no sustituyen los artefactos finales requeridos para la Entrega Final 2B.

---

# Estructura principal

```text
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

```text
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

```text
02_Evidencias/
├── 00_Restringido/
├── Codificacion_Tematica/
├── Consentimientos/
├── Cuestionario/
├── Documentos_Organizacion/
├── Fichas tecnicas/
│   ├── fichas_tecnicas.csv
│   ├── duraciones_reales_ffprobe.csv
│   └── README.md
├── Fotos_Aplicacion/
├── Fotos_Entorno/
├── Member_Checking/
├── Respuestas/
├── Transcripciones/
├── Validacion_Walkthrough/
└── README.md
```

Las evidencias incluyen consentimientos informados, cuestionario de necesidades, respuestas del cuestionario, fotografías de contexto y de aplicación, documentos de la organización, sesiones walkthrough, Member Checking, transcripciones, análisis cualitativo y archivos multimedia.

## Evidencia multimedia

El inventario técnico definitivo de la evidencia multimedia se encuentra en:

```text
02_Evidencias/Fichas tecnicas/fichas_tecnicas.csv
```

La ficha registra, entre otros campos, nombre, tipo, ruta relativa, duración, formato, códec, tamaño, SHA-256, ubicación del depósito y URL de descarga.

El inventario final contiene **67 piezas multimedia** depositadas en el contenedor cifrado del Release `evidencias-2B`.

---

# 3. Evidencia restringida

Los materiales originales que pueden contener información identificable se mantienen separados de la evidencia pública. El contenedor cifrado se distribuye como asset del Release `evidencias-2B`; la carpeta `02_Evidencias/00_Restringido/` conserva la documentación y el checksum de verificación.

La contraseña de acceso no se publica en el repositorio y se entrega al docente por un canal institucional separado.

---

# 4. Privacidad

No se publican abiertamente datos que permitan identificar directamente a los participantes (cédulas, teléfonos, correos, direcciones, firmas, voces o rostros identificables, diagnósticos asociados directamente a una persona). Las versiones públicas utilizan códigos de participante y mecanismos de anonimización.

---

# 5. Trazabilidad

Los artefactos de trazabilidad se encuentran en `04_Trazabilidad/`, incluida la matriz consolidada:

```text
04_Trazabilidad/Matriz_Trazabilidad_Final.csv
```

La matriz vigente contiene **62 trazas documentales**:

- 33 requisitos funcionales;
- 15 requisitos no funcionales generales;
- 12 requisitos no funcionales específicos de IA;
- 2 restricciones trazadas.

También se conserva la priorización MoSCoW/Kano en `04_Trazabilidad/priorizacion_moscow_kano.csv`.

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

Estudio comparativo, ciego y **registrado en OSF** (DOI [10.17605/OSF.IO/82Q76](https://doi.org/10.17605/OSF.IO/82Q76), registrado el 12/09/2026 en hora de Ecuador continental), sobre la calidad de Requisitos Funcionales (RF) elicitados por el equipo humano frente a requisitos generados por un LLM (GPT-5.5-mini), a partir de las mismas 18 transcripciones anonimizadas.

Las entrevistas originales fueron realizadas antes del registro OSF. Por ello, la documentación del proyecto no presenta el registro como previo a la recolección de las entrevistas y la comparación estadística se interpreta como **exploratoria** respecto a esa cronología.

- 66 RF (33 humanos + 33 LLM) evaluados de forma ciega por 4 jueces independientes, en 5 dimensiones de calidad (escala Likert 1–5).
- Acuerdo entre evaluadores: κ de Fleiss bajo a nulo (entre -0.011 y 0.167 según dimensión).
- Análisis pareado exploratorio sobre **11 pares temáticos estrictos**, con corrección de Holm-Bonferroni.
- **Ninguna dimensión mostró diferencia estadísticamente significativa** (todos los valores p ajustados > 0.05).

```text
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

Los ejercicios sintéticos realizados durante PE5 se conservan únicamente como antecedentes metodológicos en `PE5_Informe_Final/` y **no se presentan como resultados empíricos** de esta entrega.

---

# 9. Antecedente histórico PE5

La carpeta `PE5_Informe_Final/` contiene el cierre correspondiente a la Práctica Experimental 5 (informe, fuente LaTeX, bibliografía, figuras, métricas de simulaciones controladas y presentación de esa etapa). Se conserva para mantener trazabilidad histórica del desarrollo del proyecto; no constituye por sí solo la Entrega Final 2B, y sus simulaciones sintéticas no deben interpretarse como evidencia empírica humana.

---

# 10. Publicación académica

La preparación para publicación académica se encuentra en `07_Publicacion/`:

```text
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

`07_Publicacion/dataset_zenodo/` contiene la documentación y materiales del conjunto de datos reproducible publicado en Zenodo.

- **DOI:** `10.5281/zenodo.22315298`
- **Versión publicada:** 1.0 (2026-09-05)
- **Acceso:** Público / Open

El material complementario más reciente del experimento y del cierre 2B permanece versionado en este repositorio.

La reproducción de los datos generales del proyecto se realiza desde la raíz mediante:

```bash
python 07_Datos/scripts/orquestar.py
```

---

# 11. Ética

La documentación ética se encuentra en `08_Etica/`: protocolo de investigación, instrumentos de recolección, consentimiento informado, plan de gestión de datos, documentación de aval, declaraciones de conflicto de intereses, análisis de riesgos, cronograma y registros relacionados.

Las aprobaciones que no hayan sido emitidas oficialmente no se presentan como aprobadas.

---

# 12. Defensa

Los materiales se encuentran en `09_Defensa/`: presentación en PDF y editable, guion, folleto de una hoja y README de la defensa. El video de defensa se incorpora únicamente cuando existe una grabación real.

---

# 13. Inteligencia Artificial

SICST contempla componentes inteligentes orientados al apoyo del seguimiento terapéutico, incluyendo análisis de movimiento por visión por computadora y priorización de alertas.

Los requisitos asociados consideran:

- rendimiento;
- equidad;
- explicabilidad;
- supervisión humana;
- monitoreo;
- manejo de fallos;
- clasificación interna de riesgo.

Los requisitos verificables del componente inteligente se documentan en:

```text
01_ERS/componentes_IA/requisitos_no_funcionales_ia.csv
```

El archivo contiene **12 RNF-IA** con métrica, unidad, umbral, método de verificación, responsable, frecuencia, equidad, supervisión humana, monitoreo y nivel de riesgo. Sus identificadores se encuentran trazados en el ERS y en `04_Trazabilidad/Matriz_Trazabilidad_Final.csv`.

Las salidas del sistema no se presentan como diagnóstico médico ni sustituyen la evaluación del fisioterapeuta.

Adicionalmente, un LLM (GPT-5.5-mini) fue usado como **objeto de estudio** en el experimento comparativo documentado en `06_Experimento/prompts_llm/`. El uso de asistentes de IA como apoyo al desarrollo y documentación se declara en `10_Autoria/declaracion_uso_ia.md`.

---

# 14. Autoría y evidencia de proceso

La documentación de autoría y proceso de trabajo se encuentra en `10_Autoria/`:

```text
10_Autoria/
├── aporte_individual.md
├── aporte_individual.docx
├── declaracion_uso_ia.md
├── declaracion_uso_ia.docx
├── declaracion_cambio_composicion_equipo.md
├── declaracion_cambio_composicion_equipo.pdf
├── doble_codificacion/
├── correspondencia/
├── notas_campo/
├── bitácora_sesiones/
├── inventario_exif/
├── verificacion_previa/
├── capturas/
├── fuentes_editables/
├── grabaciones/
├── fotos_equipo/
└── retrospectiva_equipo.md
```

La carpeta contiene:

- 5 capturas de Angelo Zambrano;
- 4 capturas de Kevin Contreras;
- 2 grabaciones reales de sesiones de trabajo;
- 30 notas de campo/síntesis asociadas a jornadas diferenciadas;
- bitácora de elicitación;
- formatos abiertos de aporte individual y declaración de uso de IA;
- retrospectiva final;
- declaración firmada sobre el cambio de composición del equipo.

---

# 15. Reproducibilidad

## Reproducción del ERS

```bash
cd 01_ERS
pdflatex -interaction=nonstopmode -halt-on-error ERS_SRS_2B_v2.0.tex
pdflatex -interaction=nonstopmode -halt-on-error ERS_SRS_2B_v2.0.tex
```

## Reproducción del cuestionario general

Desde la raíz:

```bash
python 07_Datos/scripts/orquestar.py
```

La cadena ejecuta **10 pasos** y regenera datos procesados, diccionario, análisis descriptivos, cruces, acuerdo entre codificadores, saturación temática, figuras, manifiesto y checksums.

## Reproducción del experimento comparativo

```bash
python 06_Experimento/scripts_analisis/analisis_experimento_llm_humano.py
```

## Verificación SHA-256 del paquete general

```bash
sha256sum -c checksums.sha256 --quiet
```

## Verificación SHA-256 de `07_Datos`

```bash
cd 07_Datos
sha256sum -c checksums_datos.sha256 --quiet
```

Si los comandos no muestran errores y vuelven al prompt, la verificación de integridad finaliza correctamente.

---

# 16. Integridad del repositorio

Los hashes generales disponibles en `checksums.sha256` contienen actualmente **153 entradas verificables** correspondientes a los artefactos incluidos por el mecanismo de verificación del repositorio.

El paquete `07_Datos/` mantiene además su propio archivo:

```text
07_Datos/checksums_datos.sha256
```

Los manifiestos y checksums deben regenerarse cuando cambien artefactos que formen parte de sus respectivos alcances de verificación.

---

# 17. Citación

La información de citación del proyecto se encuentra en `CITATION.cff`, versión **2.0**.

Identificadores persistentes incorporados:

- DOI de Zenodo (dataset): `10.5281/zenodo.22315298`
- DOI de OSF (registro del experimento): `10.17605/OSF.IO/82Q76`
- SWHID (Software Heritage): **pendiente** — se incorporará una vez archivado el repositorio en Software Heritage.

---

# 18. Licencia

La licencia general del repositorio se encuentra en `LICENSE` (MIT). La licencia aplicada al código fuente no implica autorización automática para redistribuir evidencia sensible o identificable.

Los datasets y materiales específicos pueden incluir condiciones adicionales dentro de sus respectivas carpetas (ver `07_Datos/LICENSE-DATA.txt`). El material restringido no debe redistribuirse públicamente.

---

# 19. Control de versiones

Las modificaciones relevantes del proyecto se documentan en `CHANGELOG.md`.

La línea base de la Entrega Final 2B está identificada con la etiqueta anotada:

```text
v2.0-entrega4
```

Para la entrega final, esta etiqueta debe resolver al último commit de cierre del examen suspenso.

---

# 20. Estado de la Entrega Final

**Proyecto:** Sistema Inteligente de Control y Seguimiento de Terapia Física — SICST  
**Entrega:** Final 2B  
**Versión:** 2.0  
**Estado:** cierre documental y técnico del paquete académico.

Los artefactos pendientes de aprobación institucional o de ejecución real se identifican expresamente como pendientes y no se presentan como completados.

---

# Repositorio oficial

https://github.com/gleiston-guerrero/SICST_ISR401
