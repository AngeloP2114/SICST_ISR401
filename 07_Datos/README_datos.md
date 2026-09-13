# 07_Datos — Paquete reproducible SICST

Esta carpeta contiene el paquete de datos reproducible del proyecto
**Sistema Inteligente de Control y Seguimiento de Terapia Física (SICST)**.

## Autores

- Contreras Chávez Kevin Germán
- Zambrano Moya Angelo Paul

## Estructura

- `datos_crudos/`
- `datos_procesados/`
- `scripts/` (7 pasos numerados + orquestador)
- `resultados/` (13 archivos generados)
- `diccionario_datos.csv`
- `README_datos.md`
- `LICENSE-DATA.txt`
- `checksums_datos.sha256`
- `desviaciones.md`
- `registro_deposito.md`

## Datos utilizados

La fuente reproducible principal se encuentra en:

`07_Datos/datos_crudos/respuestas_cuestionario_2B.csv`

El conjunto contiene **79 respuestas codificadas**:

- 62 pacientes o ex pacientes de terapia física;
- 14 familiares o cuidadores;
- 3 fisioterapeutas.

No se crean participantes, respuestas ni resultados ficticios.

## Reproducción

Desde la raíz del repositorio ejecutar:

```bash
python 07_Datos/scripts/orquestar.py
```

El orquestador corre, en orden, 7 pasos:

1. `01_extraer_crudos.py` — valida el archivo de datos crudos.
2. `02_limpiar_datos.py` — genera `datos_procesados/respuestas_cuestionario_procesadas.csv`.
3. `03_generar_diccionario.py` — genera `diccionario_datos.csv`.
4. `04_analisis_por_perfil.py` — genera `resultados/resumen_perfiles.csv` y
   `resultados/estadisticos_likert_por_perfil.csv`.
5. `05_analisis_por_pregunta.py` — genera 9 tablas de frecuencia en
   `resultados/` (una por cada pregunta categórica o de opción múltiple).
6. `07_analisis_cruzado.py` — genera 2 tablas cruzadas perfil × variable
   clave (aceptación de cámara, deseo de ver el avance).
7. `06_generar_checksums.py` — genera `checksums_datos.sha256` sobre todos
   los archivos anteriores.

En total, el paso 4-7 produce **13 archivos en `resultados/`**.

## Integridad

Los valores SHA-256 para verificar los archivos de datos se encuentran en:

`07_Datos/checksums_datos.sha256`

## Privacidad

El paquete no incluye nombres completos, cédulas, teléfonos, firmas ni consentimientos firmados.

Los códigos de participante se conservan para trazabilidad académica y no deben utilizarse para intentar identificar o reidentificar personas.

## Depósito persistente

El paquete reproducible versión 1.0 se encuentra publicado en Zenodo.

- DOI: `10.5281/zenodo.22315298`
- URL: `https://doi.org/10.5281/zenodo.22315298`
- Zenodo: `https://zenodo.org/records/22315298`
- Fecha de publicación: `2026-09-05`
- Acceso: Público / Open
