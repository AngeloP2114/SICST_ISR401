# Retrospectiva del equipo — Cierre del proyecto SICST

**Fecha:** 2026-09-18
**Proyecto:** Sistema Inteligente de Control y Seguimiento de Terapia Física (SICST)
**Asignatura:** Ingeniería de Requisitos — ISR-401
**Repositorio vigente:** https://github.com/gleiston-guerrero/SICST_ISR401

## Propósito

Esta retrospectiva documenta las principales decisiones, correcciones,
dificultades y aprendizajes identificados durante el cierre del proyecto SICST.

También registra la distribución real del trabajo realizado por los integrantes
activos durante la etapa final, diferenciando las contribuciones del cierre de
los aportes históricos conservados en el repositorio.

La información presentada se basa en artefactos versionados, historial de Git,
capturas, grabaciones, bitácoras, archivos de análisis y documentos disponibles
en el repositorio.

---

## Qué funcionó bien

La organización progresiva de las evidencias permitió consolidar en el
repositorio:

* transcripciones anonimizadas;
* consentimientos y evidencias restringidas;
* notas contemporáneas y síntesis retrospectivas;
* resultados del cuestionario;
* archivos de trazabilidad;
* requisitos funcionales y no funcionales;
* documentación del componente de inteligencia artificial;
* fuentes editables de diagramas;
* resultados experimentales;
* documentación técnica y de autoría.

También se estableció una cadena reproducible de análisis desde los datos fuente
hasta los resultados procesados. Los scripts versionados permiten regenerar
tablas, estadísticas, resultados de acuerdo entre codificadores y otros
productos derivados.

La integración entre la ERS, la matriz de trazabilidad y los requisitos del
componente inteligente permitió mantener correspondencia entre requisitos,
riesgos, métricas, responsables y métodos de verificación.

El manuscrito se conservó en formato LaTeX junto con su bibliografía, tablas,
figuras y archivos reproducibles. Esto facilitó identificar diferencias entre
las afirmaciones del documento y las evidencias reales del repositorio.

Las grabaciones de sesiones de trabajo, las capturas individuales y el historial
de Git permitieron acreditar la participación de los integrantes activos durante
la etapa de cierre.

---

## Correcciones realizadas durante el cierre

### Cronología del registro OSF

Durante la revisión final se identificó que la cronología documentada
inicialmente sobre el registro OSF no era correcta.

El registro OSF con DOI `10.17605/OSF.IO/82Q76` fue realizado el 12/09/2026 a
las 19:50, hora de Ecuador continental.

Las entrevistas de campo ya habían sido realizadas antes de esa fecha. Además,
los metadatos internos de las cuatro hojas de evaluación ciega registran
guardados realizados el 12/09/2026 entre las 13:11 y las 13:16, hora de
Ecuador. Estas hojas ya contenían los 66 requisitos evaluados, incluidos los 33
requisitos generados mediante LLM.

Por tanto, el conjunto de requisitos generado mediante LLM y las calificaciones
de la evaluación ciega ya existían antes del registro OSF.

La hora exacta en que se generó el conjunto LLM no quedó documentada de manera
independiente. Por esta razón, no se asigna ni se inventa una hora exacta. La
evidencia permite afirmar únicamente que dicho conjunto ya existía antes de los
primeros guardados de las hojas de evaluación ciega.

En consecuencia, el registro OSF se reconoce como **retrospectivo tanto
respecto de la recolección de campo como del experimento comparativo y de las
calificaciones ciegas**.

El análisis se presenta como exploratorio y no como una prueba confirmatoria
completamente preregistrada. Esta limitación debe mantenerse expresamente en el
README del registro, la ficha del prompt, la documentación del experimento, el
manuscrito y su sección de amenazas a la validez.

### Notas de campo

Durante el cierre también se corrigió la clasificación de las notas de campo.

La colección contiene:

```text
Notas contemporáneas:       8
Síntesis retrospectivas:   22
Total de archivos:         30
```

Las 8 notas contemporáneas corresponden a sesiones realizadas el 17/06/2026.

Para las otras 22 sesiones no se conserva una nota escrita durante la sesión
original. Las hojas correspondientes fueron elaboradas el 17/09/2026 a partir
de las transcripciones conservadas y se identifican expresamente como síntesis
retrospectivas.

Estas síntesis no se presentan como notas tomadas durante las sesiones de julio
o agosto. La bitácora de elicitación fue actualizada para reconocer la ausencia
de una nota contemporánea en esas 22 sesiones.

### Coherencia numérica del manuscrito

Se revisó la coherencia numérica del análisis experimental.

El análisis principal utiliza 11 pares con correspondencia temática estricta,
equivalentes a 22 de los 66 requisitos evaluados. Los otros 44 requisitos se
mantienen en el conjunto de datos y en la matriz de trazabilidad, pero no forman
parte de la comparación pareada principal porque no poseen una correspondencia
uno a uno suficientemente estricta.

También se comprobó la correspondencia entre los resultados reportados y los
archivos generados por la cadena reproducible, incluyendo:

* acuerdo entre evaluadores;
* acuerdo entre codificadores;
* resultados del cuestionario;
* perfiles de participantes;
* aceptación del uso de cámara;
* visualización del avance;
* saturación temática;
* comparación pareada humano–LLM.

La versión PDF definitiva del manuscrito debe recompilarse después de incorporar
todas las correcciones de cronología, amenazas a la validez, contribuciones y
referencias citadas.

### Composición final del equipo

Durante el semestre, Morán Pilaguano Frixon Fernando y Viteri García Jonathan
Enrique dejaron de formar parte del equipo y no participaron en la etapa final
del examen suspenso.

La entrega final y el proceso de cierre fueron desarrollados por:

* Zambrano Moya Angelo Paul;
* Contreras Chávez Kevin Germán.

Los aportes históricos de los integrantes que dejaron el equipo se conservan en
el historial de Git y en los artefactos correspondientes. No se eliminan, se
modifican ni se reasignan a los integrantes activos.

---

## Distribución de aportes durante el cierre

### Angelo Paul Zambrano Moya

Durante la etapa de cierre, Angelo Zambrano realizó y coordinó actividades
relacionadas con:

* coordinación general de las correcciones del repositorio;
* registro y documentación del experimento comparativo en OSF;
* revisión de la cronología del registro OSF;
* generación y documentación del conjunto de requisitos mediante LLM;
* coordinación documental de la evaluación ciega;
* análisis estadístico de los resultados humano–LLM;
* actualización de la cadena reproducible de análisis en `07_Datos/`;
* comprobación de los resultados generados por los scripts;
* actualización de requisitos, métricas y documentación del componente de IA;
* revisión y actualización del manuscrito en LaTeX;
* verificación de la correspondencia entre el manuscrito y los resultados;
* revisión de la retrospectiva y documentación de cierre;
* organización general de los entregables y de la línea base;
* participación en las dos sesiones grabadas de revisión.

Estas actividades pueden verificarse mediante el historial de Git, los archivos
del experimento, los resultados reproducibles, el manuscrito y las evidencias
contenidas en `10_Autoria/`.

### Kevin Germán Contreras Chávez

Durante la etapa de cierre, Kevin Contreras realizó y participó en actividades
relacionadas con:

* incorporación y organización de evidencia de campo;
* participación como coentrevistador en sesiones remotas de recolección de
  información;
* organización de transcripciones, consentimientos y materiales relacionados
  con entrevistas y walkthroughs;
* incorporación de fuentes editables Draw.io para los diagramas del proyecto;
* organización y normalización de las notas de campo;
* elaboración durante el cierre de las 22 síntesis retrospectivas basadas en
  transcripciones existentes;
* actualización de la bitácora de elicitación para distinguir las 8 notas
  contemporáneas de las 22 síntesis retrospectivas;
* organización y normalización de archivos de correspondencia;
* actualización del inventario EXIF y de los hashes de evidencias;
* incorporación de capturas individuales de autoría;
* actualización de la bitácora de sesiones del cierre;
* revisión de `.mailmap` para consolidar sus identidades históricas de Git;
* revisión de documentos y README de `10_Autoria/`;
* participación en la retrospectiva y en la verificación final del repositorio;
* participación en las dos sesiones grabadas de trabajo.

Las síntesis retrospectivas elaboradas durante el cierre no se presentan como
notas tomadas durante las fechas originales de las sesiones. Su elaboración se
reconoce expresamente como una actividad posterior basada en las transcripciones
conservadas.

### Trabajo conjunto

Angelo Zambrano y Kevin Contreras participaron conjuntamente en:

* revisión de la estructura final del repositorio;
* comprobación de evidencias de autoría;
* revisión de requisitos y documentación técnica;
* verificación de notas de campo y transcripciones;
* revisión de la matriz de trazabilidad;
* comprobación del paquete de datos reproducible;
* revisión del manuscrito y de sus resultados;
* revisión de requisitos del componente inteligente;
* verificación de las observaciones realizadas por el docente;
* revisión de los pendientes antes de establecer la línea base final;
* dos sesiones grabadas de trabajo y revisión.

La distribución anterior no implica que ambos integrantes hayan realizado todas
las actividades en la misma proporción. Cada contribución se mantiene asociada
con la persona y los artefactos que permiten verificarla.

---

## Dificultades encontradas

Una de las principales dificultades fue consolidar evidencia producida en
diferentes momentos del semestre y verificar que cada archivo tuviera una
ubicación, identificación y relación clara con el proceso de Ingeniería de
Requisitos.

También fue necesario diferenciar entre evidencia contemporánea y documentación
elaborada durante el cierre. Esta situación se presentó especialmente con las
22 síntesis retrospectivas, que inicialmente se contabilizaron de la misma forma
que las notas tomadas durante las sesiones.

La revisión de metadatos de las hojas de evaluación ciega mostró que la
cronología descrita inicialmente no coincidía con la evidencia digital. Esto
obligó a reconocer el carácter retrospectivo del registro OSF respecto del
experimento y a revisar las afirmaciones metodológicas del manuscrito.

Las cuatro hojas de evaluación ciega registran el mismo último editor y tiempos
de guardado muy próximos. Estos metadatos no demuestran quién introdujo las
calificaciones, pero hacen necesario documentar de manera separada cómo recibió,
organizó y conservó el equipo cada archivo. Cuando no exista evidencia
suficiente sobre algún paso, la limitación debe reconocerse sin crear
explicaciones ficticias.

También fue necesario corregir referencias y documentación después de los
cambios de nombre y de propiedad del repositorio. Esto demostró la importancia
de realizar una revisión global de URL, rutas y nombres antes de establecer una
línea base.

El manejo de archivos multimedia de gran tamaño requirió separar la evidencia
restringida del contenido público y utilizar mecanismos de distribución,
cifrado y verificación mediante SHA-256.

La transferencia de la propiedad del repositorio a la cuenta del docente obligó
a revisar las URL públicas. La transferencia no modificó la autoría histórica:
cambiar el propietario del repositorio no cambia quién realizó cada commit.

---

## Lecciones aprendidas

Para futuras entregas se debe definir desde el inicio una estructura estable de
carpetas, convenciones de nombres y mecanismos de trazabilidad.

Las notas de campo deben registrarse durante o inmediatamente después de cada
sesión. Si se prepara posteriormente una síntesis a partir de una transcripción,
debe identificarse desde su creación como retrospectiva.

Los registros externos, protocolos y decisiones metodológicas deben conservar
su fecha exacta y un alcance explícito. Un registro creado después de que los
datos o las evaluaciones ya existen no debe presentarse como un preregistro
confirmatorio.

Las fechas escritas en los documentos deben contrastarse con los metadatos
internos, el historial de Git y demás evidencias digitales antes de realizar
afirmaciones sobre la cronología.

La reproducibilidad no depende únicamente de conservar los datos. También
requiere mantener scripts, diccionarios, resultados derivados, bibliografía,
versiones del manuscrito y mecanismos de verificación consistentes entre sí.

Incluir una referencia en un archivo `.bib` no significa que haya sido utilizada
en el manuscrito. Las fuentes relevantes deben citarse dentro del texto y
relacionarse con las afirmaciones que respaldan.

La distribución del trabajo debe documentarse durante el desarrollo y no
solamente al final. Las bitácoras, commits, capturas y grabaciones facilitan
acreditar la participación individual.

Una línea base o etiqueta debe crearse únicamente después de completar todas
las correcciones, recompilar los documentos finales y regenerar los
manifiestos. Una etiqueta histórica no debe moverse para incluir cambios
posteriores.

---

## Estado de las acciones antes de la nueva línea base final

Estado actual antes de establecer la nueva etiqueta de cierre:

1. **Hecho:** corregida la cronología OSF en los archivos relacionados;
2. **Hecho:** actualizadas las amenazas a la validez del manuscrito;
3. **Hecho:** ampliadas las referencias realmente citadas en el manuscrito;
4. **Hecho:** recompilado el PDF desde la fuente LaTeX corregida;
5. **Hecho:** documentada la procedencia y el manejo de las evaluaciones ciegas;
6. **Hecho:** regenerados los manifiestos y checksums de cierre;
7. **Hecho:** comprobado que el repositorio no contiene afirmaciones contradictorias activas; las menciones históricas conservadas están identificadas explícitamente como correcciones.
8. **Pendiente de cierre:** crear una nueva etiqueta anotada sin modificar `v2.0-entrega4`.

---

## Cierre

El proceso de revisión permitió mejorar la transparencia de la evidencia, la
trazabilidad de los aportes y la coherencia entre los datos, los requisitos, el
análisis y la publicación.

La retrospectiva reconoce tanto los logros del proyecto como las limitaciones
documentales y metodológicas identificadas durante el cierre. Las correcciones
posteriores deben conservarse mediante commits verificables y formar parte de
una nueva línea base anotada.

Los aportes se mantienen asociados con sus autores reales y no se presentan
como contemporáneas evidencias elaboradas posteriormente. De esta manera, el
repositorio conserva su integridad académica y permite que las decisiones,
resultados y responsabilidades puedan ser revisados de forma transparente.
