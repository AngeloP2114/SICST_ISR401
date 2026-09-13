"""
04_analisis_por_perfil.py

Genera resultados agregados por perfil de participante (Paciente/ex
paciente, Familiar o cuidador, Fisioterapeuta):
  - resumen_perfiles.csv           : conteo de participantes por perfil
  - estadisticos_likert_por_perfil.csv : media/mediana de las preguntas
                                          en escala 1-5, por perfil
"""
from pathlib import Path
import csv
import statistics

ROOT = Path(__file__).resolve().parents[2]
PROCESSED = ROOT / "07_Datos" / "datos_procesados" / "respuestas_cuestionario_procesadas.csv"
RESULTS = ROOT / "07_Datos" / "resultados"

COL_PERFIL = "3. Cual es su perfil dentro del estudio?"

# Preguntas Likert 1-5 compartidas por Paciente/Familiar
LIKERT_PACIENTE_FAMILIAR = {
    "6. Que tan dificil le resulta recordar como hacer los ejercicios o cuantas repeticiones realizar?": "dificultad_recordar_ejercicios",
    "7. Que tan importante seria recibir indicaciones claras con imagenes, videos o pasos sencillos?": "importancia_instrucciones_claras",
    "8. Que tan importante seria recibir recordatorios para cumplir los ejercicios?": "importancia_recordatorios",
    "10. Que tan importante seria registrar dolor despues de realizar ejercicios?": "importancia_registro_dolor",
    "11. Que tan importante seria registrar cansancio o fatiga despues de realizar ejercicios?": "importancia_registro_fatiga",
}

# Preguntas Likert 1-5 de la rama Fisioterapeuta
LIKERT_FISIOTERAPEUTA = {
    "8. Que tan importante considera mantener un historial organizado del tratamiento y evolucion del paciente?": "importancia_historial_organizado",
    "12. Que tan importante considera solicitar autorizacion antes de usar camara, imagenes o datos personales del paciente?": "importancia_autorizacion_uso_datos",
}


def leer_datos():
    with open(PROCESSED, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)


def main():
    datos = leer_datos()
    RESULTS.mkdir(parents=True, exist_ok=True)

    # --- resumen_perfiles.csv ---
    conteo = {}
    for fila in datos:
        perfil = fila[COL_PERFIL].strip()
        if perfil:
            conteo[perfil] = conteo.get(perfil, 0) + 1

    with open(RESULTS / "resumen_perfiles.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["perfil", "cantidad"])
        for perfil in sorted(conteo):
            writer.writerow([perfil, conteo[perfil]])
    print(f"OK: resumen_perfiles.csv ({sum(conteo.values())} participantes)")

    # --- estadisticos_likert_por_perfil.csv ---
    filas_stats = []
    todas_las_preguntas = {**LIKERT_PACIENTE_FAMILIAR, **LIKERT_FISIOTERAPEUTA}
    for pregunta_col, nombre_corto in todas_las_preguntas.items():
        if pregunta_col not in datos[0]:
            continue
        por_perfil = {}
        for fila in datos:
            val = fila.get(pregunta_col, "").strip()
            perfil = fila[COL_PERFIL].strip()
            if val.isdigit():
                por_perfil.setdefault(perfil, []).append(int(val))
        for perfil, valores in por_perfil.items():
            if not valores:
                continue
            filas_stats.append({
                "pregunta": nombre_corto,
                "perfil": perfil,
                "n": len(valores),
                "media": round(statistics.mean(valores), 3),
                "mediana": statistics.median(valores),
                "de": round(statistics.pstdev(valores), 3) if len(valores) > 1 else 0,
                "min": min(valores),
                "max": max(valores),
            })

    with open(RESULTS / "estadisticos_likert_por_perfil.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["pregunta", "perfil", "n", "media", "mediana", "de", "min", "max"])
        writer.writeheader()
        writer.writerows(filas_stats)
    print(f"OK: estadisticos_likert_por_perfil.csv ({len(filas_stats)} filas)")


if __name__ == "__main__":
    main()
