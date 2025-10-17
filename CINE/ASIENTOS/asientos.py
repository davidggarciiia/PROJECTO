# Configuración de la sala
FILAS = 5
COLUMNAS = 6

"""Inicializa la matriz de asientos (True = disponible, False = ocupado)"""
asientos = [] #Estas son las columnas
for _ in range(FILAS):
    fila = []
    for _ in range(COLUMNAS):
        fila.append(True)

    asientos.append(fila)

"""Muestra el mapa de asientos"""
def mostrar_asientos():
    print("💺 Mapa de asientos (X = ocupado, _ = disponible):\n")
    print("----La pantalla esta aqui----\n")
    for i, fila in enumerate(asientos):
        fila_str = f"Fila {i+1}: "
        for asiento in fila:
            if asiento==True:
                fila_str += " _ "
            else:
                fila_str += " X "
        print(fila_str)
    print()

"""Selecciona un asiento específico si está disponible"""
def seleccionar_asiento(fila, columna):
    if fila > FILAS or columna > COLUMNAS: 
        print("Asiento fuera de rango.")
        return False
    if asientos[fila-1][columna-1]==False:
        print("Asiento ya ocupado.")
        return False
    asientos[fila-1][columna-1] = False
    print(f"Asiento {fila}-{columna} reservado con éxito.")
    return True

"""Propone el asiento más centrado disponible"""
def proponer_mejor_asiento():

    centro_fila = FILAS // 2 
    centro_columna = COLUMNAS // 2 
    
    mejor_asiento = None 
    menor_distancia = float('inf')  
    
    for i in range(FILAS):
        for j in range(COLUMNAS):
            
            if asientos[i][j]:
                distancia = abs(i - centro_fila) + abs(j - centro_columna)                
                if distancia < menor_distancia:
                    menor_distancia = distancia
                    mejor_asiento = (i + 1, j + 1)  # +1 porque el usuario ve fila/columna desde 1
    
    return mejor_asiento
