"""
03_generar_diccionario.py

Genera diccionario_datos.csv describiendo cada columna del archivo
procesado: nombre, tipo inferido, y valores de ejemplo/categorías.
"""
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[2]
PROCESSED = ROOT / "07_Datos" / "datos_procesados" / "respuestas_cuestionario_procesadas.csv"
DICCIONARIO = ROOT / "07_Datos" / "diccionario_datos.csv"


def inferir_tipo(valores):
    no_vacios = [v for v in valores if v.strip()]
    if not no_vacios:
        return "vacio_en_esta_muestra"
    if all(v.strip().isdigit() for v in no_vacios):
        return "numerico_escala"
    if len(set(no_vacios)) <= 6:
        return "categorico"
    return "texto_libre"


def main():
    with open(PROCESSED, "r", encoding="utf-8", newline="") as f:
        filas = list(csv.reader(f))

    encabezado = filas[0]
    datos = filas[1:]

    filas_dic = []
    for i, col in enumerate(encabezado):
        valores = [fila[i] for fila in datos if i < len(fila)]
        tipo = inferir_tipo(valores)
        no_vacios = [v for v in valores if v.strip()]
        ejemplos = "; ".join(sorted(set(no_vacios))[:5]) if tipo == "categorico" else (
            no_vacios[0][:60] + ("..." if no_vacios and len(no_vacios[0]) > 60 else "") if no_vacios else ""
        )
        filas_dic.append({
            "columna": col,
            "tipo_inferido": tipo,
            "respuestas_no_vacias": len(no_vacios),
            "ejemplo_o_categorias": ejemplos,
        })

    with open(DICCIONARIO, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["columna", "tipo_inferido", "respuestas_no_vacias", "ejemplo_o_categorias"])
        writer.writeheader()
        writer.writerows(filas_dic)

    print(f"OK: {DICCIONARIO.relative_to(ROOT)} ({len(filas_dic)} columnas documentadas)")


if __name__ == "__main__":
    main()
