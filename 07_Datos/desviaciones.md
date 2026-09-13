# Desviaciones y transformaciones del paquete de datos SICST

## Fuente

La fuente principal utilizada por la cadena reproducible es:

`07_Datos/datos_crudos/respuestas_cuestionario_2B.csv`

El archivo corresponde a las respuestas reales recopiladas para el proyecto SICST.

## Transformaciones previstas

El pipeline (`07_Datos/scripts/`, 7 pasos + orquestador) realiza únicamente
transformaciones reproducibles sobre el archivo de origen.

### Eliminación de fecha y hora

La primera columna del archivo crudo contiene la fecha y hora de envío de cada respuesta.

Esta columna se excluye de la versión procesada para reducir información temporal innecesaria y disminuir el riesgo de identificación indirecta.

### Limpieza

El paso 2 (`02_limpiar_datos.py`) elimina espacios al inicio y final de los campos y descarta únicamente filas completamente vacías.

### Conservación de respuestas

No se modifican, completan ni fabrican respuestas de participantes.

No se generan participantes inexistentes.

## Cambio respecto a la versión anterior del pipeline

La versión anterior del pipeline consistía en un único script que generaba
solamente el resumen de participantes por perfil. Se amplió a 7 pasos
numerados para producir un análisis más completo (estadísticos por
dimensión Likert, tablas de frecuencia por pregunta, y tablas cruzadas),
sin modificar ni reinterpretar ningún dato de origen: todos los resultados
adicionales se derivan de las mismas 79 respuestas reales ya existentes.

## Resultados derivados

El pipeline genera 13 archivos en `resultados/`: un resumen de
participantes por perfil, estadísticos descriptivos de las preguntas en
escala Likert por perfil, 9 tablas de frecuencia por pregunta categórica o
de opción múltiple, y 2 tablas cruzadas perfil × variable clave.

Todos los resultados se obtienen exclusivamente desde los datos almacenados en `datos_crudos`.

## Limitaciones

Los códigos de participantes se mantienen para permitir trazabilidad interna del estudio. Antes de cualquier depósito público externo se realizará una revisión adicional de privacidad y consentimiento.

Los consentimientos firmados y demás documentos con datos personales no forman parte del paquete público de datos.
