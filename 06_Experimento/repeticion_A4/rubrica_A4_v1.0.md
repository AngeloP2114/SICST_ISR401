# Rúbrica A4 v1.0 — repetición prospectiva humano vs. LLM

**Proyecto:** SICST — Sistema Inteligente de Control y Seguimiento de Terapia Física  
**Versión:** 1.0  
**Fecha de congelación:** 19/09/2026  
**Escala:** 1 a 5  
**Uso:** esta versión debe quedar versionada antes de la primera evaluación real.

## Regla general

Cada requisito se valora de manera independiente en las cinco dimensiones siguientes.  
El evaluador no recibe información sobre el origen humano o LLM del ítem.

## 1. Completitud

**Pregunta:** ¿El requisito contiene la información necesaria para comprender completamente la funcionalidad esperada, sin vacíos relevantes?

| Nivel | Descriptor |
|---|---|
| 1 | Faltan elementos esenciales; no se comprende bien la funcionalidad. |
| 2 | Faltan varios elementos importantes. |
| 3 | Se comprende la función principal, pero falta al menos un detalle relevante. |
| 4 | Está casi completo; solo hay una omisión menor no crítica. |
| 5 | La funcionalidad se comprende completamente, sin vacíos relevantes. |

## 2. Ausencia de ambigüedad

**Pregunta:** ¿El requisito está redactado de forma precisa y permite una interpretación clara, sin términos vagos ni múltiples interpretaciones?

| Nivel | Descriptor |
|---|---|
| 1 | Es muy ambiguo o admite varias interpretaciones incompatibles. |
| 2 | Contiene varios términos vagos o interpretaciones posibles. |
| 3 | Es generalmente claro, pero conserva alguna ambigüedad relevante. |
| 4 | Es claro; solo presenta una ambigüedad menor. |
| 5 | Es preciso y permite una única interpretación razonable. |

## 3. Verificabilidad

**Pregunta:** ¿Es posible comprobar objetivamente si el requisito fue implementado correctamente mediante una prueba o criterio de aceptación?

| Nivel | Descriptor |
|---|---|
| 1 | No es posible definir una comprobación objetiva. |
| 2 | Solo podría comprobarse haciendo muchas suposiciones. |
| 3 | Puede comprobarse parcialmente, pero requiere criterios adicionales. |
| 4 | Es verificable con una aclaración menor. |
| 5 | Puede comprobarse directamente mediante una prueba o criterio objetivo. |

## 4. Corrección respecto a la fuente

Para esta repetición, la referencia entregada al evaluador es el **contexto funcional documentado del SICST**, no la etiqueta de origen del requisito.

**Pregunta:** ¿La funcionalidad es compatible con el contexto funcional del SICST y evita introducir elementos claramente ajenos o incompatibles?

| Nivel | Descriptor |
|---|---|
| 1 | Es claramente incompatible o ajeno al contexto funcional del SICST. |
| 2 | Presenta elementos importantes poco compatibles o sin relación clara con el contexto. |
| 3 | Es plausible dentro del SICST, aunque contiene algún elemento cuya pertinencia es incierta. |
| 4 | Es compatible con el contexto; solo requiere una suposición menor. |
| 5 | Es plenamente compatible con el contexto funcional del SICST y no introduce elementos ajenos. |

## 5. Consistencia interna

**Pregunta:** ¿El requisito es coherente y no contradice otros requisitos o elementos funcionales relacionados del sistema?

| Nivel | Descriptor |
|---|---|
| 1 | Presenta contradicciones claras consigo mismo o con funciones relacionadas. |
| 2 | Presenta una incompatibilidad importante. |
| 3 | Es generalmente consistente, aunque existe una tensión o compatibilidad poco clara. |
| 4 | Es consistente; solo hay un detalle menor que conviene aclarar. |
| 5 | Es coherente y no presenta contradicciones con otros requisitos o elementos relacionados. |

## Contexto funcional entregado a los evaluadores

El SICST es un sistema de software para el control y seguimiento de terapia física. Su contexto funcional incluye gestión de pacientes, evaluaciones, planes terapéuticos, rutinas y ejercicios, seguimiento del progreso, alertas, recordatorios, reportes y apoyo a la supervisión profesional. En esta actividad no se evalúa una interfaz ni un prototipo: se evalúa únicamente la calidad del texto de cada requisito funcional.

## Congelación del instrumento

Una vez iniciada la primera sesión de evaluación no se modificarán:
- los descriptores;
- las preguntas;
- el texto normalizado de los 66 ítems;
- el orden;
- la semilla de aleatorización.
