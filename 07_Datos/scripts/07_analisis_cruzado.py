"""
07_analisis_cruzado.py

Genera tablas cruzadas (perfil x variable) para las preguntas más
relevantes al diseño del sistema: aceptación de cámara y deseo de ver el
avance de forma sencilla, discriminado por tipo de participante.
"""
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[2]
PROCESSED = ROOT / "07_Datos" / "datos_procesados" / "respuestas_cuestionario_procesadas.csv"
RESULTS = ROOT / "07_Datos" / "resultados"

COL_PERFIL = "3. Cual es su perfil dentro del estudio?"

CRUCES = {
    "13. Aceptaria el uso de camara para revisar ejercicios si primero se solicita autorizacion?": "cruce_perfil_aceptacion_camara.csv",
    "12. Le gustaria ver el avance de la recuperacion de forma sencilla?": "cruce_perfil_deseo_ver_avance.csv",
}


def main():
    with open(PROCESSED, "r", encoding="utf-8", newline="") as f:
        datos = list(csv.DictReader(f))

    RESULTS.mkdir(parents=True, exist_ok=True)

    for columna, archivo in CRUCES.items():
        if columna not in datos[0]:
            continue
        tabla = {}
        for fila in datos:
            perfil = fila[COL_PERFIL].strip()
            val = fila.get(columna, "").strip()
            if perfil and val:
                tabla.setdefault(perfil, {}).setdefault(val, 0)
                tabla[perfil][val] += 1

        opciones = sorted({v for perfil_dict in tabla.values() for v in perfil_dict})
        with open(RESULTS / archivo, "w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["perfil"] + opciones)
            for perfil in sorted(tabla):
                writer.writerow([perfil] + [tabla[perfil].get(op, 0) for op in opciones])
        print(f"OK: {archivo}")


if __name__ == "__main__":
    main()
