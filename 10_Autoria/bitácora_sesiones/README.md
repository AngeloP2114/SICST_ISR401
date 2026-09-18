# Bitácoras de sesiones — SICST

Esta carpeta contiene las bitácoras utilizadas para documentar tanto la
actividad de trabajo del equipo como la correspondencia entre sesiones de
elicitación, transcripciones y notas de campo del proyecto
**Sistema Inteligente de Control y Seguimiento de Terapia Física (SICST)**.

## Archivos incluidos

### `bitacora_sesiones.csv`

Registra sesiones de trabajo reconstruidas a partir del historial de Git.

Incluye:

- fecha;
- integrante;
- hora de inicio;
- hora de finalización;
- número de commits realizados;
- resumen de la actividad desarrollada.

Su finalidad es aportar evidencia de autoría y participación técnica de los
integrantes a lo largo del desarrollo del proyecto.

---

### `bitacora_elicitacion.csv`

Documenta la correspondencia entre las sesiones reales de elicitación y
validación, las transcripciones conservadas y las notas de campo asociadas.

Incluye:

- fecha;
- código anonimizado del participante;
- tipo de sesión;
- transcripciones asociadas;
- nota de campo asociada;
- estado;
- observación.

Esta bitácora se utiliza especialmente para verificar la cobertura de notas de
campo por sesión o jornada diferenciada.

## Criterio de conteo

El número de archivos de transcripción no equivale necesariamente al número de
sesiones de elicitación.

Una misma jornada puede generar varios archivos por:

- división de una entrevista en varias partes;
- separación entre entrevista y walkthrough;
- conservación de variantes históricas de nombres;
- organización de fases para facilitar el análisis.

Por esta razón, la cobertura se verifica por sesión o jornada diferenciada y
no únicamente por cantidad bruta de archivos.

La bitácora de elicitación documenta actualmente **30 sesiones o jornadas
diferenciadas**, cada una relacionada con su nota de campo o síntesis
correspondiente.

## Relación con otras evidencias

Las notas de campo se encuentran en:

`../notas_campo/`

Las transcripciones se encuentran en:

`../../02_Evidencias/Transcripciones/`

El README de notas de campo explica con mayor detalle los casos donde una misma
jornada produjo varias transcripciones.

## Integridad

No se crean sesiones, notas o evidencias ficticias para igualar artificialmente
el número de archivos.

Cuando existe más de una transcripción para una misma jornada, esa situación se
documenta en `bitacora_elicitacion.csv`.

Las síntesis retrospectivas se identifican como tales y no se presentan como
notas tomadas durante la sesión original.
