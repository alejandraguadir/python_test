# codeisy_runner.py

import os
from codeisy_runner import Codeisy

# Ruta al archivo que quieres analizar
archivo = "automation_test/calculadora.py"

# Inicializa Codeisy
analizador = Codeisy()
resultado = analizador.analizar_archivo(archivo)

# Imprime funciones sin test
print("Funciones sin pruebas:")
for funcion in resultado["sin_pruebas"]:
    print(f"- {funcion}")
