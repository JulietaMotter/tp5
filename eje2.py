import os

# Directorio "/dev"
directorio_dev = "/dev"

# Verificar si el directorio "/dev" existe
if os.path.exists(directorio_dev) and os.path.isdir(directorio_dev):
    # Obtener todos los nombres de archivo y directorio en "/dev"
    contenido_dev = os.listdir(directorio_dev)
    
    # Filtrar solo los directorios
    directorios_dev = [nombre for nombre in contenido_dev if os.path.isdir(os.path.join(directorio_dev, nombre))]
    
    # Imprimir los directorios encontrados
    if directorios_dev:
        print("Directorios dentro del directorio /dev:")
        for directorio in directorios_dev:
            print(directorio)
    else:
        print("No se encontraron directorios dentro del directorio /dev.")
else:
    print("El directorio /dev no existe o no es un directorio en este sistema.")
