# Procedimiento A4 v1.0 — repetición prospectiva de la evaluación

## Preparación previa

- Total de ítems: 66.
- Brazo humano: 33 requisitos.
- Brazo LLM: 33 requisitos.
- Orden de presentación: aleatorizado y fijo para los tres evaluadores.
- Semilla declarada: `20260918`.
- Identificadores ciegos: `A4-001` a `A4-066`.
- Rúbrica: `instrumentos/rubrica_A4_v1.0.md`.
- Hoja de ítems canónica: `datos_preparados/hoja_items_A4_v1.0.csv`.
- La correspondencia ítem–origen no se facilita a los evaluadores.

## Hojas preparadas antes de la recolección

Las tres hojas en blanco que deben quedar versionadas antes de la primera evaluación real son:

| Código | Archivo |
|---|---|
| `EVAL-01` | `instrumentos/hojas_preparadas/SICST_A4_Evaluador_01.xlsx` |
| `EVAL-02` | `instrumentos/hojas_preparadas/SICST_A4_Evaluador_02.xlsx` |
| `EVAL-03` | `instrumentos/hojas_preparadas/SICST_A4_Evaluador_03.xlsx` |

Los tres archivos deben mostrar, antes de iniciar la recolección:

- `Puntajes completados = 0`;
- `Estado = PENDIENTE`;
- celdas de puntuación `D6:H71` vacías;
- exactamente los mismos 66 ítems, en el mismo orden;
- el código del evaluador coherente en las hojas `Instrucciones` y `Evaluacion`.

No se debe modificar el texto de los requisitos, la rúbrica, el orden ni la semilla una vez iniciada la primera sesión.

## Elegibilidad de los evaluadores

Participarán al menos tres personas nuevas que:

1. no sean integrantes actuales ni anteriores del equipo del proyecto;
2. no formen parte del corpus utilizado en el estudio;
3. no hayan sido evaluadores del experimento anterior;
4. no hayan participado previamente en entrevistas, walkthrough o member checking del SICST;
5. no conozcan la correspondencia de origen de los 66 ítems.

Si una persona no cumple estas condiciones, no se utilizará como evaluador de esta repetición.

## Aplicación

Cada evaluador valora los mismos 66 requisitos en las cinco dimensiones de la rúbrica, con valores enteros de 1 a 5.

La persona puede introducir directamente sus puntuaciones o, si no maneja con soltura la hoja de cálculo, puede responder verbalmente mientras el aplicador registra **exactamente** los valores indicados. En ese caso se anota en la ficha de sesión que se utilizó captura asistida verbal. El aplicador no sugiere ni completa puntuaciones por iniciativa propia.

No es necesario compartir pantalla permanentemente. Deben documentarse de forma privada el participante, la fecha, hora de inicio y fin, modalidad/lugar, equipo utilizado y cualquier incidencia. En el repositorio público se utiliza únicamente el código `EVAL-01`, `EVAL-02` o `EVAL-03`.

## Guardado de las evaluaciones reales

Al terminar cada sesión, la hoja completada se conserva sin alterar en:

`06_Experimento/repeticion_A4/datos_crudos/evaluaciones/`

manteniendo el mismo nombre:

- `SICST_A4_Evaluador_01.xlsx`
- `SICST_A4_Evaluador_02.xlsx`
- `SICST_A4_Evaluador_03.xlsx`

La copia en `instrumentos/hojas_preparadas/` permanece como evidencia de la hoja en blanco versionada antes de la recolección.

## Cierre

Antes de cerrar la sesión se comprueba únicamente que existan 330 puntuaciones (66 × 5). La comprobación de completitud no autoriza a cambiar los valores elegidos por la persona.

Cualquier limpieza o transformación posterior se realiza mediante script y nunca sobreescribiendo los archivos crudos originales.
