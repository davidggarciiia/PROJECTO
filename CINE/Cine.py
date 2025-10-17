from ASIENTOS import asientos


print("---BIENVENIDO AL CINEBICHO---")

asientos.mostrar_asientos()


while True:
    asiento_propuesto = asientos.proponer_mejor_asiento()
    print(f"Se le propone el asiento más centrado disponible: Fila {asiento_propuesto[0]}, Columna {asiento_propuesto[1]}")
    
    fila = int(input("Ingrese el número de fila: "))
    columna = int(input("Ingrese el número de columna: "))
    
    asientos.seleccionar_asiento(fila, columna)
    
    respuesta = input("\n¿Desea comprar otro asiento para esta película? (s/n): ").lower()
    
    if respuesta != 's':
        break
    
    print("\n")
    asientos.mostrar_asientos()

print("\n¡Gracias por su compra!")