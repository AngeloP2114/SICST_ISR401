# 07_Datos — Paquete reproducible SICST

Esta carpeta contiene el paquete de datos reproducible del proyecto
**Sistema Inteligente de Control y Seguimiento de Terapia Física (SICST)**.

## Autores

- Contreras Chávez Kevin Germán
- Zambrano Moya Angelo Paul

## Estructura

- `datos_crudos/`
- `datos_procesados/`
- `scripts/` (10 pasos numerados + orquestador)
- `resultados/` (17 artefactos generados + README)
- `diccionario_datos.csv`
- `manifiesto_datos.csv`
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

El orquestador ejecuta, en orden, los siguientes 10 pasos:

1. `01_extraer_crudos.py` — valida el archivo de datos crudos.
2. `02_limpiar_datos.py` — genera `datos_procesados/respuestas_cuestionario_procesadas.csv`.
3. `03_generar_diccionario.py` — genera `diccionario_datos.csv`.
4. `04_analisis_por_perfil.py` — genera los resultados descriptivos por perfil.
5. `05_analisis_por_pregunta.py` — genera las tablas de frecuencia por pregunta.
6. `07_analisis_cruzado.py` — genera las tablas cruzadas perfil × variables clave.
7. `09_analisis_cualitativo.py` — genera el acuerdo entre codificadores y la saturación temática.
8. `08_generar_figuras.py` — genera las figuras reproducibles del análisis.
9. `10_generar_manifiesto.py` — genera `manifiesto_datos.csv`.
10. `06_generar_checksums.py` — genera `checksums_datos.sha256` al final de la cadena.

La carpeta `resultados/` contiene actualmente **17 artefactos generados**
(CSV y PNG), además de su archivo `README.md`.

La cadena reproducible incluye:

- resumen de perfiles;
- estadísticos Likert por perfil;
- tablas de frecuencia;
- cruces por perfil;
- acuerdo entre codificadores;
- saturación temática;
- figuras reproducibles;
- diccionario completo de datos;
- manifiesto de archivos;
- checksums SHA-256.

## Resultados reproducibles

Entre los resultados generados se encuentran:

- `resultados/resumen_perfiles.csv`
- `resultados/estadisticos_likert_por_perfil.csv`
- `resultados/frecuencia_ha_recibido_terapia.csv`
- `resultados/frecuencia_le_han_enviado_ejercicios.csv`
- `resultados/frecuencia_dificultad_principal.csv`
- `resultados/frecuencia_deseo_ver_avance.csv`
- `resultados/frecuencia_aceptacion_uso_camara.csv`
- `resultados/frecuencia_dificultad_observada_fisioterapeutas.csv`
- `resultados/frecuencia_criterios_ejercicio_correcto_fisioterapeutas.csv`
- `resultados/frecuencia_informacion_considerada_privada.csv`
- `resultados/frecuencia_quien_deberia_ver_avance.csv`
- `resultados/cruce_perfil_aceptacion_camara.csv`
- `resultados/cruce_perfil_deseo_ver_avance.csv`
- `resultados/acuerdo_codificadores.csv`
- `resultados/saturacion_tematica.csv`
- `resultados/figura_distribucion_perfiles.png`
- `resultados/figura_medias_likert_por_perfil.png`

## Acuerdo entre codificadores

El análisis cualitativo reproducible genera:

- 36 decisiones comparadas;
- 33 acuerdos;
- 3 desacuerdos;
- 91.67 % de acuerdo observado;
- Cohen's kappa = `0.7187`;
- intervalo bootstrap del 95 % = `[0.3077, 1.0000]`;
- 10 000 remuestreos;
- semilla reproducible = `401`.

Los resultados se conservan en:

`07_Datos/resultados/acuerdo_codificadores.csv`

## Saturación temática

El análisis de saturación utiliza las 18 sesiones canónicas del corpus cualitativo.

El resultado acumulado alcanza **17 temas** y el último tema nuevo aparece en la
sesión 9 (`EFT-01`). Las sesiones 10 a 18 no incorporan temas nuevos.

El archivo generado es:

`07_Datos/resultados/saturacion_tematica.csv`

## Diccionario de datos

El archivo:

`07_Datos/diccionario_datos.csv`

documenta las columnas del conjunto de datos crudo y del conjunto procesado.

El diccionario se genera automáticamente mediante:

`03_generar_diccionario.py`

y no debe modificarse manualmente después de ejecutar el orquestador.

## Manifiesto de datos

El archivo:

`07_Datos/manifiesto_datos.csv`

registra los archivos que forman parte del paquete reproducible utilizando rutas
relativas POSIX respecto a `07_Datos/`.

El manifiesto se genera mediante:

`10_generar_manifiesto.py`

## Integridad

Los valores SHA-256 para verificar los archivos del paquete se encuentran en:

`07_Datos/checksums_datos.sha256`

Después de ejecutar el orquestador, la verificación puede realizarse desde
`07_Datos/` mediante:

```bash
sha256sum -c checksums_datos.sha256 --quiet
```

Si el comando no muestra errores y vuelve al prompt, la verificación de
integridad ha finalizado correctamente.

## Privacidad

El paquete no incluye nombres completos, cédulas, teléfonos, firmas ni
consentimientos firmados.

Los códigos de participante se conservan para trazabilidad académica y no deben
utilizarse para intentar identificar o reidentificar personas.

## Depósito persistente

El paquete reproducible versión 1.0 se encuentra publicado en Zenodo.

- DOI: `10.5281/zenodo.22315298`
- URL: `https://doi.org/10.5281/zenodo.22315298`
- Zenodo: `https://zenodo.org/records/22315298`
- Fecha de publicación: `2026-09-05`
- Acceso: Público / Open

## Criterio de reproducibilidad

La fuente de verdad del análisis es la cadena ejecutada por:

```bash
python 07_Datos/scripts/orquestar.py
```

Los archivos derivados no deben editarse manualmente para modificar resultados.
Cualquier cambio en datos crudos, scripts o reglas de análisis debe reproducirse
mediante el orquestador y finalizar con la regeneración del manifiesto y los
checksums.
