import os

# Ejemplo de uso del módulo os

ruta_actual = os.getcwd()
print("Ruta actual:", ruta_actual)

archivos = os.listdir(ruta_actual)
print("Archivos en la ruta actual:", archivos)
