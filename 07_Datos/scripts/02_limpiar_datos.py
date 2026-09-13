"""
02_limpiar_datos.py

Genera datos_procesados/respuestas_cuestionario_procesadas.csv a partir de
los datos crudos: elimina la columna de fecha/hora (para reducir
información temporal innecesaria en los datos derivados), recorta espacios
en blanco, y descarta filas completamente vacías.
"""
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / "07_Datos" / "datos_crudos" / "respuestas_cuestionario_2B.csv"
PROCESSED = ROOT / "07_Datos" / "datos_procesados" / "respuestas_cuestionario_procesadas.csv"


def main():
    with open(RAW, "r", encoding="utf-8-sig", newline="") as f:
        filas = list(csv.reader(f))

    encabezado = [c.strip() for c in filas[0]]
    datos = [f for f in filas[1:] if any(c.strip() for c in f)]

    # La primera columna es fecha/hora de respuesta; se excluye de la
    # version procesada.
    encabezado_procesado = encabezado[1:]
    datos_procesados = [[c.strip() for c in fila][1:] for fila in datos]

    PROCESSED.parent.mkdir(parents=True, exist_ok=True)
    with open(PROCESSED, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(encabezado_procesado)
        writer.writerows(datos_procesados)

    print(f"OK: {PROCESSED.relative_to(ROOT)} ({len(datos_procesados)} filas)")


if __name__ == "__main__":
    main()
