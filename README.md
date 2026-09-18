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

**Nota sobre integración del equipo:** la composición final de la Entrega Final 2B corresponde a Kevin Germán Contreras Chávez y Angelo Paul Zambrano Moya. El repositorio conserva aportes históricos de **Morán Pilaguano Frixon Fernando** (usuario `FrixonMP`) cuando existen en el historial de Git; **Viteri García Jonathan Enrique** también dejó de formar parte del equipo antes del cierre. La situación se documenta en `10_Autoria/declaracion_cambio_composicion_equipo.md` y en su versión PDF firmada. Los aportes históricos se mantienen bajo su autoría original y no se reasignan.

---

## Identificadores persistentes

| Recurso | Identificador |
|---|---|
| Registro retrospectivo del protocolo experimental (OSF) | [10.17605/OSF.IO/82Q76](https://doi.org/10.17605/OSF.IO/82Q76) |
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
- experimentación empírica con registro retrospectivo en OSF (Enfoque 1: RF humano vs. LLM);
- preparación de publicación académica;
- privacidad y gestión ética;
- defensa final.

SICST se plantea como una herramienta de apoyo y no sustituye la valoración, diagnóstico ni decisión del profesional de salud.

---

# Línea base originalmente evaluada

La línea base originalmente evaluada corresponde a:

**Entrega Final 2B — versión 2.0**

y se identifica mediante la etiqueta anotada:

```text
v2.0-entrega4
```

La etiqueta `v2.0-entrega4` se conserva inmutable y continúa asociada al commit originalmente evaluado `f901513`. No debe moverse. Las correcciones posteriores se identificarán mediante una nueva etiqueta anotada sobre el commit final corregido.

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

También se conserva la priorización MoSCoW/Kano en:

```text
04_Trazabilidad/priorizacion_moscow_kano.csv
```

---

# 6. Modelado

Los modelos del sistema se encuentran en `03_Modelado/`: contexto, i* SD/SR, casos de uso, secuencia, actividad, estados, clases, componentes, despliegue, procesos, DFD y mockups.

---

# 7. Producto Mínimo Viable

El prototipo del sistema se encuentra en `05_MVP/`, con aplicaciones diferenciadas para paciente y fisioterapeuta.

---

# 8. Experimento — Enfoque 1: RF humano vs. LLM

El material experimental se encuentra en `06_Experimento/`.

## Cronología correcta

Las **18 entrevistas** utilizadas como corpus fuente pertenecen a una etapa previa de elicitación y construcción del ERS.

La evidencia del repositorio permite reconstruir la siguiente cronología:

1. realización de las entrevistas y elicitación de requisitos;
2. generación del conjunto de requisitos mediante GPT-5.5-mini;
3. realización de las cuatro evaluaciones ciegas;
4. registro del protocolo experimental en OSF;
5. análisis estadístico y documentación posterior.

El protocolo experimental fue registrado en OSF con los siguientes datos:

- DOI: `10.17605/OSF.IO/82Q76`
- Fecha UTC: `2026-09-13T00:50:38.265668Z`
- Ecuador continental (UTC-5): `2026-09-12 19:50:38`

Cuando se realizó el registro OSF ya existían el conjunto de requisitos generado mediante el LLM y las cuatro hojas de evaluación ciega utilizadas posteriormente en el análisis.

Por tanto, el registro se documenta como un **registro retrospectivo del protocolo** y no como una prerregistración confirmatoria previa a la generación de los datos experimentales.

En consecuencia:

- las entrevistas del ERS no se presentan como prerregistradas;
- la generación del conjunto LLM ocurrió antes del registro OSF;
- las cuatro evaluaciones ciegas ocurrieron antes del registro OSF;
- las comparaciones inferenciales se interpretan como exploratorias y no confirmatorias;
- las desviaciones u operacionalizaciones estadísticas posteriores al registro se documentan en `06_Experimento/osf_deviations.pdf`.

## Diseño y resultado

El estudio compara:

- 33 RF elicitados por el equipo humano;
- 33 RF generados por GPT-5.5-mini;
- las mismas 18 transcripciones anonimizadas como corpus fuente;
- 66 ítems evaluados;
- 4 evaluadores ciegos al origen de los requisitos;
- evaluación ciega;
- 5 dimensiones de calidad en escala Likert de 1 a 5;
- 11 pares temáticos estrictos para la comparación pareada.

La evaluación ciega se realizó sin revelar a los jueces si cada requisito era humano o generado por LLM.

El análisis incluye κ de Fleiss, estadística descriptiva, comparación pareada y corrección Holm-Bonferroni.

En la ejecución reproducible actual, ninguna de las cinco dimensiones principales mostró diferencia estadísticamente significativa después de la corrección por comparaciones múltiples. La ausencia de significancia no se interpreta como prueba de equivalencia.

```text
06_Experimento/
├── protocolo.pdf
├── osf_deviations.pdf
├── registro_previo/
│   ├── README.md
│   ├── consulta.json
│   └── osf_registration.pdf
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

La carpeta `PE5_Informe_Final/` contiene el cierre correspondiente a la Práctica Experimental 5. Se conserva para mantener trazabilidad histórica del desarrollo del proyecto; no constituye por sí sola la Entrega Final 2B y sus simulaciones sintéticas no deben interpretarse como evidencia empírica humana.

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

**Revista objetivo:** Requirements Engineering (Springer Nature).

## Dataset publicado en Zenodo

`07_Publicacion/dataset_zenodo/` contiene la documentación y materiales del conjunto de datos reproducible publicado en Zenodo.

- **DOI:** `10.5281/zenodo.22315298`
- **Versión publicada:** 1.0
- **Fecha de publicación:** 2026-09-05
- **Acceso:** Público / Open

El material complementario más reciente del experimento y del cierre 2B permanece versionado en este repositorio.

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

Los requisitos verificables del componente inteligente se documentan en:

```text
01_ERS/componentes_IA/requisitos_no_funcionales_ia.csv
```

El archivo contiene **12 RNF-IA** con métrica, unidad, umbral, método de verificación, responsable, frecuencia, equidad, supervisión humana, monitoreo y nivel de riesgo.

Sus identificadores se encuentran trazados en:

```text
04_Trazabilidad/Matriz_Trazabilidad_Final.csv
```

Las salidas del sistema no se presentan como diagnóstico médico ni sustituyen la evaluación del fisioterapeuta.

GPT-5.5-mini fue utilizado como **objeto de estudio** en el experimento comparativo. El uso de asistentes de IA como apoyo al desarrollo y documentación se declara en `10_Autoria/declaracion_uso_ia.md`.

---

# 14. Autoría y evidencia de proceso

La documentación de autoría se encuentra en `10_Autoria/`:

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
- 30 notas de campo o síntesis asociadas a jornadas diferenciadas;
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

Si los comandos no muestran errores y vuelven al prompt, la verificación de integridad ha finalizado correctamente.

---

# 16. Integridad del repositorio

El archivo `checksums.sha256` cubre **505 de los 506 archivos versionados** del repositorio. El único archivo excluido es `checksums.sha256` porque un manifiesto no puede contener de forma estable su propio hash.

El paquete `07_Datos/` mantiene además su propio archivo:

```text
07_Datos/checksums_datos.sha256
```

Los manifiestos y checksums deben regenerarse cuando cambien artefactos que formen parte de sus respectivos alcances de verificación.

---

# 17. Citación

La información de citación del proyecto se encuentra en `CITATION.cff`, versión **2.0**.

Identificadores persistentes incorporados:

- DOI de Zenodo: `10.5281/zenodo.22315298`
- DOI del registro OSF: `10.17605/OSF.IO/82Q76`
- SWHID (Software Heritage): pendiente de archivado futuro.

---

# 18. Licencia

La licencia general del repositorio se encuentra en `LICENSE` (MIT).

La licencia del código no implica autorización automática para redistribuir evidencia sensible o identificable. Los datasets y materiales específicos pueden incluir condiciones adicionales dentro de sus respectivas carpetas.

---

# 19. Control de versiones

Las modificaciones relevantes del proyecto se documentan en `CHANGELOG.md`.

La línea base originalmente evaluada de la Entrega Final 2B se identifica con la etiqueta anotada:

```text
v2.0-entrega4
```

La etiqueta `v2.0-entrega4` permanece asociada al commit originalmente evaluado y no debe moverse. El cierre corregido utilizará una nueva etiqueta anotada.

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
