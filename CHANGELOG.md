# CHANGELOG — SICST

Registro de cambios del proyecto **Sistema Inteligente de Control y Seguimiento de Terapia Física (SICST)** para la Entrega Final 2B de Ingeniería de Requerimientos — ISR-401.

---

## [2B-v2.2] - 2026-09-18

### Cierre técnico y documental

Versión de cierre previa a la recreación final de la etiqueta anotada:

```text
v2.0-entrega4
```

La composición final del equipo corresponde a:

- Contreras Chávez Kevin Germán.
- Zambrano Moya Angelo Paul.

La salida de Morán Pilaguano Frixon Fernando y Viteri García Jonathan Enrique se documenta en `10_Autoria/declaracion_cambio_composicion_equipo.md` y en su versión PDF firmada. Los aportes históricos existentes se conservan bajo su autoría original.

### Registro OSF y experimento

- El protocolo del experimento comparativo humano–LLM fue registrado en OSF:
  `10.17605/OSF.IO/82Q76`.
- El registro se realizó el **12/09/2026 a las 19:50:38** en hora de Ecuador continental.
- Las 18 entrevistas utilizadas como corpus fuente pertenecen a la etapa previa de elicitación del ERS y ya existían antes del registro OSF.
- El registro OSF corresponde al protocolo del experimento comparativo humano–LLM.
- El conjunto LLM y las **cuatro evaluaciones ciegas** ya existían antes del registro OSF; por ello, el registro se considera retrospectivo y las comparaciones inferenciales se interpretan como exploratorias.
- El estudio compara 33 RF humanos con 33 RF generados por GPT-5.5-mini a partir de las mismas 18 transcripciones anonimizadas.
- El análisis utiliza 11 pares temáticos estrictos y corrección de Holm-Bonferroni.
- Ninguna de las cinco dimensiones principales mostró diferencia estadísticamente significativa después del ajuste.
- Las desviaciones u operacionalizaciones estadísticas posteriores al registro se documentan en `06_Experimento/osf_deviations.pdf`.
- El comprobante de registro se conserva en `06_Experimento/registro_previo/osf_registration.pdf`.

### Reproducibilidad de `07_Datos`

- El pipeline reproducible utiliza **10 pasos numerados más el orquestador**.
- La ejecución completa se realiza desde la raíz con:

```bash
python 07_Datos/scripts/orquestar.py
```

- La cadena valida **79 respuestas codificadas**:
  - 62 pacientes o ex pacientes;
  - 14 familiares o cuidadores;
  - 3 fisioterapeutas.
- `diccionario_datos.csv` documenta **51 columnas**.
- `resultados/` contiene **17 artefactos generados** más su `README.md`.
- El análisis cualitativo reproducible genera:
  - 36 decisiones comparadas;
  - 33 acuerdos;
  - 3 desacuerdos;
  - 91.67 % de acuerdo observado;
  - Cohen κ = `0.7187`;
  - IC bootstrap 95 % = `[0.3077, 1.0000]`;
  - 10 000 remuestreos;
  - semilla `401`.
- `saturacion_tematica.csv` documenta 18 sesiones canónicas y 17 temas acumulados.
- `manifiesto_datos.csv` documenta **37 archivos**.
- `checksums_datos.sha256` se regenera al final de la cadena.

### Autoría y evidencia de proceso

`10_Autoria/` quedó actualizado con evidencia verificable de los dos integrantes activos:

- **5 capturas** de Angelo Zambrano.
- **4 capturas** de Kevin Contreras.
- **2 grabaciones** reales de sesiones de trabajo.
- **30 notas de campo o síntesis** asociadas a jornadas diferenciadas.
- `bitacora_elicitacion.csv` con **30 sesiones/jornadas documentadas**.
- aporte individual disponible en `.md` y `.docx`.
- declaración de uso de IA disponible en `.md` y `.docx`.
- declaración firmada del cambio de composición del equipo.
- retrospectiva final.
- fuentes editables e inventarios de integridad.

No se crean evidencias ficticias para antiguos integrantes.

### Trazabilidad e IA

- La matriz vigente es:

```text
04_Trazabilidad/Matriz_Trazabilidad_Final.csv
```

- La matriz contiene **62 trazas documentales**:
  - 33 requisitos funcionales;
  - 15 requisitos no funcionales generales;
  - 12 requisitos no funcionales específicos de IA;
  - 2 restricciones trazadas.
- Los 12 RNF-IA están documentados en:

```text
01_ERS/componentes_IA/requisitos_no_funcionales_ia.csv
```

- Los RNF-IA incluyen métricas, umbrales, verificación, responsables, frecuencia, equidad, supervisión humana, monitoreo y nivel de riesgo.

### Evidencia multimedia

- El inventario técnico vigente se encuentra en:

```text
02_Evidencias/Fichas tecnicas/fichas_tecnicas.csv
```

- El inventario final documenta **67 piezas multimedia**.
- El contenedor cifrado se distribuye mediante el Release `evidencias-2B`.
- La contraseña no se publica en el repositorio.

### Integridad

- `checksums.sha256` contiene **151 entradas SHA-256 verificables**.
- El paquete `07_Datos/` mantiene su propio `07_Datos/checksums_datos.sha256`.
- Los manifiestos y checksums se regeneran cuando cambia un artefacto incluido en su alcance.

### Documentación corregida

- `README.md` raíz sincronizado con:
  - ruta vigente de `Fichas tecnicas`;
  - ruta vigente de `Matriz_Trazabilidad_Final.csv`;
  - 62 trazas documentales;
  - cronología real del registro retrospectivo OSF;
  - 151 entradas SHA-256 verificables;
  - composición final del equipo;
  - estado actual de autoría y reproducibilidad.
- `04_Trazabilidad/README.md` actualizado con 62 trazas y 12 RNF-IA.
- `07_Datos/README_datos.md` actualizado a la cadena real de 10 pasos y 17 artefactos generados.
- `07_Datos/manifiesto_datos.csv` regenerado después de actualizar la documentación reproducible.
- `CITATION.cff` actualizado con la descripción del registro retrospectivo del protocolo experimental.

### Línea base

La etiqueta anotada `v2.0-entrega4` corresponde a la línea base evaluada originalmente y se conserva sin modificar.

Las correcciones posteriores a la evaluación se integrarán en una nueva etiqueta anotada, manteniendo intacta la trazabilidad de `v2.0-entrega4`.

---

## [2B-v2.1] - 2026-09-13

### Estado de esa versión

Esta sección conserva el estado histórico alcanzado el 13/09/2026. Varias carencias existentes en ese momento fueron resueltas posteriormente en `2B-v2.2`.

### Agregado

- Registro del protocolo experimental en OSF, DOI `10.17605/OSF.IO/82Q76`.
- Experimento comparativo: 33 RF elicitados por el equipo humano frente a 33 RF generados por GPT-5.5-mini a partir de las mismas 18 transcripciones anonimizadas.
- Prompt del LLM, datos crudos, evaluaciones ciegas y matriz de pareo temático.
- Script reproducible de análisis del experimento.
- Manuscrito final reescrito y alineado con la comparación humano vs. LLM.
- Paquete de publicación y materiales anonimizados.
- Expansión inicial del pipeline de `07_Datos/`.
- Ampliación de la documentación de autoría.
- `fair_assessment.pdf` incorporado en la raíz.
- `.mailmap` ampliado para normalizar identidades Git.

### Aclaración cronológica

Las entrevistas utilizadas como corpus pertenecían a una etapa previa de elicitación del ERS.

En la documentación de esta versión se afirmó erróneamente que el registro OSF precedía a la generación del conjunto LLM y a las cuatro evaluaciones ciegas. La revisión posterior de la evidencia del repositorio estableció que el conjunto LLM y las cuatro evaluaciones ciegas ya existían antes del registro OSF.

Por tanto, el registro OSF se considera **retrospectivo respecto del experimento**, y las comparaciones inferenciales se interpretan como exploratorias y no confirmatorias.

### Corregido

- URLs desactualizadas del repositorio.
- Estructura de carpetas de defensa y autoría.
- Normalización de identidades Git.
- Referencias bibliográficas utilizadas por el manuscrito.

### Eliminado

- Enfoque de explicabilidad basado en datos sintéticos que había sido descartado.
- Fuente Springer no compilable y artefactos duplicados u obsoletos.
- Copias redundantes de documentos y datos ya preservados en su ubicación canónica.

### Pendientes identificados en esa fecha

Al 13/09/2026 todavía faltaban varias evidencias de autoría y ampliaciones del pipeline. Estas tareas se resolvieron posteriormente y se documentan en `2B-v2.2`.

Permanecen como mejoras externas no indispensables para describir el estado actual del repositorio:

- posible archivado futuro en Software Heritage;
- posible nueva versión del depósito Zenodo con materiales complementarios posteriores.

---

## [2B-v2.0] - 2026-09-05

### Línea base intermedia

Versión intermedia de la Entrega Final 2B.

Autores activos:

- Contreras Chávez Kevin Germán.
- Zambrano Moya Angelo Paul.

### Agregado

- Estructura reproducible inicial en `07_Datos/`.
- Datos crudos y procesados.
- Resultados derivados.
- Diccionario de datos.
- Checksums SHA-256.
- `desviaciones.md`.
- `registro_deposito.md`.
- `LICENSE-DATA.txt`.
- `07_Datos/scripts/orquestar.py`.
- Evidencia de doble codificación.
- Declaración de uso de inteligencia artificial.
- `.mailmap` para normalización de identidades Git.

### Dataset reproducible

El conjunto reproducible contenía **79 respuestas codificadas**:

- 62 pacientes o ex pacientes;
- 14 familiares o cuidadores;
- 3 fisioterapeutas.

### Publicación en Zenodo

- DOI: `10.5281/zenodo.22315298`
- Versión: 1.0
- Fecha de publicación: 2026-09-05
- Acceso: público / Open

### Corregido

- Se retiraron referencias a un conjunto anterior de 31 respuestas.
- Se sincronizaron resultados y documentación con el conjunto de 79 respuestas.
- Se eliminó documentación que indicaba erróneamente que todavía no existía un depósito persistente.

### Estado

`2B-v2.0` fue una línea base intermedia. El estado final del cierre se documenta en `2B-v2.2`.
