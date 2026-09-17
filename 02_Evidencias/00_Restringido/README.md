# Evidencias restringidas

Esta carpeta contiene las evidencias originales con datos identificables del proyecto SICST.

Las evidencias restringidas se almacenan en un contenedor cifrado mediante AES-256:

`evidencias_restringidas.7z`

El contenedor está publicado como asset del Release:

`evidencias-2B`

## Descarga

URL directa del archivo cifrado:

https://github.com/AngeloP2114/Sistema_Terapia_Fisica_ISR401_2B/releases/download/evidencias-2B/evidencias_restringidas.7z

Checksum del contenedor:

https://github.com/AngeloP2114/Sistema_Terapia_Fisica_ISR401_2B/releases/download/evidencias-2B/checksum_evidencias_restringidas.sha256

## Qué hay dentro

El inventario final contiene 67 piezas multimedia:

- 34 archivos de video.
- 33 archivos de audio.

Todas las piezas están documentadas en:

`02_Evidencias/Fichas tecnicas/fichas_tecnicas.csv`

La ficha técnica incluye, entre otros campos:

- nombre del archivo;
- tipo de evidencia;
- ruta relativa;
- duración obtenida mediante `ffprobe`;
- formato;
- códec de video;
- códec de audio;
- tamaño en bytes;
- SHA-256;
- ubicación del depósito;
- URL de descarga.

Las 67 piezas fichadas están depositadas dentro del contenedor cifrado
`evidencias_restringidas.7z`.

## Inventario de duraciones

Las duraciones finales se obtuvieron directamente sobre los archivos reales mediante
`ffprobe`.

El resultado completo se conserva en:

`02_Evidencias/Fichas tecnicas/duraciones_reales_ffprobe.csv`

Este archivo contiene las 67 piezas y su duración tanto en segundos como en formato
horas, minutos y segundos.

## Verificación de integridad del contenedor completo

Después de descargar `evidencias_restringidas.7z`, puede calcularse su SHA-256 mediante
PowerShell:

```powershell
Get-FileHash evidencias_restringidas.7z -Algorithm SHA256
```

El resultado esperado es:

```text
22E59782CC933666309B53CCD830C0B294408065DAC2F475D1FF320371C0E01F
```

El mismo valor se encuentra registrado en:

`02_Evidencias/00_Restringido/checksum_evidencias_restringidas.sha256`

y en el asset correspondiente del Release `evidencias-2B`.

## Acceso para verificación docente

El contenedor `evidencias_restringidas.7z` se encuentra cifrado mediante AES-256 debido
a que contiene evidencias con datos identificables.

La contraseña no consta en este repositorio público.

Se entrega exclusivamente al docente responsable mediante el Sistema de Gestión
Académica (SGA).

Una vez recibida la contraseña, el docente puede descargar el contenedor desde el Release
`evidencias-2B`, seleccionar cualquier pieza fichada, extraerla y comprobar su integridad.

## Verificación de una pieza individual

El contenedor fue creado sin modo sólido, por lo que no es necesario extraer las 67 piezas
para comprobar una evidencia determinada.

Con 7-Zip instalado, puede extraerse una pieza concreta mediante:

```powershell
& "C:\Program Files\7-Zip\7z.exe" e evidencias_restringidas.7z "NOMBRE_DEL_ARCHIVO" -p"CONTRASEÑA"
```

Después puede calcularse su SHA-256:

```powershell
Get-FileHash "NOMBRE_DEL_ARCHIVO" -Algorithm SHA256
```

El valor obtenido debe coincidir exactamente con la columna `sha256` de:

`02_Evidencias/Fichas tecnicas/fichas_tecnicas.csv`

## Verificación de duración y códecs

La duración y los códecs de cualquier pieza pueden comprobarse mediante `ffprobe`.

Para video:

```powershell
ffprobe -v error -show_entries format=filename,duration,format_name -show_entries stream=codec_type,codec_name -of default=noprint_wrappers=1 "ARCHIVO.mp4"
```

Para audio:

```powershell
ffprobe -v error -show_entries format=filename,duration,format_name -show_entries stream=codec_type,codec_name -of default=noprint_wrappers=1 "ARCHIVO.mp3"
```

o, cuando corresponda:

```powershell
ffprobe -v error -show_entries format=filename,duration,format_name -show_entries stream=codec_type,codec_name -of default=noprint_wrappers=1 "ARCHIVO.m4a"
```

La duración obtenida debe coincidir con la columna `duracion_segundos` de
`fichas_tecnicas.csv`.

## URL de descarga por pieza

La columna `url_descarga` de `fichas_tecnicas.csv` apunta al depósito donde se encuentran
las evidencias originales:

`evidencias_restringidas.7z`

publicado en el Release `evidencias-2B`.

De esta manera, cada pieza fichada dispone de una ruta verificable hacia el depósito que
la contiene.

## Nota sobre el inventario final

La inspección realizada el 15/09/2026 registró un inventario previo de 45 piezas
multimedia.

Durante el cierre del paquete de evidencias se realizó una conciliación completa contra
los archivos efectivamente depositados.

El inventario final contiene 67 piezas de audio y video.

La ficha técnica final fue regenerada directamente a partir de los archivos reales,
obteniendo:

- duración mediante `ffprobe`;
- códecs mediante `ffprobe`;
- tamaño real en bytes;
- SHA-256 mediante cálculo directo sobre cada archivo;
- URL del depósito final.

Por ello, el archivo:

`02_Evidencias/Fichas tecnicas/fichas_tecnicas.csv`

constituye el inventario técnico definitivo de las evidencias multimedia de la Entrega 2B.

## Contraseña

La contraseña del contenedor cifrado no se publica en este repositorio.

Se entrega exclusivamente al docente responsable mediante el Sistema de Gestión Académica
(SGA), debido a que las evidencias contienen información identificable de los
participantes.
