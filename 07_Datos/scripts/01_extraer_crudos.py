"""
01_extraer_crudos.py

Valida que el archivo de datos crudos exista, no esté vacío, y tenga la
estructura mínima esperada (encabezado + al menos una fila de datos).
No modifica el archivo -- solo lo valida antes de que el resto del
pipeline lo use.
"""
from pathlib import Path
import csv
import sys

ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / "07_Datos" / "datos_crudos" / "respuestas_cuestionario_2B.csv"


def main():
    if not RAW.exists():
        print(f"ERROR: no se encontró {RAW}", file=sys.stderr)
        sys.exit(1)

    with open(RAW, "r", encoding="utf-8-sig", newline="") as f:
        filas = list(csv.reader(f))

    if len(filas) < 2:
        print("ERROR: el archivo de datos crudos no tiene filas de datos.", file=sys.stderr)
        sys.exit(1)

    encabezado = filas[0]
    datos = [f for f in filas[1:] if any(c.strip() for c in f)]

    print(f"OK: {RAW.name}")
    print(f"  Columnas: {len(encabezado)}")
    print(f"  Filas de datos válidas: {len(datos)}")


if __name__ == "__main__":
    main()
