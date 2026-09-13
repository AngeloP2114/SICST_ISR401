"""
05_analisis_por_pregunta.py

Genera una tabla de frecuencias por cada pregunta categórica o de
selección múltiple del cuestionario, en archivos separados dentro de
resultados/. Las preguntas de opción múltiple (con respuestas separadas
por coma) se descomponen contando cada opción por separado.
"""
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[2]
PROCESSED = ROOT / "07_Datos" / "datos_procesados" / "respuestas_cuestionario_procesadas.csv"
RESULTS = ROOT / "07_Datos" / "resultados"

# columna_original -> (nombre_archivo, es_multiseleccion)
PREGUNTAS_SIMPLES = {
    "4. Ha recibido usted o la persona que cuida terapia fisica o rehabilitacion?": "frecuencia_ha_recibido_terapia.csv",
    "5. Le han enviado ejercicios para realizar en casa?": "frecuencia_le_han_enviado_ejercicios.csv",
    "9. Cual ha sido o seria la dificultad principal al realizar ejercicios en casa?": "frecuencia_dificultad_principal.csv",
    "12. Le gustaria ver el avance de la recuperacion de forma sencilla?": "frecuencia_deseo_ver_avance.csv",
    "13. Aceptaria el uso de camara para revisar ejercicios si primero se solicita autorizacion?": "frecuencia_aceptacion_uso_camara.csv",
    "6. Cual dificultad observa con mayor frecuencia cuando el paciente realiza ejercicios en casa?": "frecuencia_dificultad_observada_fisioterapeutas.csv",
    "7. Que aspectos toma en cuenta para saber si un ejercicio fue realizado correctamente?": "frecuencia_criterios_ejercicio_correcto_fisioterapeutas.csv",
}

PREGUNTAS_MULTISELECCION = {
    "14. Que informacion considera mas privada y debe protegerse?": "frecuencia_informacion_considerada_privada.csv",
    "15. Quien deberia poder ver el avance terapeutico?": "frecuencia_quien_deberia_ver_avance.csv",
}


def leer_datos():
    with open(PROCESSED, "r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def tabla_simple(datos, columna):
    conteo = {}
    for fila in datos:
        val = fila.get(columna, "").strip()
        if val:
            conteo[val] = conteo.get(val, 0) + 1
    return conteo


def tabla_multiseleccion(datos, columna):
    conteo = {}
    for fila in datos:
        val = fila.get(columna, "").strip()
        if not val:
            continue
        for opcion in val.split(","):
            opcion = opcion.strip()
            if opcion:
                conteo[opcion] = conteo.get(opcion, 0) + 1
    return conteo


def escribir_tabla(conteo, ruta, total_respuestas):
    with open(ruta, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["opcion", "cantidad", "porcentaje_sobre_respuestas"])
        for opcion in sorted(conteo, key=lambda k: -conteo[k]):
            pct = round(100 * conteo[opcion] / total_respuestas, 1) if total_respuestas else 0
            writer.writerow([opcion, conteo[opcion], pct])


def main():
    datos = leer_datos()
    RESULTS.mkdir(parents=True, exist_ok=True)
    generados = 0

    for columna, archivo in PREGUNTAS_SIMPLES.items():
        if columna not in datos[0]:
            continue
        conteo = tabla_simple(datos, columna)
        if not conteo:
            continue
        total = sum(conteo.values())
        escribir_tabla(conteo, RESULTS / archivo, total)
        print(f"OK: {archivo} ({total} respuestas)")
        generados += 1

    for columna, archivo in PREGUNTAS_MULTISELECCION.items():
        if columna not in datos[0]:
            continue
        conteo = tabla_multiseleccion(datos, columna)
        if not conteo:
            continue
        respondientes = sum(1 for fila in datos if fila.get(columna, "").strip())
        escribir_tabla(conteo, RESULTS / archivo, respondientes)
        print(f"OK: {archivo} ({respondientes} respondientes, opción múltiple)")
        generados += 1

    print(f"Total de tablas de frecuencia generadas: {generados}")


if __name__ == "__main__":
    main()
