# Configuración de la sala
FILAS = 5
COLUMNAS = 6

# Crear matriz de asientos (True = disponible, False = ocupado)
asientos = [] #Estas son las columnas
for _ in range(FILAS):
    fila = []
    for _ in range(COLUMNAS):
        fila.append(True)

    asientos.append(fila)

def mostrar_asientos():
    print("💺 Mapa de asientos (X = ocupado, _ = disponible):\n")
    print("----La pantalla esta aqui----\n")
    for i, fila in enumerate(asientos): #Itera la array de asientos y una i para que se vean las filas del cine
        fila_str = f"Fila {i+1}: "
        for asiento in fila:
            if asiento==True:
                fila_str += " _ "
            else:
                fila_str += " X "
        print(fila_str)
    print()

def seleccionar_asiento(fila, columna):
    if fila > FILAS or columna > COLUMNAS: #Si fila o columna esta fuera del rango
        print("Asiento fuera de rango.")
        return False
    if asientos[fila-1][columna-1]==False: #Si ya esta ocupado
        print("Asiento ya ocupado.")
        return False
    asientos[fila-1][columna-1] = False
    print(f"Asiento {fila}-{columna} reservado con éxito.")
    return True

