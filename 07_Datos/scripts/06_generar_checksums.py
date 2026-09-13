"""
06_generar_checksums.py

Calcula el hash SHA-256 de todos los archivos de datos crudos, procesados
y de resultados del paquete 07_Datos, y los escribe en
checksums_datos.sha256 para verificación de integridad.
"""
from pathlib import Path
import hashlib

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "07_Datos"
CHECKSUMS = DATA / "checksums_datos.sha256"


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for bloque in iter(lambda: f.read(65536), b""):
            h.update(bloque)
    return h.hexdigest()


def main():
    archivos = []
    for sub in ["datos_crudos", "datos_procesados", "resultados"]:
        carpeta = DATA / sub
        if carpeta.exists():
            archivos.extend(sorted(p for p in carpeta.rglob("*") if p.is_file()))
    archivos.append(DATA / "diccionario_datos.csv")

    with open(CHECKSUMS, "w", encoding="utf-8") as f:
        for archivo in archivos:
            if archivo.exists():
                ruta_relativa = archivo.relative_to(ROOT)
                f.write(f"{sha256(archivo)}  {ruta_relativa.as_posix()}\n")

    print(f"OK: {CHECKSUMS.relative_to(ROOT)} ({len(archivos)} archivos)")


if __name__ == "__main__":
    main()
