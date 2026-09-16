# Plan de monitoreo posterior al despliegue de los componentes inteligentes del SICST

**Proyecto:** Sistema Inteligente de Control y Seguimiento de Terapia Física (SICST)  
**Versión:** 1.0  
**Fecha:** 2026-09-16

## 1. Estado y alcance

Este documento define el monitoreo previsto para IA-01 e IA-02.

**El sistema no se declara desplegado en producción en este documento.** Por tanto, no se presentan valores operativos inventados ni ciclos de monitoreo ficticios. Las frecuencias que indican “en producción” comienzan únicamente cuando exista un despliegue real.

Antes del despliegue se aplican las verificaciones por versión, release o reentrenamiento establecidas en `requisitos_no_funcionales_ia.csv`.

## 2. Principios del monitoreo

Cada indicador debe tener:

- requisito asociado;
- métrica y unidad;
- umbral;
- periodicidad;
- responsable;
- acción cuando el umbral no se cumple.

Un valor sin acción definida no cierra el control.  
Un ciclo no ejecutado debe quedar explícitamente documentado cuando exista operación real.

## 3. Indicadores

| Código | RNF-IA | Indicador | Umbral | Periodicidad | Responsable | Acción al incumplirse |
|---|---|---|---|---|---|---|
| MP-01 | RNF-IA1-P01 | Latencia extremo a extremo p95 | <= 2 s | Por release; mensual en producción | Equipo de desarrollo (responsable técnico del componente IA) | Marcar salida como no confiable y continuar con revisión/flujo manual. |
| MP-02 | RNF-IA1-P02 | F1 de detección postural | >= 0.85 | Por versión/reentrenamiento; auditoría mensual en producción | Equipo de desarrollo, con validación clínica del fisioterapeuta responsable | No presentar corrección como definitiva; derivar al fisioterapeuta. |
| MP-03 | RNF-IA1-P03 | MAE del conteo de repeticiones | <= 1 repetición por serie | Por versión/reentrenamiento; auditoría mensual en producción | Equipo de desarrollo, con validación clínica del fisioterapeuta responsable | Marcar conteo como pendiente y permitir corrección manual. |
| MP-04 | RNF-IA1-EQ01 | Brecha absoluta de F1 por edad | <= 0.05 | Por reentrenamiento; trimestral en producción | Equipo de desarrollo, con revisión clínica del fisioterapeuta responsable | Analizar la brecha antes de aprobar el release; revisión humana de casos afectados. |
| MP-05 | RNF-IA1-EQ02 | Brecha absoluta de recall por limitación de movilidad | <= 0.05 | Por reentrenamiento; trimestral en producción | Equipo de desarrollo, con revisión clínica del fisioterapeuta responsable | Revisar el grupo afectado y no aprobar el release sin análisis. |
| MP-06 | RNF-IA1-XAI01 | Longitud/latencia/claridad de explicación | <= 60 palabras; <= 2 s; claridad >= 4/5 | Por release mayor; semestral en producción | Equipo de desarrollo, con evaluación del fisioterapeuta y pacientes participantes | Derivar la corrección a revisión humana si la explicación no cumple. |
| MP-07 | RNF-IA2-P01 | Precisión de alertas prioritarias | >= 0.80 | Por actualización; mensual en producción | Equipo de desarrollo, con validación clínica del fisioterapeuta responsable | No usar la priorización automática como criterio de decisión hasta corregir. |
| MP-08 | RNF-IA2-P02 | Recall de alertas prioritarias | >= 0.80 | Por actualización; mensual en producción | Equipo de desarrollo, con validación clínica del fisioterapeuta responsable | No usar la priorización como filtro exclusivo; reforzar revisión manual. |
| MP-09 | RNF-IA2-P03 | Latencia p95 de priorización | <= 1 s | Por release; mensual en producción | Equipo de desarrollo (responsable técnico del componente IA) | Mostrar estado degradado y continuar con revisión manual. |
| MP-10 | RNF-IA2-EQ01 | Brecha absoluta de TPR por edad | <= 0.05 | Por reentrenamiento; trimestral en producción | Equipo de desarrollo, con revisión clínica del fisioterapeuta responsable | Analizar la brecha antes del release y revisar casos límite. |
| MP-11 | RNF-IA2-EQ02 | Brecha absoluta de FPR por gravedad | <= 0.05 | Por reentrenamiento; trimestral en producción | Equipo de desarrollo, con revisión clínica del fisioterapeuta responsable | Revisar falsas alertas por grupo y corregir antes de aprobar. |
| MP-12 | RNF-IA2-XAI01 | Factores/longitud/latencia/claridad de explicación | <= 3 factores; <= 60 palabras; <= 2 s; claridad >= 4/5 | Por release mayor; semestral en producción | Equipo de desarrollo, con evaluación del fisioterapeuta responsable | Presentar la alerta para revisión manual si la explicación no cumple. |

## 4. Flujo ante una alerta de monitoreo

Cuando una medición incumpla su umbral:

1. registrar fecha, requisito, valor medido y evidencia de cálculo;
2. marcar el componente o salida como degradado cuando corresponda;
3. activar la supervisión manual definida por el RNF-IA;
4. abrir una incidencia con causa preliminar;
5. revisar datos, modelo, interfaz o entorno según la métrica afectada;
6. repetir la verificación completa antes de aprobar un nuevo release;
7. conservar el resultado anterior y el nuevo para mantener trazabilidad.

## 5. Formato del registro operativo futuro

Cuando exista despliegue real, cada ciclo deberá poder representarse con al menos los siguientes campos:

```text
fecha,indicador,requisito,valor,unidad,umbral,cumple,responsable,evidencia,accion,observaciones
```

**No se crea aquí un CSV vacío de monitoreo**, porque un archivo vacío podría confundirse con evidencia de una medición inexistente. El registro se inicia con el primer ciclo real.

## 6. Línea base

La “línea base” utilizada para comparar degradación debe ser el resultado de la última validación aprobada del componente correspondiente. No debe reutilizarse el experimento humano–LLM de `06_Experimento` o `07_Datos` como línea base del desempeño del componente de visión, porque son objetos de evaluación diferentes.

La línea base debe conservar:

- versión del modelo o módulo;
- versión del conjunto de prueba;
- fecha de validación;
- métricas globales;
- métricas por grupo cuando aplique;
- responsable de la validación.

## 7. Equidad

Las métricas agregadas no sustituyen las métricas por grupo.

Se vigilan explícitamente:

- F1 por edad para IA-01;
- recall por nivel de limitación para IA-01;
- TPR por edad para IA-02;
- FPR por gravedad para IA-02.

Cuando una brecha supera `0.05`, el resultado global no se usa para justificar el release sin analizar el grupo afectado.

## 8. Supervisión humana y fallback

Mientras el SICST opere como apoyo clínico no autónomo:

- el fisioterapeuta conserva la decisión final;
- una corrección postural no confiable se deriva a revisión humana;
- un conteo dudoso puede corregirse manualmente;
- una priorización que no cumple precisión/recall no se usa como filtro exclusivo;
- una alerta sigue siendo revisable y descartable por el fisioterapeuta;
- una explicación insuficiente no debe presentarse como justificación definitiva.

## 9. Revisión del plan

Este plan se revisa cuando:

- se incorpora un nuevo componente de IA;
- cambia un umbral;
- cambia la población objetivo;
- se modifica la autonomía del sistema;
- se cambia el modelo o la fuente de datos;
- la clasificación interna de riesgo cambia;
- se identifica un modo de fallo no cubierto por los indicadores actuales.

## Convención del campo responsable

En este plan, **responsable** identifica al rol que debe ejecutar, controlar o validar la medición; no equivale necesariamente al usuario que recibe la salida del sistema. El **equipo de desarrollo** ejecuta las mediciones técnicas y mantiene la instrumentación. El **fisioterapeuta responsable** aporta la validación clínica y conserva la decisión profesional final. Los **pacientes participantes** pueden intervenir en pruebas de comprensión o claridad, pero no son responsables técnicos de las métricas.

