# CHANGELOG — SICST

Registro de cambios del proyecto **Sistema Inteligente de Control y Seguimiento
de Terapia Física (SICST)** para la Entrega Final 2B de Ingeniería de
Requerimientos — ISR-401.

---

## [2B-v2.2] - 2026-09-18

### Cierre técnico y documental

Versión de cierre previa a la recreación de la etiqueta anotada
`v2.0-entrega4`.

La composición final del equipo corresponde a:

- Contreras Chávez Kevin Germán.
- Zambrano Moya Angelo Paul.

La salida de Morán Pilaguano Frixon Fernando y Viteri García Jonathan Enrique
se documenta en `10_Autoria/declaracion_cambio_composicion_equipo.md` y en su
versión PDF firmada. Los aportes históricos existentes se conservan bajo su
autoría original.

### Reproducibilidad de `07_Datos`

- Se actualizó el pipeline reproducible a **10 pasos numerados más el
  orquestador**.
- La ejecución completa se realiza desde la raíz con:

  ```bash
  python 07_Datos/scripts/orquestar.py
  ```

- La cadena final valida **79 respuestas codificadas**:
  - 62 pacientes o ex pacientes;
  - 14 familiares o cuidadores;
  - 3 fisioterapeutas.
- `diccionario_datos.csv` documenta **51 columnas**.
- `resultados/` contiene **17 artefactos generados** más su `README.md`.
- Se incorporó análisis cualitativo reproducible:
  - 36 decisiones comparadas;
  - 33 acuerdos;
  - 3 desacuerdos;
  - acuerdo observado de 91.67 %;
  - Cohen κ = `0.7187`;
  - IC bootstrap 95 % = `[0.3077, 1.0000]`;
  - 10 000 remuestreos;
  - semilla `401`.
- `saturacion_tematica.csv` documenta 18 sesiones canónicas y 17 temas
  acumulados.
- `manifiesto_datos.csv` documenta **37 archivos**.
- `checksums_datos.sha256` se regenera al final de la cadena.

### Registro OSF y experimento

- Registro del protocolo en OSF:
  `10.17605/OSF.IO/82Q76`.
- El registro se realizó el **12/09/2026** en hora de Ecuador continental.
- Las entrevistas originales anteceden al registro OSF; por ello, el
  repositorio no presenta el registro como previo a la recolección de las
  entrevistas.
- La comparación humano vs. LLM se documenta como **exploratoria** respecto a
  esa cronología.
- El estudio compara 33 RF humanos con 33 RF generados por GPT-5.5-mini a
  partir de las mismas 18 transcripciones anonimizadas.
- El análisis pareado utiliza 11 pares temáticos estrictos con corrección de
  Holm-Bonferroni.
- Ninguna de las dimensiones evaluadas mostró diferencia estadísticamente
  significativa después del ajuste.
- El registro verificable se conserva en:

  `06_Experimento/registro_previo/osf_registration.pdf`

### Autoría y evidencia de proceso

`10_Autoria/` quedó actualizado con evidencia verificable de los dos
integrantes activos:

- **5 capturas** de Angelo Zambrano.
- **4 capturas** de Kevin Contreras.
- **2 grabaciones** reales de sesiones de trabajo.
- **30 notas de campo o síntesis** asociadas a jornadas diferenciadas.
- `bitacora_elicitacion.csv` con **30 sesiones/jornadas documentadas**.
- aporte individual disponible en `.md` y `.docx`.
- declaración de uso de IA disponible en `.md` y `.docx`.
- declaración firmada del cambio de composición del equipo.
- retrospectiva final del proyecto.
- fuentes editables e inventarios de integridad.

No se crean evidencias ficticias para antiguos integrantes.

### Trazabilidad e IA

- La matriz vigente es:

  `04_Trazabilidad/Matriz_Trazabilidad_Final.csv`

- La matriz contiene **62 trazas documentales**:
  - 33 requisitos funcionales;
  - 15 requisitos no funcionales generales;
  - 12 requisitos no funcionales específicos de IA;
  - 2 restricciones trazadas.
- Los 12 RNF-IA están documentados en:

  `01_ERS/componentes_IA/requisitos_no_funcionales_ia.csv`

- Los RNF-IA incluyen métricas, umbrales, verificación, responsables,
  frecuencia, equidad, supervisión humana, monitoreo y nivel de riesgo.

### Evidencia multimedia

- El inventario técnico vigente se encuentra en:

  `02_Evidencias/Fichas tecnicas/fichas_tecnicas.csv`

- El inventario final documenta **67 piezas multimedia**.
- El contenedor cifrado se distribuye mediante el Release
  `evidencias-2B`.
- La contraseña no se publica en el repositorio.

### Integridad

- `checksums.sha256` contiene **151 entradas SHA-256 verificables**.
- El paquete `07_Datos/` mantiene su propio
  `07_Datos/checksums_datos.sha256`.
- Los manifiestos y checksums se regeneran cuando cambia un artefacto incluido
  en su alcance.

### Documentación corregida

- `README.md` raíz actualizado con:
  - ruta vigente de `Fichas tecnicas`;
  - ruta vigente de `Matriz_Trazabilidad_Final.csv`;
  - 62 trazas documentales;
  - ubicación correcta del registro OSF;
  - 151 entradas SHA-256 verificables;
  - composición final del equipo;
  - estado actual de autoría y reproducibilidad.
- `07_Datos/README_datos.md` actualizado a la cadena real de 10 pasos y 17
  artefactos generados.
- `07_Datos/manifiesto_datos.csv` regenerado después de actualizar la
  documentación reproducible.

### Línea base

La etiqueta prevista para la línea base final sigue siendo:

```text
v2.0-entrega4
```

Debe recrearse al final del cierre para que sea **anotada** y apunte al último
commit que integra todas las correcciones.

---

## [2B-v2.1] - 2026-09-13

### Estado de esa versión

Esta sección conserva el estado histórico alcanzado el 13/09/2026. Varias
carencias que existían en ese momento fueron resueltas posteriormente en
`2B-v2.2`.

### Agregado

- Registro del protocolo experimental en OSF, DOI
  `10.17605/OSF.IO/82Q76`.
- Experimento comparativo: 33 RF elicitados por el equipo humano frente a
  33 RF generados por GPT-5.5-mini, a partir de las mismas 18 transcripciones
  anonimizadas.
- Prompt del LLM, datos crudos, evaluaciones ciegas y matriz de pareo temático.
- Script reproducible de análisis del experimento.
- Manuscrito final reescrito y alineado con la comparación humano vs. LLM.
- Paquete de publicación y materiales anonimizados.
- Expansión inicial del pipeline de `07_Datos/`.
- Ampliación de la documentación de autoría.
- `fair_assessment.pdf` incorporado en la raíz.
- `.mailmap` ampliado para normalizar identidades Git.

### Aclaración cronológica

Las entrevistas de campo fueron realizadas antes del registro OSF. Por ello,
el cierre posterior documenta la comparación como exploratoria respecto a esa
cronología y no presenta el registro como previo a la recolección original de
las entrevistas.

### Corregido

- URLs desactualizadas del repositorio.
- Estructura de carpetas de defensa y autoría.
- Normalización de identidades Git.
- Referencias bibliográficas utilizadas por el manuscrito.

### Eliminado

- Enfoque de explicabilidad basado en datos sintéticos que había sido
  descartado.
- Fuente Springer no compilable y artefactos duplicados u obsoletos.
- Copias redundantes de documentos y datos ya preservados en su ubicación
  canónica.

### Pendientes identificados en esa fecha

Al 13/09/2026 todavía faltaban varias evidencias de autoría y ampliaciones del
pipeline. Estas tareas se resolvieron posteriormente y se documentan en
`2B-v2.2`.

Permanecen como mejoras externas no indispensables para describir el estado
actual del repositorio:

- posible archivado futuro en Software Heritage;
- posible nueva versión del depósito Zenodo con materiales complementarios
  posteriores.

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
- Se sincronizaron resultados y documentación con el conjunto de 79
  respuestas.
- Se eliminó documentación que indicaba erróneamente que todavía no existía
  un depósito persistente.

### Estado

`2B-v2.0` fue una línea base intermedia. El estado final del cierre se
documenta en `2B-v2.2`.
