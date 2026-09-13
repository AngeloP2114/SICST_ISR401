# Rúbrica de Evaluación de Calidad de Requisitos Funcionales — SICST

## Objetivo

Evaluar comparativamente la calidad de los Requisitos Funcionales (RF)
elicitados por el equipo humano y los generados por el modelo de lenguaje
(LLM), mediante una escala Likert de 1 a 5 en cinco dimensiones.

## Escala

Cada dimensión se puntúa de **1** (no cumple en absoluto) a **5** (cumple
totalmente), sin puntos intermedios ambiguos.

---

## Dimensiones de evaluación

### 1. Completitud

¿La información proporcionada en el requisito permite comprender
completamente la funcionalidad esperada, sin dejar vacíos relevantes?

### 2. Ausencia de ambigüedad

¿El requisito está redactado de forma precisa, sin términos vagos ni
interpretaciones múltiples posibles?

### 3. Verificabilidad

¿Es posible comprobar objetivamente si el requisito fue implementado
correctamente (se puede definir una prueba o criterio de aceptación)?

### 4. Corrección respecto a la fuente

¿El requisito refleja fielmente lo que se dijo en la transcripción de
entrevista de la que proviene, sin agregar ni distorsionar información?

### 5. Consistencia interna

¿El requisito es coherente consigo mismo y no presenta contradicciones
internas en su propia redacción?

---

## Registro de evaluación

Cada evaluador completa su hoja individual en:

```
datos_crudos/evaluaciones_ciegas/Evaluacion_<nombre>.xlsx
```

Puntuando cada uno de los 66 ítems anonimizados de
`datos_crudos/hoja_evaluacion_ciega.csv` en las 5 dimensiones anteriores.

## Cegado

Los evaluadores desconocen si cada ítem proviene del proceso humano o del
LLM. El origen real solo se revela durante el análisis, mediante la clave
privada de desciego almacenada de forma cifrada en
`02_Evidencias/00_Restringido/`.

## Evaluadores participantes

4 evaluadores independientes: Mishell, Angel, Dayana y Sebas.
