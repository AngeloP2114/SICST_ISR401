# CHANGELOG — SICST

Registro de los cambios correspondientes a la línea base vigente del proyecto
**Sistema Inteligente de Control y Seguimiento de Terapia Física (SICST)**.

## [2B-v2.1] - 2026-09-13

### Línea base

Cierre de los criterios de piso de la Entrega Final 2B: registro previo
externo del experimento (OSF), ejecución del experimento comparativo real
(Enfoque 1), reescritura del manuscrito, expansión del paquete de datos, y
completitud de la carpeta de autoría.

### Agregado

- Registro previo del protocolo experimental en OSF, DOI
  `10.17605/OSF.IO/82Q76` (2026-09-12), anterior a la generación de datos.
- Experimento comparativo real (Enfoque 1): 33 RF elicitados por el equipo
  humano vs. 33 RF generados por LLM (GPT-5.5-mini), a partir de las mismas
  18 transcripciones anonimizadas.
  - `06_Experimento/prompts_llm/prompt_generacion_RF_llm.md`: prompt exacto,
    modelo, fecha, confirmación de no uso de información externa.
  - `06_Experimento/datos_crudos/`: RF del LLM, hoja de evaluación ciega,
    evaluaciones de 4 jueces independientes.
  - `06_Experimento/datos_procesados/matriz_trazabilidad_tema_RF.csv`: pareo
    temático humano-LLM (11 pares estrictos).
  - `06_Experimento/scripts_analisis/analisis_experimento_llm_humano.py`:
    análisis reproducible (κ de Fleiss, prueba t apareada, corrección
    Holm-Bonferroni).
  - `06_Experimento/protocolo.pdf`, `osf_registration.pdf`,
    `osf_deviations.pdf`.
- Manuscrito reescrito por completo (`07_Publicacion/manuscrito_final.tex`
  y `.pdf`, 8 páginas), alineado con la pregunta de investigación real
  (Enfoque 1) y con los resultados del experimento comparativo.
- Paquete `07_Publicacion/dataset_zenodo/` completado: `ANONYMIZATION.md`,
  `ETHICS.md`, prompts del LLM, script de análisis, matriz de pareo
  temático, transcripciones anonimizadas de las 18 entrevistas.
- Pipeline de `07_Datos/` expandido de 1 a 8 scripts numerados
  (`01_extraer_crudos.py` a `08_generar_figuras.py`) con un orquestador de
  una sola orden; de 1 a 13 archivos de resultados (tablas y figuras).
- `10_Autoria/`: agregada bitácora de sesiones (`bitacora_sesiones/`,
  derivada del historial real de Git), inventario EXIF/hash de 48 archivos
  multimedia (`inventario_exif/`), verificación previa
  (`verificacion_previa/`), correspondencia con la organización (6
  fotografías reales), y notas de campo (8 fotografías reales).
- `fair_assessment.pdf` en la raíz: autoevaluación FAIR con F-UJI sobre el
  dataset de Zenodo, puntaje agregado 88% (Findable: advanced, Accessible:
  advanced, Interoperable: moderate, Reusable: moderate).
- Etiqueta anotada de línea base: `v2.0-entrega4`.

### Corregido

- Referencias bibliográficas: de 30 a 33 entradas (`references.bib`),
  agregadas las citas de Fleiss (1971), Cohen (1960) y Cheng et al. (2026)
  usadas en el manuscrito reescrito.
- URLs desactualizadas (`_2A`) corregidas a `_2B` en `README.md`,
  `CITATION.cff` (raíz y `dataset_zenodo/`), y archivos relacionados.
- Renombrado `9_Defensa/` a `09_Defensa/` para coincidir exactamente con el
  árbol de la Sección 9.1 de la guía.
- Renombradas carpetas de `10_Autoria/` para consistencia de nomenclatura
  (minúsculas, sin espacios).
- `.mailmap` actualizado con la identidad de `FrixonMP`, colaborador que
  dejó de formar parte del equipo el 06/09/2026; su aporte histórico se
  conserva en el historial de Git por transparencia.

### Eliminado

- Enfoque de explicabilidad con datos sintéticos (protocolo, script y
  resultados de una exploración descartada en favor del Enfoque 1),
  eliminado de `06_Experimento/` con commits documentados individualmente.
- `manuscrito_final_springer.tex`: fuente no compilable (requería
  `sn-jnl.cls`, no redistribuible por Springer Nature), huérfano.
- `07_Publicacion/07_Datos/`: subcarpeta duplicada con transcripciones que
  ya residían correctamente en `02_Evidencias/`.
- Archivos `.docx` duplicados y desactualizados en `07_Datos/` y
  `07_Publicacion/dataset_zenodo/`.

### Pendiente para el cierre

- Referencias: completar de 33 a 40 entradas mínimas.
- SWHID: archivar el repositorio en Software Heritage y agregar el
  identificador a `CITATION.cff`.
- Publicar la versión 2.0 del depósito de Zenodo incluyendo el material del
  experimento comparativo.
- Completar en `10_Autoria/`: capturas por integrante, fuentes editables de
  diagramas, grabación de sesión de trabajo, fotos del equipo.

---

## [2B-v2.0] - 2026-09-05

### Línea base

La versión vigente del repositorio corresponde a:

**Entrega Final 2B — versión 2.0**

Autores actuales de la entrega:

- Contreras Chávez Kevin Germán
- Zambrano Moya Angelo Paul

---

### Agregado

- Estructura reproducible definitiva en `07_Datos/`.
- Datos crudos utilizados para la reproducción del análisis.
- Datos procesados generados a partir de los datos crudos.
- Resultados derivados reproducibles.
- Diccionario de datos actualizado.
- Archivo de checksums SHA-256 para verificación de integridad.
- Archivo `desviaciones.md` para documentar transformaciones y limitaciones.
- Archivo `registro_deposito.md` para registrar el depósito persistente.
- Condiciones específicas de uso en `07_Datos/LICENSE-DATA.txt`.
- Script reproducible: `07_Datos/scripts/orquestar.py`.
- Evidencia de doble codificación en `10_Autoria/doble_codificacion/`.
- Cálculo del porcentaje de acuerdo entre codificadores, Cohen κ, e
  intervalo de confianza mediante bootstrap.
- Declaración de uso de inteligencia artificial en
  `10_Autoria/declaracion_uso_ia.md`.
- Archivo `.mailmap` en la raíz para normalizar identidades Git de los
  autores actuales.

### Dataset reproducible

El conjunto reproducible vigente contenía **79 respuestas codificadas**:
62 pacientes o ex pacientes, 14 familiares o cuidadores, 3 fisioterapeutas.

### Publicación en Zenodo

- **DOI:** `10.5281/zenodo.22315298`
- **Versión:** 1.0
- **Fecha de publicación:** 2026-09-05

### Corregido

- Se eliminó la indicación antigua de que todavía no existía un depósito
  en Zenodo ni un DOI.
- Se corrigieron referencias a un conjunto anterior de únicamente 31
  respuestas, actualizadas a 79.
- Se eliminaron archivos y figuras generados con la versión anterior del
  conjunto de datos.
- Se sincronizaron README, citación, licencia, resultados y registro de
  depósito con la publicación real.

### Estado de la versión

La versión `2B-v2.0` constituyó la línea base intermedia previa al cierre
de los criterios de piso de la Entrega Final 2B (ver `2B-v2.1` arriba).
