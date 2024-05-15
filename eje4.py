import sys

def calcular_asignacion(sueldo, rango):
    if rango==1:
        asignacion=sueldo * 0.83
    elif rango==2:
        asignacion=sueldo * 1.2
    elif rango==3:
        asignacion=sueldo * 5
    else:
        asignacion = None 
    return asignacion

sueldo = float(sys.argv[1])
rango = int(sys.argv[2])

asignacion=calcular_asignacion(sueldo,rango)

if asignacion is not None:
    print(f"La asignacion del empleado es {asignacion}")
else:
    print ("El rango ingresado no es válido") 