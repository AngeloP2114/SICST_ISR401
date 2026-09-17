"""
orquestar.py

Ejecuta la cadena completa y reproducible del paquete de datos SICST con
una sola orden:

    python 07_Datos/scripts/orquestar.py

Corre, en orden: extracción/validación, limpieza, generación del
diccionario de datos, análisis por perfil, análisis por pregunta, y
generación de checksums. Si algún paso falla, el orquestador se detiene
inmediatamente.
"""
import subprocess
import sys
from pathlib import Path
import importlib.util


def asegurar_dependencias():
    if importlib.util.find_spec("matplotlib") is None:
        requirements = Path(__file__).resolve().parents[1] / "requirements.txt"

        print("Dependencia faltante: matplotlib")
        print("Instalando dependencias de 07_Datos...")

        subprocess.run(
            [
                sys.executable,
                "-m",
                "pip",
                "install",
                "-r",
                str(requirements),
            ],
            check=True,
        )




CARPETA = Path(__file__).resolve().parent

PASOS = [
    "01_extraer_crudos.py",
    "02_limpiar_datos.py",
    "03_generar_diccionario.py",
    "04_analisis_por_perfil.py",
    "05_analisis_por_pregunta.py",
    "07_analisis_cruzado.py",
    "09_analisis_cualitativo.py",
    "08_generar_figuras.py",
    "10_generar_manifiesto.py",
    "06_generar_checksums.py",  # checksums siempre al final, tras generar todo
]


def main():
    asegurar_dependencias()
    for paso in PASOS:
        print(f"\n=== Ejecutando {paso} ===")
        resultado = subprocess.run([sys.executable, str(CARPETA / paso)])
        if resultado.returncode != 0:
            print(f"\nERROR: el paso {paso} falló. Cadena detenida.", file=sys.stderr)
            sys.exit(resultado.returncode)

    print("\nCadena reproducible SICST (07_Datos) ejecutada correctamente.")


if __name__ == "__main__":
    main()
