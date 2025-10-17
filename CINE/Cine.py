from ASIENTOS import asientos
from TICKET.ticket import Ticket  # Importar la clase Ticket

print("---BIENVENIDO AL CINEBICHO---")

asientos.mostrar_asientos()

asientos_seleccionados = []

while True:
    asiento_propuesto = asientos.proponer_mejor_asiento()
    print(f"Se le propone el asiento más centrado disponible: Fila {asiento_propuesto[0]}, Columna {asiento_propuesto[1]}")

    fila = int(input("Ingrese el número de fila: "))
    columna = int(input("Ingrese el número de columna: "))
    
    if asientos.seleccionar_asiento(fila, columna):
        asientos_seleccionados.append((fila, columna))  # Agregar el asiento seleccionado a la lista
    
    respuesta = input("\n¿Desea comprar otro asiento para esta película? (s/n): ").lower()
    
    if respuesta != 's':
        break
    
    print("\n")
    asientos.mostrar_asientos()

# Crear y generar el ticket
ticket = Ticket(pelicula, asientos_seleccionados, precio_total)
ticket.generar_ticket()

print("\n¡Gracias por su compra!")