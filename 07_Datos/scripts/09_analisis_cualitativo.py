"""
09_analisis_cualitativo.py

Genera resultados reproducibles del análisis cualitativo SICST:

1. Acuerdo entre codificadores:
   - porcentaje de acuerdo
   - Cohen's kappa
   - IC 95 % bootstrap
   - semilla reproducible

2. Saturación temática:
   - temas nuevos por sesión
   - temas acumulados
"""

from pathlib import Path
import csv
import random
import math

ROOT = Path(__file__).resolve().parents[2]

RESULTS = ROOT / "07_Datos" / "resultados"

COD_ANGELO = (
    ROOT
    / "10_Autoria"
    / "doble_codificacion"
    / "codificacion_angelo.csv"
)

COD_KEVIN = (
    ROOT
    / "10_Autoria"
    / "doble_codificacion"
    / "codificacion_kevin.csv"
)

MATRIZ_CODIFICACION = (
    ROOT
    / "02_Evidencias"
    / "Codificacion_Tematica"
    / "matriz_codificacion_SICST.csv"
)

SALIDA_ACUERDO = RESULTS / "acuerdo_codificadores.csv"
SALIDA_SATURACION = RESULTS / "saturacion_tematica.csv"

N_BOOTSTRAP = 10000
SEMILLA = 401


def leer_codificacion(ruta):
    with open(
        ruta,
        "r",
        encoding="utf-8-sig",
        newline=""
    ) as archivo:

        lector = csv.DictReader(archivo)
        filas = list(lector)

        codigos = [
            c
            for c in lector.fieldnames
            if c != "participante"
        ]

    datos = {}

    for fila in filas:
        participante = fila["participante"]

        datos[participante] = {
            codigo: int(fila[codigo])
            for codigo in codigos
        }

    return datos, codigos


def calcular_kappa(pares):
    n = len(pares)

    acuerdos = sum(
        1
        for a, b in pares
        if a == b
    )

    po = acuerdos / n

    p1_a = sum(a for a, _ in pares) / n
    p1_b = sum(b for _, b in pares) / n

    p0_a = 1 - p1_a
    p0_b = 1 - p1_b

    pe = (
        p1_a * p1_b
        + p0_a * p0_b
    )

    if abs(1 - pe) < 1e-12:
        return None, po

    kappa = (
        po - pe
    ) / (
        1 - pe
    )

    return kappa, po


def percentil(valores, p):
    valores = sorted(valores)

    posicion = (
        len(valores) - 1
    ) * p

    inferior = math.floor(posicion)
    superior = math.ceil(posicion)

    if inferior == superior:
        return valores[inferior]

    fraccion = posicion - inferior

    return (
        valores[inferior]
        + (
            valores[superior]
            - valores[inferior]
        )
        * fraccion
    )


def generar_acuerdo():
    angelo, codigos_a = leer_codificacion(
        COD_ANGELO
    )

    kevin, codigos_k = leer_codificacion(
        COD_KEVIN
    )

    if codigos_a != codigos_k:
        raise ValueError(
            "Los dos archivos de codificación "
            "no contienen los mismos códigos."
        )

    if set(angelo) != set(kevin):
        raise ValueError(
            "Los archivos de codificación "
            "no contienen los mismos participantes."
        )

    pares = []

    for participante in angelo:
        for codigo in codigos_a:
            pares.append(
                (
                    angelo[participante][codigo],
                    kevin[participante][codigo],
                )
            )

    kappa, acuerdo = calcular_kappa(pares)

    rng = random.Random(SEMILLA)

    bootstrap = []

    for _ in range(N_BOOTSTRAP):
        muestra = [
            pares[
                rng.randrange(len(pares))
            ]
            for _ in range(len(pares))
        ]

        k, _ = calcular_kappa(muestra)

        if k is not None:
            bootstrap.append(k)

    ic_lo = percentil(
        bootstrap,
        0.025
    )

    ic_hi = percentil(
        bootstrap,
        0.975
    )

    acuerdos = sum(
        1
        for a, b in pares
        if a == b
    )

    desacuerdos = (
        len(pares) - acuerdos
    )

    with open(
        SALIDA_ACUERDO,
        "w",
        encoding="utf-8",
        newline=""
    ) as archivo:

        writer = csv.writer(
            archivo,
            lineterminator="\n"
        )

        writer.writerow(
            ["metrica", "valor"]
        )

        writer.writerow(
            [
                "decisiones_comparadas",
                len(pares)
            ]
        )

        writer.writerow(
            ["acuerdos", acuerdos]
        )

        writer.writerow(
            ["desacuerdos", desacuerdos]
        )

        writer.writerow(
            [
                "porcentaje_acuerdo",
                f"{acuerdo * 100:.2f}"
            ]
        )

        writer.writerow(
            [
                "cohen_kappa",
                f"{kappa:.4f}"
            ]
        )

        writer.writerow(
            [
                "ic95_inferior",
                f"{ic_lo:.4f}"
            ]
        )

        writer.writerow(
            [
                "ic95_superior",
                f"{ic_hi:.4f}"
            ]
        )

        writer.writerow(
            [
                "bootstrap_repeticiones",
                N_BOOTSTRAP
            ]
        )

        writer.writerow(
            ["semilla", SEMILLA]
        )

    print(
        "OK: acuerdo_codificadores.csv "
        f"(kappa={kappa:.4f}, "
        f"IC95=[{ic_lo:.4f}, {ic_hi:.4f}], "
        f"semilla={SEMILLA})"
    )


def generar_saturacion():
    with open(
        MATRIZ_CODIFICACION,
        "r",
        encoding="utf-8-sig",
        newline=""
    ) as archivo:

        reader = csv.DictReader(archivo)
        filas = list(reader)

    columnas = [
        c
        for c in reader.fieldnames
        if c not in (
            "codigo",
            "participante"
        )
    ]

    temas_vistos = set()
    resultado = []

    for orden, fila in enumerate(
        filas,
        start=1
    ):
        participante = (
            fila.get("codigo")
            or fila.get("participante")
        )

        presentes = {
            codigo
            for codigo in columnas
            if fila.get(
                codigo,
                ""
            ).strip() == "1"
        }

        nuevos = (
            presentes
            - temas_vistos
        )

        temas_vistos.update(
            presentes
        )

        resultado.append(
            {
                "orden": orden,
                "participante": participante,
                "temas_nuevos": len(nuevos),
                "temas_acumulados": len(temas_vistos),
            }
        )

    with open(
        SALIDA_SATURACION,
        "w",
        encoding="utf-8",
        newline=""
    ) as archivo:

        writer = csv.DictWriter(
            archivo,
            fieldnames=[
                "orden",
                "participante",
                "temas_nuevos",
                "temas_acumulados",
            ],
            lineterminator="\n",
        )

        writer.writeheader()
        writer.writerows(resultado)

    print(
        "OK: saturacion_tematica.csv "
        f"({len(resultado)} sesiones, "
        f"{len(temas_vistos)} temas acumulados)"
    )


def main():
    RESULTS.mkdir(
        parents=True,
        exist_ok=True
    )

    generar_acuerdo()
    generar_saturacion()


if __name__ == "__main__":
    main()
