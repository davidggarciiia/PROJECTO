from ASIENTOS import asientos


print("---BIENVENIDO AL CINEBICHO---")
# muestra_peliculas
#slecciona_pelicula
#muestra_horarios

#Muestra matriz de asientos y cuales estan disponibles
asientos.mostrar_asientos()
#Selecciona el asiento que el usuario quiere comprar 
asientos.seleccionar_asiento(asientos.FILAS, asientos.COLUMNAS)

# Mostrar los asientos actualizados
asientos.mostrar_asientos()

# Bucle para comprar múltiples asientos
while True:
    # Solicitar fila y columna al usuario
    fila = int(input("Ingrese el número de fila: "))
    columna = int(input("Ingrese el número de columna: "))
    
    # Intentar seleccionar el asiento
    asientos.seleccionar_asiento(fila, columna)
    
    # Preguntar si quiere comprar más asientos
    respuesta = input("\n¿Desea comprar otro asiento para esta película? (s/n): ").lower()
    
    if respuesta != 's':
        break
    
    # Mostrar asientos actualizados antes de la siguiente compra
    print("\n")
    asientos.mostrar_asientos()

# Mostrar el estado final de los asientos
print("\n--- Estado final de los asientos ---")
asientos.mostrar_asientos()
print("\n¡Gracias por su compra!")