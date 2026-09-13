"""
08_generar_figuras.py

Genera figuras (PNG) a partir de los resultados tabulares, tal como exige
la guía: "resultados/ (tablas y figuras generadas por los scripts, nunca
a mano)".
"""
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[2]
RESULTS = ROOT / "07_Datos" / "resultados"


def leer_csv(nombre):
    ruta = RESULTS / nombre
    with open(ruta, "r", encoding="utf-8", newline="") as f:
        return list(csv.reader(f))


def figura_perfiles():
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    filas = leer_csv("resumen_perfiles.csv")[1:]
    perfiles = [f[0] for f in filas]
    cantidades = [int(f[1]) for f in filas]

    fig, ax = plt.subplots(figsize=(7, 4.5))
    ax.bar(perfiles, cantidades, color=["#2563eb", "#16a34a", "#dc2626"])
    ax.set_ylabel("Cantidad de participantes")
    ax.set_title("Distribución de participantes por perfil — Cuestionario SICST (n=79)")
    for i, v in enumerate(cantidades):
        ax.text(i, v + 1, str(v), ha="center")
    plt.xticks(rotation=15, ha="right")
    plt.tight_layout()
    plt.savefig(RESULTS / "figura_distribucion_perfiles.png", dpi=150)
    plt.close()
    print("OK: figura_distribucion_perfiles.png")


def figura_likert():
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    filas = leer_csv("estadisticos_likert_por_perfil.csv")[1:]
    # agrupar por pregunta, usando el perfil dominante (Paciente/Familiar)
    datos_paciente_familiar = [f for f in filas if f[1] in (
        "Paciente o ex paciente de terapia fisica", "Familiar o cuidador"
    )]

    preguntas = sorted(set(f[0] for f in datos_paciente_familiar))
    perfiles = ["Paciente o ex paciente de terapia fisica", "Familiar o cuidador"]

    fig, ax = plt.subplots(figsize=(9, 5))
    x = range(len(preguntas))
    ancho = 0.35
    colores = {"Paciente o ex paciente de terapia fisica": "#2563eb",
               "Familiar o cuidador": "#16a34a"}

    for i, perfil in enumerate(perfiles):
        medias = []
        for pregunta in preguntas:
            fila = next((f for f in datos_paciente_familiar
                         if f[0] == pregunta and f[1] == perfil), None)
            medias.append(float(fila[3]) if fila else 0)
        posiciones = [xi + (i - 0.5) * ancho for xi in x]
        ax.bar(posiciones, medias, width=ancho, label=perfil, color=colores[perfil])

    ax.set_xticks(list(x))
    ax.set_xticklabels(preguntas, rotation=30, ha="right", fontsize=8)
    ax.set_ylabel("Media (escala 1-5)")
    ax.set_ylim(0, 5.5)
    ax.set_title("Puntaje medio por pregunta Likert, según perfil")
    ax.legend()
    plt.tight_layout()
    plt.savefig(RESULTS / "figura_medias_likert_por_perfil.png", dpi=150)
    plt.close()
    print("OK: figura_medias_likert_por_perfil.png")


def main():
    figura_perfiles()
    figura_likert()


if __name__ == "__main__":
    main()
