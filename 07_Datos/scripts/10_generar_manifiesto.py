"""
10_generar_manifiesto.py

Genera 07_Datos/manifiesto_datos.csv con rutas POSIX
relativas a 07_Datos y SHA-256 de cada archivo incluido.
"""

from pathlib import Path
import csv
import hashlib

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "07_Datos"
SALIDA = DATA / "manifiesto_datos.csv"


def sha256(ruta):
    h = hashlib.sha256()

    with open(ruta, "rb") as f:
        for bloque in iter(lambda: f.read(65536), b""):
            h.update(bloque)

    return h.hexdigest()


def categoria(ruta_relativa):
    partes = ruta_relativa.parts

    if partes[0] == "datos_crudos":
        return "dato_crudo"

    if partes[0] == "datos_procesados":
        return "dato_procesado"

    if partes[0] == "resultados":
        return "resultado"

    if partes[0] == "scripts":
        return "script"

    if ruta_relativa.name == "diccionario_datos.csv":
        return "documentacion"

    return "documentacion"


def main():
    archivos = []

    for ruta in DATA.rglob("*"):
        if not ruta.is_file():
            continue

        if "__pycache__" in ruta.parts:
            continue

        if ruta.suffix == ".pyc":
            continue

        if ruta.name in {
            "manifiesto_datos.csv",
            "checksums_datos.sha256",
        }:
            continue

        archivos.append(ruta)

    archivos.sort(
        key=lambda p: p.relative_to(DATA).as_posix()
    )

    with open(
        SALIDA,
        "w",
        encoding="utf-8",
        newline=""
    ) as f:

        writer = csv.writer(
            f,
            lineterminator="\n"
        )

        writer.writerow([
            "ruta_relativa_07_datos",
            "categoria",
            "sha256",
        ])

        for archivo in archivos:
            relativa = archivo.relative_to(DATA)

            writer.writerow([
                relativa.as_posix(),
                categoria(relativa),
                sha256(archivo),
            ])

    print(
        f"OK: manifiesto_datos.csv "
        f"({len(archivos)} archivos documentados)"
    )


if __name__ == "__main__":
    main()
