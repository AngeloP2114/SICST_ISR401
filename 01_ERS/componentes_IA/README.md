# Clasificación interna de riesgo de los componentes de IA del SICST

**Proyecto:** Sistema Inteligente de Control y Seguimiento de Terapia Física (SICST)  
**Versión:** 1.0  
**Fecha:** 2026-09-16

## 1. Alcance

Este documento clasifica el riesgo **interno de ingeniería** de los componentes inteligentes especificados para el SICST. La clasificación se utiliza para decidir controles de supervisión, verificación, monitoreo y fallback.

**No constituye una certificación jurídica ni una clasificación legal oficial.** La conclusión se limita al alcance funcional documentado del proyecto.

## 2. Componentes sometidos a clasificación

| Componente | Función | Datos/salidas relevantes | Clasificación interna |
|---|---|---|---|
| IA-01 — Visión por computadora y análisis de movimiento | Analizar ejecución, detectar postura, contar repeticiones y generar retroalimentación | Imagen/video corporal, resultados de ejecución y correcciones posturales | **Alto** |
| IA-02 — Priorización de alertas y recomendaciones | Priorizar eventos de seguimiento y presentar alertas/recomendaciones al fisioterapeuta | Eventos de seguimiento, prioridad, factores explicativos y recomendaciones | **Alto** |

## 3. Escala interna usada

La escala del proyecto tiene tres niveles:

- **Bajo:** un error produce un efecto operativo menor y fácilmente reversible.
- **Medio:** un error puede degradar el servicio o producir decisiones incorrectas, pero con impacto acotado.
- **Alto:** un error puede influir en el seguimiento terapéutico o en información relacionada con el estado del paciente, por lo que exige supervisión humana obligatoria, trazabilidad y fallback seguro.

Con esta escala, IA-01 e IA-02 se mantienen en **Alto** porque sus salidas influyen en el seguimiento de terapia física y pueden afectar la interpretación de una ejecución o la atención de una alerta.

## 4. Límites de autonomía

El SICST se especifica como **apoyo clínico no autónomo**.

Los componentes de IA:

- no emiten diagnóstico médico autónomo;
- no prescriben ni modifican por sí solos un tratamiento;
- no deben presentar una corrección o prioridad como decisión clínica definitiva;
- permiten que el fisioterapeuta revise, confirme, corrija o descarte la salida;
- deben degradarse a revisión manual cuando no alcanzan el umbral definido.

La supervisión humana no es un control opcional: forma parte de los RNF-IA.

## 5. Riesgos principales y salvaguardas

| Riesgo | Componente | Posible consecuencia | Salvaguarda exigida |
|---|---|---|---|
| Detección postural incorrecta | IA-01 | Retroalimentación no adecuada para la ejecución observada | `RNF-IA1-P02`: F1 >= 0.85; revisión del fisioterapeuta; salida no definitiva si no cumple |
| Conteo incorrecto de repeticiones | IA-01 | Registro de progreso inexacto | `RNF-IA1-P03`: MAE <= 1 repetición; corrección manual y estado pendiente de revisión |
| Latencia excesiva | IA-01 | Retroalimentación tardía durante la sesión | `RNF-IA1-P01`: p95 <= 2 s; continuar sin depender de la salida automática |
| Brecha entre grupos etarios | IA-01 | Desempeño desigual | `RNF-IA1-EQ01`: brecha F1 <= 0.05 |
| Brecha por limitación de movilidad | IA-01 | Menor sensibilidad para un grupo | `RNF-IA1-EQ02`: brecha de recall <= 0.05 |
| Explicación insuficiente de una corrección | IA-01 | Usuario/fisioterapeuta no entiende la salida | `RNF-IA1-XAI01`: <= 60 palabras, <= 2 s, claridad media >= 4/5 |
| Falsa prioridad | IA-02 | Atención innecesaria o ruido de alertas | `RNF-IA2-P01`: precisión >= 0.80; confirmación humana |
| Evento prioritario no recuperado | IA-02 | Seguimiento tardío de un evento relevante | `RNF-IA2-P02`: recall >= 0.80; la priorización no puede ser filtro exclusivo si incumple |
| Latencia de priorización | IA-02 | Dashboard degradado | `RNF-IA2-P03`: p95 <= 1 s; revisión manual |
| Brecha etaria de sensibilidad | IA-02 | Priorización desigual | `RNF-IA2-EQ01`: brecha TPR <= 0.05 |
| Brecha de falsas alertas por gravedad | IA-02 | Carga desigual de falsas alarmas | `RNF-IA2-EQ02`: brecha FPR <= 0.05 |
| Alerta sin explicación suficiente | IA-02 | Decisión humana con poco contexto | `RNF-IA2-XAI01`: hasta 3 factores, <= 60 palabras, <= 2 s, claridad >= 4/5 |

## 6. Condiciones que obligan a revisar esta clasificación

La clasificación debe revisarse cuando ocurra cualquiera de estos cambios:

1. un componente pase de recomendar a ejecutar acciones sin confirmación humana;
2. se incorporen nuevos tipos de datos sensibles o nuevas fuentes de imagen/video;
3. se añada diagnóstico, prescripción o ajuste autónomo de terapia;
4. se cambien los umbrales de seguridad o los grupos de equidad;
5. se sustituya el modelo o se modifique de forma sustancial su finalidad;
6. se incorpore un nuevo componente de IA;
7. se detecte en operación un incumplimiento repetido que cambie el perfil de riesgo.

Además, se realiza una revisión documental **al menos anual** mientras el componente permanezca previsto para uso operativo.

## 7. Criterio ante incumplimiento

Un incumplimiento de un umbral de IA no se resuelve ocultando la medición ni promediando el problema. Debe:

1. registrarse el incumplimiento;
2. identificar el requisito afectado;
3. impedir el uso de la salida como criterio automático cuando el RNF así lo exige;
4. derivar a revisión humana;
5. investigar la causa;
6. revalidar el componente antes de restablecer su uso.

## 8. Estado actual

La clasificación anterior documenta el **riesgo previsto por la especificación**. No declara que exista un despliegue clínico ni que se hayan ejecutado ciclos de monitoreo de producción. Las evidencias de verificación deben corresponder a pruebas o mediciones reales y conservar su trazabilidad.

## Responsabilidad de revisión

La clasificación y sus controles se mantienen por el **equipo de desarrollo**, con **revisión clínica del fisioterapeuta responsable** cuando el cambio afecte la interpretación de postura, repeticiones, alertas o recomendaciones. El paciente y el familiar/cuidador no son responsables de la clasificación de riesgo; su participación se limita a los usos y permisos definidos en el ERS.
