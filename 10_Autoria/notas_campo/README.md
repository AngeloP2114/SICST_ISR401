# Notas de campo y correspondencia con transcripciones

Esta carpeta contiene las notas de campo y hojas de síntesis asociadas con las
entrevistas y walkthroughs realizados durante el proceso de elicitación y
validación del proyecto **Sistema Inteligente de Control y Seguimiento de
Terapia Física (SICST)**.

Los identificadores utilizados preservan el anonimato de los participantes y
permiten mantener trazabilidad entre las sesiones realizadas, las
transcripciones conservadas y las notas asociadas.

---

## 1. Propósito de las notas de campo

Las notas de campo se conservan como evidencia complementaria del proceso de
elicitación y validación de requisitos.

Su propósito es registrar o sintetizar aspectos relevantes observados durante
las sesiones, tales como:

- necesidades expresadas por los participantes;
- dificultades observadas durante la terapia física;
- comentarios relacionados con el seguimiento terapéutico;
- observaciones sobre el uso de los mockups;
- reacciones durante los walkthroughs;
- información relevante para la identificación y validación de requisitos.

Las notas no sustituyen las transcripciones. Ambos artefactos cumplen funciones
diferentes y se utilizan conjuntamente para mantener la trazabilidad del
trabajo de campo.

---

## 2. Criterio de correspondencia

Para relacionar las notas con las demás evidencias del repositorio se aplican
los siguientes criterios:

- Cada archivo de notas indica la fecha de la sesión en su nombre.
- El código anonimizado del participante permite relacionar la nota con su
  entrevista o walkthrough correspondiente.
- Cuando una hoja muestra una **fecha de elaboración posterior a la sesión
  original**, se trata de una **síntesis retrospectiva preparada a partir de la
  transcripción conservada**.
- Las síntesis retrospectivas no se presentan como notas tomadas durante la
  sesión original.
- `EVA2-PAC-10` a `EVA2-PAC-14` es la denominación canónica utilizada para
  esos participantes.
- La forma abreviada `EV2` presente en algunas hojas históricas se refiere a
  los mismos participantes y no representa casos adicionales.
- Las variantes históricas `Walktrough` y `Walkthrough` corresponden al mismo
  tipo de actividad. Los archivos fuente no se modifican únicamente para
  corregir esa grafía.

---

## 3. Diferencia entre archivos de transcripción y sesiones reales

Durante una revisión anterior del repositorio se observó una diferencia entre
el número de notas de campo y el número de archivos almacenados dentro de la
carpeta de transcripciones.

Es importante aclarar que:

**el número de archivos de transcripción no equivale necesariamente al número
de sesiones independientes de elicitación.**

Una misma jornada puede generar más de un archivo de transcripción debido a:

- separación entre entrevista y walkthrough;
- división de una entrevista extensa en varias partes;
- conservación de variantes históricas de nombres;
- separación de fases para facilitar el análisis;
- archivos duplicados o variantes documentales conservadas por trazabilidad.

Por esta razón, la cobertura de notas de campo se evalúa por
**sesión o jornada diferenciada**, y no mediante una comparación directa
archivo por archivo.

---

## 4. Corpus de sesiones documentadas

El corpus final documentado del proyecto contiene:

- **18 entrevistas anonimizadas**;
- **14 walkthroughs de validación**.

Sin embargo, dos participantes realizaron entrevista y walkthrough dentro de
una misma jornada de trabajo:

- `WALK-NTEC-01`, 19/07/2026;
- `WALK-TEC-01`, 01/08/2026.

Por tanto, el conteo de jornadas diferenciadas es:

```text
18 entrevistas
+ 14 walkthroughs
- 2 jornadas compartidas
= 30 jornadas/sesiones diferenciadas
```

La carpeta `10_Autoria/notas_campo/` contiene actualmente **30 archivos de
notas**, correspondientes a esas jornadas diferenciadas.

---

## 5. Sesiones con entrevista y walkthrough en una misma jornada

| Jornada | Evidencia conservada | Nota asociada |
|---|---|---|
| `WALK-NTEC-01`, 19/07/2026 | Entrevista y walkthrough | `2026-07-19_Walkthrough_No_Tecnico_WALK-NTEC-01_Notas.jpeg` |
| `WALK-TEC-01`, 01/08/2026 | Entrevista, segunda parte de entrevista y walkthrough | `2026-08-01_Walkthrough_Tecnico_WALK-TEC-01_Notas.jpeg` |

En estas dos jornadas se conserva una sola hoja de síntesis porque corresponden
a una misma sesión de trabajo con el mismo participante.

La existencia de varios archivos de transcripción se debe a la separación de
fases o partes realizada para facilitar el análisis y no significa que hayan
existido varias sesiones independientes.

---

## 6. Control de cobertura de notas

La colección actual contiene:

- **8 notas iniciales del 17/06/2026**, correspondientes a estudiantes de
  fisioterapia, familiares/cuidadores y un profesional de fisioterapia;
- **8 notas de entrevistas de pacientes o expacientes**;
- **14 notas asociadas con walkthroughs y sesiones de validación**.

Total:

**30 archivos de notas de campo o síntesis.**

Este total corresponde a las **30 jornadas diferenciadas** identificadas en el
corpus final.

---

## 7. Correspondencia detallada por sesión

La relación completa entre:

- fecha;
- participante;
- tipo de sesión;
- transcripción o transcripciones asociadas;
- nota de campo;
- estado;
- observación;

se encuentra documentada en:

`../bitácora_sesiones/bitacora_elicitacion.csv`

Este archivo permite verificar la cobertura sesión por sesión y explica los
casos en que una misma jornada produjo más de una transcripción.

---

## 8. Aclaración sobre la observación de los 53 archivos

En una revisión anterior se contabilizaron múltiples archivos dentro de la
carpeta de transcripciones y se compararon con el número de notas de campo
existentes en ese momento.

Ese conteo no debe interpretarse como 53 sesiones distintas.

El repositorio conserva archivos históricos, divisiones de una misma sesión,
entrevistas separadas por partes y archivos correspondientes a diferentes
fases de una misma jornada.

Por esta razón, no se crean notas adicionales únicamente para igualar el
número bruto de archivos de transcripción.

Crear varias notas para una misma sesión con el único objetivo de igualar el
conteo de archivos produciría una representación incorrecta del trabajo de
campo.

El criterio utilizado en el cierre es:

> **una nota o síntesis por sesión/jornada diferenciada, con explicación
> documental cuando una jornada genera varias transcripciones.**

---

## 9. Notas retrospectivas

Algunas hojas fueron elaboradas durante la etapa de cierre a partir de las
transcripciones originales conservadas.

Estas hojas se identifican expresamente como **síntesis retrospectivas**.

No se presentan como evidencia escrita durante la fecha original de la
entrevista.

Su función es documentar de manera trazable los principales elementos de la
sesión utilizando como fuente una transcripción que ya existía previamente en
el repositorio.

No se crean participantes, respuestas, fechas de entrevistas ni hechos que no
estén respaldados por las evidencias originales.

---

## 10. Trazabilidad con las transcripciones

Las transcripciones utilizadas como evidencia primaria se encuentran en:

`../../02_Evidencias/Transcripciones/`

El README de esa carpeta documenta el corpus final de entrevistas y los códigos
anonimizados de participantes.

Las notas de esta carpeta utilizan los mismos códigos siempre que es posible
para facilitar la correspondencia entre:

```text
sesión
  ↓
transcripción
  ↓
nota de campo / síntesis
  ↓
codificación temática
  ↓
requisitos
```

---

## 11. Integridad de la evidencia

La integridad binaria y la presencia o ausencia de metadatos EXIF de los
archivos se documentan en:

`../inventario_exif/inventario_exif.csv`

Cuando un archivo no contiene metadatos EXIF suficientes para demostrar su
fecha de captura, no se infiere ni se fabrica dicha información.

Las fechas utilizadas para la correspondencia provienen de la evidencia
documental disponible y de la organización histórica del repositorio.

---

## 12. Criterio de verificación

Para verificar esta sección deben distinguirse:

1. **cantidad de archivos de transcripción**;
2. **cantidad de sesiones o jornadas reales diferenciadas**;
3. **cantidad de notas de campo o síntesis disponibles**.

En el cierre actual del proyecto:

```text
Sesiones/jornadas diferenciadas: 30
Notas de campo o síntesis:        30
```

Las diferencias entre el número bruto de archivos de transcripción y el número
de notas están explicadas por la existencia de varias transcripciones
asociadas a una misma jornada.

---

## 13. Principio de integridad académica

No se generan notas ficticias únicamente para aumentar el conteo de archivos.

Cuando una nota contemporánea no existe, la ausencia se reconoce o se conserva
una síntesis retrospectiva claramente identificada como tal, siempre basada en
una transcripción existente.

De esta manera, el repositorio preserva la trazabilidad del trabajo de campo
sin presentar evidencia creada retrospectivamente como si hubiera sido
producida durante la sesión original.
