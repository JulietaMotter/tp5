import psutil
from datetime import datetime

def obtener_informacion_sistema():
    # Obtener la hora del sistema
    hora_actual = datetime.now()
    print("Hora del sistema:", hora_actual)

    # Obtener el estado de la memoria RAM
    estado_memoria = psutil.virtual_memory()
    print("Estado de la memoria RAM:")
    print("  Total:", round(estado_memoria.total / (1024 ** 3), 2), "GB")
    print("  Disponible:", round(estado_memoria.available / (1024 ** 3), 2), "GB")
    print("  Usada:", round(estado_memoria.used / (1024 ** 3), 2), "GB")
    print("  Porcentaje de uso:", estado_memoria.percent, "%")

    # Obtener el almacenamiento disponible en la partición "/"
    almacenamiento = psutil.disk_usage("/")
    print("Almacenamiento disponible en la partición '/':")
    print("  Total:", round(almacenamiento.total / (1024 ** 3), 2), "GB")
    print("  Usado:", round(almacenamiento.used / (1024 ** 3), 2), "GB")
    print("  Libre:", round(almacenamiento.free / (1024 ** 3), 2), "GB")
    print("  Porcentaje de uso:", almacenamiento.percent, "%")

# Llamamos a la función para obtener la información del sistema
obtener_informacion_sistema()