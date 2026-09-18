# Retrospectiva del equipo — Cierre del proyecto SICST

**Fecha:** 2026-09-18  
**Proyecto:** Sistema Inteligente de Control y Seguimiento de Terapia Física (SICST)  
**Asignatura:** Ingeniería de Requisitos — ISR-401

## Propósito

Esta retrospectiva documenta las principales decisiones, correcciones y aprendizajes realizados durante el cierre del proyecto, después de la revisión de la evidencia, los datos, la trazabilidad y el manuscrito final.

## Qué funcionó bien

La organización progresiva de las evidencias permitió consolidar en el repositorio las transcripciones, notas de campo, resultados del cuestionario, archivos de trazabilidad y documentación técnica. También se logró establecer una cadena reproducible de análisis desde los datos fuente hasta los resultados procesados.

La integración entre la ERS, los requisitos relacionados con inteligencia artificial y la matriz de trazabilidad permitió conservar correspondencia entre requisitos, riesgos, métricas y métodos de verificación.

El manuscrito final se mantuvo versionado en LaTeX y se generó nuevamente el PDF a partir de la versión actualizada del archivo fuente, manteniendo consistencia entre los resultados reportados y los archivos reproducibles del proyecto.

## Correcciones realizadas durante el cierre

Durante la revisión final se aclaró la cronología del registro OSF. Las entrevistas de campo fueron realizadas antes del registro, por lo que el análisis comparativo entre requisitos humanos y generados con LLM se presenta como exploratorio y no como un estudio confirmatorio completamente preregistrado.

También se revisó la coherencia numérica del manuscrito. El análisis principal utiliza 11 pares estrictamente emparejados, equivalentes a 22 de los 66 ítems evaluados; por lo tanto, los 44 ítems restantes quedan fuera de la comparación pareada principal.

Se incorporaron al manuscrito los resultados cuantitativos y cualitativos reproducibles, incluyendo información de perfiles, aceptación del uso de cámara, visualización del avance, acuerdo entre codificadores y saturación temática.

Finalmente, el PDF del manuscrito fue recompilado desde el archivo LaTeX actualizado para evitar diferencias entre la fuente versionada y el documento entregable.

## Distribución de aportes en el cierre

Durante la etapa final del proyecto, las responsabilidades documentadas se distribuyeron de la siguiente manera:

- **Angelo Paul Zambrano Moya:** estuvo a cargo del registro y documentación del experimento comparativo en OSF, la generación del conjunto de requisitos mediante LLM, la coordinación de la evaluación ciega y el análisis estadístico de los resultados.

- **Kevin Germán Contreras Chávez:** participó como coentrevistador en sesiones de recolección de información de campo realizadas de forma remota, contribuyendo a la obtención de evidencia utilizada posteriormente en la elicitación y análisis de requisitos.

- **Trabajo conjunto:** ambos integrantes revisaron el manuscrito final y participaron en la comprobación de que los resultados, evidencias y afirmaciones incluidas en la entrega correspondieran a información real y trazable dentro del repositorio.

Los aportes históricos de integrantes que dejaron de formar parte del equipo se mantienen en el historial de Git y en los artefactos correspondientes, sin reasignar ni atribuir esas contribuciones a los integrantes finales.

## Dificultades encontradas

Una de las principales dificultades fue consolidar evidencia producida en distintos momentos del semestre y verificar que cada archivo tuviera una ubicación, identificación y relación clara con el proceso de Ingeniería de Requisitos.

También fue necesario corregir referencias y documentación después del cambio de nombre del repositorio. Esto mostró la importancia de realizar una revisión global de URLs, rutas y archivos de verificación antes de establecer una línea base final.

El manejo de archivos multimedia de gran tamaño requirió separar la evidencia restringida del contenido normal del repositorio y utilizar mecanismos de distribución y verificación mediante checksum.

La transferencia de la propiedad del repositorio a la cuenta del docente
obligó a revisar de forma global las URL públicas. Se mantuvo intacta la
autoría histórica: cambiar el propietario del repositorio no cambia quién
realizó cada commit.

## Lecciones aprendidas

Para futuras entregas, es conveniente definir desde el inicio una estructura estable de carpetas, convenciones de nombres y mecanismos de trazabilidad.

Los registros externos, protocolos y decisiones metodológicas deben documentarse con su fecha exacta y con un alcance explícito para evitar interpretaciones incorrectas sobre la cronología de la investigación.

La reproducibilidad no depende únicamente de conservar los datos, sino también de mantener scripts, diccionarios, resultados derivados, versiones del manuscrito y mecanismos de verificación consistentes entre sí.

También se comprobó que una línea base o tag debe crearse únicamente después de completar todas las correcciones finales, de manera que represente exactamente el estado entregado.

## Cierre

El proceso de revisión final permitió mejorar la coherencia entre evidencia, requisitos, análisis y publicación. Las correcciones realizadas quedaron integradas en archivos versionados dentro del repositorio y forman parte del estado de cierre del proyecto SICST.
