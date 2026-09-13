# Dataset reproducible SICST — Zenodo

## Descripción

Este paquete documenta el conjunto de datos reproducible del proyecto
**Sistema Inteligente de Control y Seguimiento de Terapia Física
(SICST)**, incluyendo tanto el cuestionario general del proyecto como el
experimento comparativo del Enfoque 1 (RF humano vs. LLM).

## Autores

- Contreras Chávez Kevin Germán
- Zambrano Moya Angelo Paul (ORCID: 0009-0006-0056-8482)

## Publicación

- DOI: `10.5281/zenodo.22315298`
- URL DOI: `https://doi.org/10.5281/zenodo.22315298`
- Zenodo: `https://zenodo.org/records/22315298`
- Versión: `1.0`
- Acceso: Público / Open

## Registro previo del experimento (OSF)

- DOI: `10.17605/OSF.IO/82Q76`
- URL: `https://doi.org/10.17605/OSF.IO/82Q76`
- Fecha de registro: 2026-09-12

## Contenido del paquete

### Cuestionario general del proyecto
- `resumen_perfiles.csv` — distribución de 79 respuestas por perfil.
- `catalogo_transcripciones_anonimizado.csv` — índice de transcripciones.
- `Matriz_Trazabilidad_Final_PE5_Rubrica.csv` — matriz de trazabilidad
  ERS (58 trazas: RF, RNF generales, RNF de IA).

### Experimento comparativo (Enfoque 1: LLM vs. humano)
- `prompt_generacion_RF_llm.md` — prompt exacto usado con GPT-5.5-mini,
  modelo, fecha, y confirmación de no uso de información externa.
- `matriz_trazabilidad_tema_RF.csv` — pareo temático entre RF humanos y
  RF del LLM (66 ítems, 11 pares estrictos usados en el análisis
  confirmatorio).
- `analisis_experimento_llm_humano.py` — script reproducible que calcula
  el acuerdo entre evaluadores (κ de Fleiss) y la comparación pareada
  (prueba t / Wilcoxon con corrección de Holm-Bonferroni), y regenera
  exactamente las Tablas 1-2 y la Figura 1 del manuscrito.

### Documentación
- `ANONYMIZATION.md` — procedimiento de anonimización aplicado.
- `ETHICS.md` — declaración ética y de gobernanza de datos.
- `CITATION.cff` — metadatos de citación.
- `LICENSE.txt` — licencia del contenido.

## Fuente reproducible completa

La versión vigente de todos los datos y scripts se encuentra en el
repositorio del proyecto:

`https://github.com/AngeloP2114/Sistema_Terapia_Fisica_ISR401_2B`

- Cuestionario general: `07_Datos/`
- Experimento Enfoque 1: `06_Experimento/`

## Reproducción

Desde la raíz del repositorio:

```bash
# Cuestionario general
python 07_Datos/scripts/orquestar.py

# Experimento comparativo LLM vs. humano
python 06_Experimento/scripts_analisis/analisis_experimento_llm_humano.py
```

## Integridad

Los hashes SHA-256 del cuestionario general se encuentran en
`07_Datos/checksums_datos.sha256`.

## Privacidad

No se incluyen nombres completos, cédulas, teléfonos, firmas ni
consentimientos firmados. Los códigos de participante se mantienen
únicamente para trazabilidad académica. La clave que revela el origen
real (humano/LLM) de cada ítem del experimento se mantiene cifrada fuera
de este paquete público (ver `ANONYMIZATION.md`).

## Citación

Consultar `CITATION.cff`.

## Repositorio fuente

`https://github.com/AngeloP2114/Sistema_Terapia_Fisica_ISR401_2B`
