# Notas de campo y correspondencia con transcripciones

Esta carpeta contiene las notas de campo y las síntesis retrospectivas asociadas
con las entrevistas y walkthroughs realizados durante el proceso de elicitación
y validación del proyecto **Sistema Inteligente de Control y Seguimiento de
Terapia Física (SICST)**.

Los identificadores utilizados preservan el anonimato de los participantes y
permiten mantener la trazabilidad entre las sesiones realizadas, las
transcripciones conservadas y los documentos asociados.

---

## 1. Propósito de las notas de campo

Las notas de campo se conservan como evidencia complementaria del proceso de
elicitación y validación de requisitos.

Su propósito es registrar o sintetizar aspectos relevantes observados durante
las sesiones, tales como:

* necesidades expresadas por los participantes;
* dificultades observadas durante la terapia física;
* comentarios relacionados con el seguimiento terapéutico;
* observaciones sobre el uso de los mockups;
* reacciones durante los walkthroughs;
* información relevante para la identificación y validación de requisitos.

Las notas no sustituyen las transcripciones. Ambos artefactos cumplen funciones
diferentes y se utilizan conjuntamente para mantener la trazabilidad del
trabajo de campo.

---

## 2. Criterio de correspondencia

Para relacionar las notas con las demás evidencias del repositorio se aplican
los siguientes criterios:

* El nombre de cada archivo identifica la fecha de la sesión documentada.
* El código anonimizado del participante permite relacionar cada documento con
  su entrevista o walkthrough correspondiente.
* Cuando la fecha de elaboración visible en una hoja es posterior a la fecha de
  la sesión original, el documento se clasifica como una **síntesis
  retrospectiva preparada a partir de la transcripción conservada**.
* Las síntesis retrospectivas no se presentan como notas tomadas durante la
  sesión original.
* `EVA2-PAC-10` a `EVA2-PAC-14` es la denominación canónica utilizada para esos
  participantes.
* La forma abreviada `EV2`, presente en algunas hojas históricas, se refiere a
  los mismos participantes y no representa casos adicionales.
* Las variantes históricas `Walktrough` y `Walkthrough` corresponden al mismo
  tipo de actividad. Los archivos fuente no se modifican únicamente para
  corregir esa grafía.

---

## 3. Diferencia entre archivos de transcripción y sesiones reales

Durante una revisión anterior del repositorio se observó una diferencia entre
el número de documentos almacenados en la carpeta de transcripciones y el
número de notas de campo disponibles.

Es importante aclarar que:

**El número de archivos de transcripción no equivale necesariamente al número
de sesiones independientes de elicitación.**

Una misma jornada puede generar más de un archivo de transcripción debido a:

* separación entre entrevista y walkthrough;
* división de una entrevista extensa en varias partes;
* conservación de variantes históricas de nombres;
* separación de fases para facilitar el análisis;
* archivos duplicados o variantes documentales conservadas por trazabilidad.

Por esta razón, la cobertura se evalúa por **sesión o jornada diferenciada** y
no mediante una comparación directa archivo por archivo.

---

## 4. Corpus de sesiones documentadas

El corpus final documentado del proyecto contiene:

* **18 entrevistas anonimizadas**;
* **14 walkthroughs de validación**.

Sin embargo, dos participantes realizaron la entrevista y el walkthrough
dentro de una misma jornada de trabajo:

* `WALK-NTEC-01`, 19/07/2026;
* `WALK-TEC-01`, 01/08/2026.

Por tanto, el conteo de jornadas diferenciadas es:

```text
18 entrevistas
+ 14 walkthroughs
- 2 jornadas compartidas
= 30 sesiones o jornadas diferenciadas
```

La carpeta `10_Autoria/notas_campo/` contiene **30 archivos documentales**
asociados con esas jornadas. De estos archivos, 8 son notas contemporáneas y
22 son síntesis retrospectivas.

---

## 5. Sesiones con entrevista y walkthrough en una misma jornada

| Jornada                    | Evidencia conservada                                  | Documento asociado                                          |
| -------------------------- | ----------------------------------------------------- | ----------------------------------------------------------- |
| `WALK-NTEC-01`, 19/07/2026 | Entrevista y walkthrough                              | `2026-07-19_Walkthrough_No_Tecnico_WALK-NTEC-01_Notas.jpeg` |
| `WALK-TEC-01`, 01/08/2026  | Entrevista, segunda parte de entrevista y walkthrough | `2026-08-01_Walkthrough_Tecnico_WALK-TEC-01_Notas.jpeg`     |

En estas dos jornadas se conserva una sola hoja de síntesis porque la entrevista
y el walkthrough corresponden a una misma sesión de trabajo con el mismo
participante.

La existencia de varios archivos de transcripción se debe a la separación de
fases o partes realizada para facilitar el análisis y no significa que hayan
existido varias sesiones independientes.

---

## 6. Cobertura real de notas

La colección actual contiene:

* **8 notas contemporáneas del 17/06/2026**, elaboradas durante las sesiones con
  estudiantes de fisioterapia, familiares o cuidadores y un profesional de
  fisioterapia;
* **22 síntesis retrospectivas**, elaboradas el 17/09/2026 a partir de las
  transcripciones previamente conservadas de las sesiones realizadas en julio
  y agosto.

Por tanto, la cobertura real de notas contemporáneas es de **8 de 30 sesiones
o jornadas diferenciadas**.

Para las otras 22 sesiones no se conserva una nota escrita durante la sesión
original. Sus hojas se mantienen únicamente como síntesis retrospectivas y no
se presentan como evidencia contemporánea.

En total existen **30 archivos documentales**, distribuidos de la siguiente
manera:

```text
Notas contemporáneas:       8
Síntesis retrospectivas:   22
Total de archivos:         30
```

---

## 7. Correspondencia detallada por sesión

La relación completa entre:

* fecha;
* participante;
* tipo de sesión;
* transcripción o transcripciones asociadas;
* nota de campo o síntesis retrospectiva;
* estado;
* observación;

se encuentra documentada en:

`../bitácora_sesiones/bitacora_elicitacion.csv`

Este archivo permite verificar la cobertura sesión por sesión y explica los
casos en que una misma jornada produjo más de una transcripción.

En la bitácora, las 22 sesiones que no poseen una nota contemporánea deben
figurar con el estado:

`No hubo nota contemporánea; síntesis retrospectiva disponible`

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

> **Un documento por sesión o jornada diferenciada, con una explicación
> documental cuando una jornada genera varias transcripciones y con una
> distinción expresa entre nota contemporánea y síntesis retrospectiva.**

---

## 9. Síntesis retrospectivas

Las 22 hojas correspondientes a las sesiones de julio y agosto fueron
elaboradas el 17/09/2026 durante la etapa de cierre, utilizando como fuente las
transcripciones originales previamente conservadas.

Estas hojas se identifican expresamente como **síntesis retrospectivas**.

No se presentan como notas escritas durante la fecha original de la entrevista
o del walkthrough.

Su función es documentar de manera trazable los principales elementos de cada
sesión utilizando como fuente una transcripción que ya existía previamente en
el repositorio.

No se crean participantes, respuestas, fechas de entrevistas ni hechos que no
estén respaldados por las evidencias originales.

---

## 10. Trazabilidad con las transcripciones

Las transcripciones utilizadas como evidencia primaria se encuentran en:

`../../02_Evidencias/Transcripciones/`

El README de esa carpeta documenta el corpus final de entrevistas y los códigos
anonimizados de los participantes.

Los documentos de esta carpeta utilizan los mismos códigos siempre que es
posible para facilitar la correspondencia entre:

```text
sesión
  ↓
transcripción
  ↓
nota contemporánea o síntesis retrospectiva
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
3. **cantidad de notas contemporáneas**;
4. **cantidad de síntesis retrospectivas**.

En el cierre actual del proyecto:

```text
Sesiones o jornadas diferenciadas:       30
Notas contemporáneas disponibles:         8
Sesiones sin nota contemporánea:         22
Síntesis retrospectivas disponibles:     22
Total de archivos documentales:          30
```

Las diferencias entre el número bruto de archivos de transcripción y el número
de sesiones están explicadas por la existencia de varias transcripciones
asociadas con una misma jornada.

La existencia de una síntesis retrospectiva no convierte el documento en una
nota tomada durante la sesión original.

---

## 13. Principio de integridad académica

No se generan notas ficticias ni se modifican fechas únicamente para aumentar
el conteo de archivos.

Cuando una nota contemporánea no existe, su ausencia se reconoce expresamente.
La síntesis retrospectiva correspondiente se conserva claramente identificada
como tal y respaldada por una transcripción existente.

De esta manera, el repositorio preserva la trazabilidad del trabajo de campo
sin presentar evidencia creada retrospectivamente como si hubiera sido
producida durante la sesión original.
