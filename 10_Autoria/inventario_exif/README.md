# Inventario EXIF y hashes SHA-256

`inventario_exif.csv` registra la evidencia gráfica pública utilizada en la
auditoría del proyecto.

## Alcance

Se incluyen imágenes de:

- `02_Evidencias/Fotos_Aplicacion/`;
- `02_Evidencias/Fotos_Entorno/`;
- `10_Autoria/capturas/`;
- `10_Autoria/correspondencia/`;
- `10_Autoria/fotos_equipo/`;
- `10_Autoria/notas_campo/`.

El inventario fue regenerado el **18/09/2026** y contiene **88 archivos**.

## Interpretación de columnas

| Columna | Descripción |
|---|---|
| `archivo` | Ruta relativa dentro del repositorio |
| `tamano_bytes` | Tamaño del archivo en bytes |
| `fecha_captura_exif` | Fecha encontrada en EXIF; `SIN_EXIF` cuando no consta |
| `modelo_dispositivo` | Modelo registrado en EXIF; `SIN_EXIF` cuando no consta |
| `gps_presente` | Indica si el archivo contiene campos GPS |
| `hash_sha256` | Huella SHA-256 calculada sobre el archivo versionado |

La ausencia de EXIF no demuestra que una imagen sea falsa: estos metadatos
pueden perderse al exportar, comprimir o enviar un archivo. Por esa razón, la
verificación se complementa con el hash, el historial Git, la correspondencia
y las transcripciones.
