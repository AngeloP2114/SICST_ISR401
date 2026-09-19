# Registro de correcciones — Plan de mejora de datos SICST

**Plan recibido:** 19/09/2026  
**Repositorio de referencia al recibir el plan:** `gleiston-guerrero/SICST_ISR401`, HEAD `f16af8a`  
**Regla:** no se reescribe historial. Cada corrección se incorpora mediante commit nuevo y se registra aquí.

> IMPORTANTE: los campos `COMMIT: PENDIENTE` deben reemplazarse por el hash real después de subir cada grupo. No escribir hashes inventados.

| Tarea | Cambio / estado | Evidencia o archivo | Commit |
|---|---|---|---|
| A1 | Pendiente de acción en OSF sobre el registro retrospectivo antiguo | OSF `82q76` | PENDIENTE |
| A2 | Pendiente de evidencia primaria de los evaluadores antiguos o rotulado de procedencia no verificable | declaraciones / hojas originales | PENDIENTE |
| A3 | Pendiente de revisar todos los calificativos de independencia del experimento antiguo | `06_Experimento/README.md`, publicación y OSF cuando aplique | PENDIENTE |
| A4 | Preparación prospectiva creada en una estructura simple: rúbrica v1.0, tres hojas en blanco (`SICST_A4_Evaluador_01.xlsx`, `_02.xlsx`, `_03.xlsx`), `hoja_items_A4_v1.0.csv`, semilla 20260918, control de estilo 50 % y registro OSF `drt3c` | `06_Experimento/repeticion_A4/` | PENDIENTE |
| A5 | Se ejecutará después de recibir 3 evaluaciones reales | script/CSV nuevo | PENDIENTE |
| A6 | Ficha rotulada como reconstruida y contradicción de WALK corregida; exportación completa del chat original sigue pendiente | `06_Experimento/prompts_llm/prompt_generacion_RF_llm.md` | PENDIENTE |
| A7 | Definición de consistencia unificada y mención de “clave privada” retirada; versión auténtica usada el 12/09 sigue pendiente | `06_Experimento/instrumentos/rubrica_evaluacion_requisitos.md` | PENDIENTE |
| B1 | Pendiente retranscripción desde audio de FAM-04 | audio original + transcripción | PENDIENTE |
| B2 | Pendiente información real de elegibilidad/reclutamiento/vínculo de cada participante | `02_Evidencias/elegibilidad.csv` | PENDIENTE |
| B3 | Pendiente transcripción literal de piezas faltantes/verificación de ritmos | audios/videos originales | PENDIENTE |
| B4 | Duraciones del README reemplazadas por valores de `ffprobe`; total 11875.815 s ≈ 197.93 min | `02_Evidencias/Transcripciones/README.md` + `Fichas tecnicas/duraciones_reales_ffprobe.csv` | PENDIENTE |
| B5 | Pendiente verificar guías contra todas las transcripciones | guías y transcripciones | PENDIENTE |
| B6 | Referencia del primer commit de Frixon corregida a `9824b6a`; tabla de exclusiones con motivos reales sigue pendiente | `10_Autoria/declaracion_cambio_composicion_equipo.md` | PENDIENTE |
| B7 | Pendiente recalcular corpus final después de resolver B1–B3/B6 | documentación del corpus | PENDIENTE |
| C1–C5 | Pendientes de evidencia/codificación y scripts específicos | matriz, libro de códigos, doble codificación | PENDIENTE |
| D1–D4 | Pendientes de reconstrucción de procedencia real y corrección de matriz/ERS | `04_Trazabilidad/` y ERS | PENDIENTE |
| D5 | Pendiente ejecutar y corregir todas las rutas rotas | script de comprobación | PENDIENTE |
| D6 | Naturaleza del `.tex` declarada como reconstrucción posicional; alineación final de versión pendiente | `01_ERS/README.md` | PENDIENTE |
| E1 | README del MVP corregido para declarar prototipo estático, localStorage, sin backend/login y cámara simulada; Tabla 81 del ERS aún pendiente | `05_MVP/README.md` | PENDIENTE |
| E2 | Pendiente ejecutar casos de prueba reales | CSV de ejecución + evidencia | PENDIENTE |
| F1 | Pendiente repetir member checking real | grabación + acta | PENDIENTE |
| F2 | Pendiente cotejo de actas, códigos, roles y fechas | walkthrough | PENDIENTE |
| F3 | Pendiente fijar fechas reales de notas o aportar prueba contemporánea | notas + registros | PENDIENTE |
| G1 | Pendiente revisión visual y autorización escrita antes de cualquier limpieza de historial | archivos sensibles | PENDIENTE |
| G2 | Pendiente cotejo físico de consentimientos originales | originales | PENDIENTE |
| G3 | Desviación ética y ausencia actual de aval firmado declaradas sin retrofechar | `08_Etica/declaracion_desviacion_etica.md` y `08_Etica/README.md` | PENDIENTE |
| G4 | Procedencia diferenciada: 4 `Formato_*.docx` del equipo; `HCL - HOJA.docx` de la organización | `02_Evidencias/Documentos_Organizacion/README.md` | PENDIENTE |
| G5 | Declaración de IA ampliada con drawio, conversión PDF→LaTeX, python-docx, RNF IA y preparación A4 | `10_Autoria/declaracion_uso_ia.md` | PENDIENTE |
| H1–H3 | Pendientes de exportación original de Forms, recodificaciones e instrumento completo | cuestionario | PENDIENTE |
| I1 | Pendiente alineación final al cerrar v2.3 y completar CHANGELOG desde 26/07 | README, CITATION, CHANGELOG | PENDIENTE |
| I2 | Pendiente verificar lista exacta de los 4 archivos del depósito Zenodo 05/09 antes de corregir documentación | Zenodo `10.5281/zenodo.22315298` | PENDIENTE |
| I3 | `.gitattributes` preparado con LF fijo y dependencias fijadas; falta ejecutar prueba final en clon Windows/autocrlf después de aplicar cambios | `.gitattributes`, requirements | PENDIENTE |

## Cierre

Antes de crear `v2.3-datos`:

1. sustituir todos los `PENDIENTE` que realmente se hayan completado por el hash del commit correspondiente;
2. no marcar como hecha ninguna tarea que dependa de evidencia todavía no obtenida;
3. regenerar manifiestos/checksums cuando corresponda;
4. ejecutar las verificaciones reproducibles;
5. crear la etiqueta anotada únicamente sobre el commit final.
