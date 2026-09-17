"""
03_generar_diccionario.py

Genera diccionario_datos.csv con una fila por cada columna de los
dos archivos canónicos del paquete:

- 26 columnas del archivo crudo.
- 25 columnas del archivo procesado.

Total esperado: 51 filas documentadas.
"""

from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "07_Datos"

FUENTES = [
    (
        BASE / "datos_crudos" / "respuestas_cuestionario_2B.csv",
        "datos_crudos/respuestas_cuestionario_2B.csv",
        "utf-8-sig",
    ),
    (
        BASE / "datos_procesados" / "respuestas_cuestionario_procesadas.csv",
        "datos_procesados/respuestas_cuestionario_procesadas.csv",
        "utf-8",
    ),
]

DICCIONARIO = BASE / "diccionario_datos.csv"


def inferir_tipo(valores):
    no_vacios = [v.strip() for v in valores if v.strip()]

    if not no_vacios:
        return "vacio_en_esta_muestra"

    if all(v.replace(".", "", 1).isdigit() for v in no_vacios):
        return "numerico"

    if len(set(no_vacios)) <= 6:
        return "categorico"

    return "texto_libre"


def documentar_archivo(ruta, nombre_relativo, encoding):
    with open(ruta, "r", encoding=encoding, newline="") as f:
        filas = list(csv.reader(f))

    if not filas:
        raise ValueError(f"Archivo vacío: {ruta}")

    encabezado = filas[0]
    datos = filas[1:]
    resultado = []

    for i, columna in enumerate(encabezado):
        valores = [
            fila[i]
            for fila in datos
            if i < len(fila)
        ]

        no_vacios = [
            v.strip()
            for v in valores
            if v.strip()
        ]

        tipo = inferir_tipo(valores)

        if tipo == "categorico":
            ejemplo = "; ".join(sorted(set(no_vacios))[:5])
        elif no_vacios:
            ejemplo = no_vacios[0][:100]
        else:
            ejemplo = ""

        resultado.append({
            "archivo_origen": nombre_relativo,
            "columna": columna,
            "tipo_inferido": tipo,
            "respuestas_no_vacias": len(no_vacios),
            "ejemplo_o_categorias": ejemplo,
        })

    return resultado


def main():
    filas_diccionario = []

    for ruta, nombre_relativo, encoding in FUENTES:
        if not ruta.exists():
            raise FileNotFoundError(f"No existe: {ruta}")

        filas_diccionario.extend(
            documentar_archivo(
                ruta,
                nombre_relativo,
                encoding,
            )
        )

    with open(
        DICCIONARIO,
        "w",
        encoding="utf-8",
        newline=""
    ) as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "archivo_origen",
                "columna",
                "tipo_inferido",
                "respuestas_no_vacias",
                "ejemplo_o_categorias",
            ],
            lineterminator="\n",
        )

        writer.writeheader()
        writer.writerows(filas_diccionario)

    print(
        f"OK: {DICCIONARIO.relative_to(ROOT)} "
        f"({len(filas_diccionario)} columnas documentadas)"
    )

    if len(filas_diccionario) != 51:
        raise ValueError(
            "Se esperaban 51 filas en el diccionario "
            f"y se generaron {len(filas_diccionario)}."
        )


if __name__ == "__main__":
    main()
