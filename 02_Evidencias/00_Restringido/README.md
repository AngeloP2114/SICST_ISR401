# Evidencias restringidas

Esta carpeta contiene las evidencias originales con datos identificables del proyecto SICST.

Las evidencias restringidas se almacenan en un contenedor cifrado mediante AES-256:
`evidencias_restringidas.7z`, publicado como asset del Release
[`evidencias-2B`](https://github.com/AngeloP2114/Sistema_Terapia_Fisica_ISR401_2B/releases/tag/evidencias-2B).

## Descarga

URL directa del archivo cifrado (1.08 GB):
https://github.com/AngeloP2114/Sistema_Terapia_Fisica_ISR401_2B/releases/download/evidencias-2B/evidencias_restringidas.7z

Checksum del contenedor (para verificar integridad de la descarga):
https://github.com/AngeloP2114/Sistema_Terapia_Fisica_ISR401_2B/releases/download/evidencias-2B/checksum_evidencias_restringidas.sha256

## Qué hay dentro

Las 67 piezas de audio y video fichadas en
`02_Evidencias/Fichas tecnicas/fichas_tecnicas.csv` (columna `ubicacion_deposito`)
están depositadas dentro de este contenedor cifrado.

## Verificación de integridad del contenedor completo

```powershell
Get-FileHash evidencias_restringidas.7z -Algorithm SHA256
```
Debe coincidir con el valor publicado en `checksum_evidencias_restringidas.sha256`.

## Verificación de una pieza individual (sin descomprimir todo)

1. Descargar `evidencias_restringidas.7z` desde el enlace de arriba.
2. Solicitar la contraseña al equipo por el medio institucional correspondiente.
3. Extraer únicamente el archivo deseado (el contenedor no usa modo sólido,
   así que no hace falta descomprimir los 67 archivos completos):
   ```powershell
   & "C:\Program Files\7-Zip\7z.exe" e evidencias_restringidas.7z NOMBRE_DEL_ARCHIVO -p"CONTRASEÑA"
   ```
4. Calcular su SHA-256 y compararlo con la columna `sha256` de `fichas_tecnicas.csv`
   para esa pieza:
   ```powershell
   Get-FileHash NOMBRE_DEL_ARCHIVO -Algorithm SHA256
   ```

## Contraseña

La contraseña del contenedor cifrado no se publica en este repositorio y se
entrega únicamente al docente mediante el medio institucional correspondiente.

## Nota sobre el inventario final

La inspección del 15/09/2026 registró 45 piezas multimedia.
El inventario de cierre contiene 67 piezas de audio y video disponibles
en el Release `evidencias-2B`. La ficha técnica final fue regenerada
directamente a partir de los archivos depositados mediante `ffprobe`
y SHA-256.
