# Declaración corregida de desviaciones y decisiones posteriores al registro OSF

**Proyecto:** Sistema Inteligente de Control y Seguimiento de Terapia Física (SICST)  
**Registro OSF:** DOI `10.17605/OSF.IO/82Q76`  
**Fecha de registro:** 2026-09-13 00:50:38 UTC / 2026-09-12 19:50:38, hora de Ecuador continental (UTC-5)  
**Fecha de esta corrección:** 2026-09-18

## 1. Propósito de esta declaración

Este documento corrige la interpretación cronológica presentada en una versión anterior de `osf_deviations.pdf`. La evidencia versionada del repositorio muestra que el registro OSF no precedió a la generación del conjunto de requisitos mediante LLM ni a las cuatro evaluaciones ciegas utilizadas posteriormente en el análisis.

El registro OSF se conserva sin alteraciones como evidencia histórica. La corrección consiste en describir de forma transparente la cronología real y el carácter exploratorio del análisis.

## 2. Cronología reconstruida

La secuencia documentada es la siguiente:

1. Se realizaron las entrevistas de campo y la elicitación de requisitos del ERS.
2. Se generó el conjunto de requisitos funcionales mediante GPT-5.5-mini a partir del corpus anonimizado. La hora exacta de generación no fue preservada, pero debió ocurrir antes de las 13:11 del 12/09/2026, hora de Ecuador, porque las hojas de evaluación ya comenzaron a guardarse a esa hora.
3. Se realizaron las cuatro evaluaciones ciegas. Los metadatos de las hojas XLSX sitúan sus guardados aproximadamente entre las 13:11 y 13:16 del 12/09/2026, hora de Ecuador.
4. El protocolo se registró en OSF el 12/09/2026 a las 19:50:38, hora de Ecuador.
5. El análisis estadístico y la documentación final se realizaron posteriormente.

Por tanto, el registro OSF es retrospectivo respecto de las entrevistas, la generación del conjunto LLM y las cuatro evaluaciones ciegas.

## 3. Alcance del registro OSF

El registro OSF describió de forma general la comparación entre requisitos funcionales humanos y requisitos generados por LLM, el uso de una rúbrica de cinco dimensiones, el análisis descriptivo, el acuerdo entre evaluadores y una comparación estadística entre ambas condiciones.

Sin embargo, el registro no fijó de forma prospectiva todos los detalles operativos del análisis que finalmente se ejecutaron. Por ello, no se presenta como una prerregistración confirmatoria del experimento y las comparaciones inferenciales se interpretan como exploratorias.

## 4. Operacionalizaciones estadísticas posteriores al registro

El análisis reproducible actual utiliza las siguientes decisiones operativas:

- 33 requisitos funcionales humanos y 33 requisitos funcionales generados por LLM para descriptivos y acuerdo entre evaluadores.
- 11 pares temáticos estrictos como unidad efectiva para la comparación pareada.
- Prueba de Shapiro-Wilk sobre las diferencias dentro de cada par.
- Prueba t de Student apareada cuando corresponde y prueba de Wilcoxon de rangos con signo cuando corresponde.
- Corrección de Holm-Bonferroni sobre las cinco dimensiones principales.
- Diferencia media humano - LLM e intervalos bootstrap del 95 %.
- Cohen's dz como tamaño del efecto pareado, también con intervalo bootstrap del 95 %.
- Kappa de Fleiss para el acuerdo entre los cuatro evaluadores sobre los 66 ítems.

Estas decisiones no deben describirse como si hubieran sido fijadas prospectivamente antes de que existieran los datos experimentales.

## 5. Procedencia de las evaluaciones ciegas

Las cuatro evaluaciones fueron realizadas por Mishell, Angel, Dayana y Sebas. Cada participante completó su propia hoja y calificó los ítems sin disponer de la columna que revelaba si cada requisito provenía del proceso humano o del LLM.

Las hojas se completaron durante una misma sesión y de forma secuencial utilizando el mismo computador. Antes de pasar al siguiente evaluador se verificó únicamente que la hoja estuviera completa y se guardó el archivo correspondiente. De acuerdo con el procedimiento documentado, las puntuaciones anteriores no se mostraron al siguiente participante.

El uso de una misma sesión y un mismo equipo constituye una limitación metodológica. No se presenta esta configuración como evidencia de independencia experimental entre evaluadores. El hecho de que los archivos compartan metadatos de última edición asociados al mismo equipo tampoco permite, por sí solo, identificar a la persona que introdujo cada puntuación.

## 6. Resultados e interpretación

El acuerdo entre evaluadores fue bajo o nulo según la dimensión, con valores de kappa de Fleiss aproximadamente entre -0.013 y 0.167.

En los 11 pares temáticos estrictos, ninguna de las cinco dimensiones mostró una diferencia estadísticamente significativa después de la corrección de Holm-Bonferroni. Dado el tamaño reducido de la muestra pareada, el bajo acuerdo interevaluador y el carácter retrospectivo del registro OSF, estos resultados se interpretan como exploratorios e inconclusos, no como evidencia confirmatoria de equivalencia entre ambos procedimientos de generación de requisitos.

## 7. Corrección respecto de la versión anterior

La versión anterior de `osf_deviations.pdf` contenía afirmaciones que ya no se consideran correctas, entre ellas:

- que el protocolo había sido prerregistrado antes de generar el conjunto LLM y antes de recopilar las evaluaciones ciegas;
- que el análisis principal utilizaba pruebas para muestras independientes;
- que las reglas estadísticas específicas habían sido definidas prospectivamente antes de observar los resultados;
- que no existían desviaciones sustantivas respecto del registro.

Esta versión sustituye esas afirmaciones por una descripción consistente con la evidencia temporal del repositorio y con el análisis reproducible actual.

## 8. Conclusión

El registro OSF se mantiene como parte de la trazabilidad del proyecto, pero se documenta correctamente como un registro retrospectivo del protocolo. Las decisiones estadísticas específicas que no quedaron fijadas prospectivamente se presentan como operacionalizaciones posteriores, y los resultados inferenciales se interpretan como exploratorios.
