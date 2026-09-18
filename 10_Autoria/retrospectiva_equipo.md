# Retrospectiva del equipo — Cierre del proyecto SICST

**Fecha:** 2026-09-18  
**Proyecto:** Sistema Inteligente de Control y Seguimiento de Terapia Física (SICST)  
**Asignatura:** Ingeniería de Requisitos — ISR-401

## Propósito

Esta retrospectiva documenta las principales decisiones, correcciones y aprendizajes realizados durante el cierre del proyecto, después de la revisión de la evidencia, los datos, la trazabilidad, la documentación del experimento y el manuscrito final.

## Qué funcionó bien

La organización progresiva de las evidencias permitió consolidar en el repositorio las transcripciones, notas contemporáneas disponibles, síntesis retrospectivas, resultados del cuestionario, archivos de trazabilidad y documentación técnica.

También se logró establecer una cadena reproducible de análisis desde los datos fuente hasta los resultados procesados, manteniendo scripts, datos derivados y documentación asociada.

La integración entre la ERS, los requisitos relacionados con inteligencia artificial y la matriz de trazabilidad permitió conservar correspondencia entre requisitos, riesgos, métricas y métodos de verificación.

El manuscrito final se mantuvo versionado en LaTeX, lo que permitió conservar una fuente reproducible y mantener correspondencia entre el documento, los resultados y los archivos de datos del proyecto.

## Correcciones realizadas durante el cierre

Durante la revisión final se aclaró la cronología real del registro OSF.

Las entrevistas de campo, la generación del conjunto de requisitos mediante LLM y las cuatro evaluaciones ciegas utilizadas posteriormente en el análisis ya se habían realizado antes de la marca temporal del registro OSF del 12/09/2026 a las 19:50 hora Ecuador.

Por esta razón, el registro OSF se documenta como retrospectivo respecto de esas fases. En consecuencia, el análisis comparativo entre requisitos humanos y requisitos generados mediante LLM se presenta como exploratorio y no como un estudio confirmatorio preregistrado.

La documentación fue corregida para eliminar afirmaciones anteriores que indicaban erróneamente que la generación del conjunto LLM y las evaluaciones ciegas habían ocurrido después del registro OSF. Los artefactos históricos y sus metadatos se conservan sin retrofechar ni modificar para aparentar una cronología diferente.

También se revisó la coherencia numérica del manuscrito. El análisis principal utiliza 11 pares estrictamente emparejados, equivalentes a 22 de los 66 ítems evaluados; por lo tanto, los 44 ítems restantes quedan fuera de la comparación pareada principal.

Se revisó además la documentación de las notas de campo. Se distinguieron las notas contemporáneas existentes de las 22 síntesis retrospectivas elaboradas posteriormente a partir de transcripciones de sesiones de julio y agosto. Estas síntesis no se presentan como notas tomadas durante las sesiones originales.

Se incorporaron y revisaron resultados cuantitativos y cualitativos reproducibles, incluyendo información de perfiles, aceptación del uso de cámara, visualización del avance, acuerdo entre codificadores y saturación temática.

La documentación del cierre se revisó para mantener consistencia entre las afirmaciones realizadas, los archivos presentes en el repositorio y la evidencia que puede verificarse directamente.

## Distribución de aportes en el cierre

Durante la etapa final del proyecto, las responsabilidades documentadas se distribuyeron de la siguiente manera:

- **Angelo Paul Zambrano Moya:** estuvo a cargo de la formalización y documentación retrospectiva del protocolo experimental en OSF, la generación del conjunto de requisitos mediante LLM, la coordinación de la evaluación ciega y el análisis estadístico de los resultados. También participó en la revisión de la trazabilidad, la documentación metodológica y el cierre general del repositorio.

- **Kevin Germán Contreras Chávez:** participó como coentrevistador en sesiones de recolección de información de campo realizadas de forma remota, contribuyendo a la obtención de evidencia utilizada posteriormente en la elicitación y análisis de requisitos. Durante la fase de cierre del 16 y 17 de septiembre de 2026, con 64 commits registrados, fue responsable de elaborar 22 síntesis retrospectivas a partir de las transcripciones de sesiones realizadas en julio y agosto, para las cuales no existía una nota manuscrita contemporánea; gestionar la correspondencia del equipo; completar el inventario EXIF de las fotografías; ejecutar la lista de verificación previa a la entrega; depositar sus propias capturas de evidencia individual; y grabar, junto con Angelo, las dos sesiones de trabajo documentadas en `10_Autoria/grabaciones/`.

- **Trabajo conjunto:** ambos integrantes revisaron el manuscrito final y participaron en la comprobación de que los resultados, evidencias y afirmaciones incluidas en la entrega correspondieran a información real y trazable dentro del repositorio.

Los aportes históricos de integrantes que dejaron de formar parte del equipo se mantienen en el historial de Git y en los artefactos correspondientes, sin reasignar ni atribuir esas contribuciones a los integrantes finales.

## Dificultades encontradas

Una de las principales dificultades fue consolidar evidencia producida en distintos momentos del semestre y verificar que cada archivo tuviera una ubicación, identificación y relación clara con el proceso de Ingeniería de Requisitos.

También fue necesario corregir afirmaciones relacionadas con la cronología del experimento después de comparar la documentación escrita con las marcas temporales disponibles en los archivos y en el registro OSF.

La revisión mostró la importancia de distinguir entre un preregistro realizado antes de la obtención de los datos experimentales y un registro retrospectivo realizado cuando parte de esos datos ya existía.

Otra dificultad consistió en organizar evidencia de campo generada en momentos distintos. En particular, para varias sesiones de julio y agosto no se conservaba una nota manuscrita contemporánea y posteriormente se elaboraron síntesis a partir de las transcripciones. Fue necesario documentar expresamente esta diferencia para no presentar esas síntesis como evidencia contemporánea.

También fue necesario corregir referencias y documentación después del cambio de nombre y de propiedad del repositorio. Esto mostró la importancia de realizar una revisión global de URLs, rutas y archivos de verificación antes de establecer una línea base final.

El manejo de archivos multimedia de gran tamaño requirió separar la evidencia restringida del contenido normal del repositorio y utilizar mecanismos de distribución y verificación mediante checksum.

La transferencia de la propiedad del repositorio a la cuenta del docente obligó a revisar de forma global las URL públicas. Se mantuvo intacta la autoría histórica: cambiar el propietario del repositorio no cambia quién realizó cada commit.

## Lecciones aprendidas

Para futuras entregas, es conveniente definir desde el inicio una estructura estable de carpetas, convenciones de nombres y mecanismos de trazabilidad.

Si se pretende declarar un experimento como preregistrado, el registro debe realizarse antes de generar los datos experimentales o recolectar las evaluaciones que posteriormente serán analizadas.

Cuando un registro se realiza después de que parte de los datos ya existe, debe indicarse claramente su carácter retrospectivo y evitar presentar los análisis como confirmatorios preregistrados.

Las notas tomadas durante una sesión y las síntesis elaboradas posteriormente a partir de una transcripción son tipos de evidencia diferentes y deben identificarse como tales.

Los registros externos, protocolos y decisiones metodológicas deben documentarse con su fecha exacta y con un alcance explícito para evitar interpretaciones incorrectas sobre la cronología de la investigación.

La reproducibilidad no depende únicamente de conservar los datos, sino también de mantener scripts, diccionarios, resultados derivados, versiones del manuscrito y mecanismos de verificación consistentes entre sí.

También se comprobó que una línea base o tag debe crearse únicamente después de completar todas las correcciones finales, de manera que represente exactamente el estado entregado.

## Cierre

El proceso de revisión final permitió mejorar la coherencia entre evidencia, requisitos, análisis y publicación.

Las correcciones metodológicas realizadas no modifican retrospectivamente los artefactos originales, sino que aclaran su procedencia, su cronología y las limitaciones de la evidencia disponible.

El cierre del proyecto busca que las afirmaciones contenidas en la documentación puedan contrastarse con archivos, metadatos, historial de Git y demás evidencia conservada en el repositorio.
