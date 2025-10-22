from PELICULAS import peliculas_utils
from PELICULAS import pelicula
from ASIENTOS import asientos
from DESCUENTOS import descuento

print("---BIENVENIDO AL CINEBICHO---")

# Declarar las películas disponibles
peliculas_disponibles = [
    pelicula.Pelicula("Avengers: Endgame","Alvaro",2014, ["15:00", "18:00", "21:00"]),
    pelicula.Pelicula("The Dark Knight","Alvaro",2014, ["16:00", "19:00", "22:00"]),
    pelicula.Pelicula("Inception","Alvaro",2014, ["14:30", "17:30", "20:30"])
]

# Mostrar todas las películas disponibles
peliculas_utils.mostrar_todas(peliculas_disponibles)

# Pide al usuario que seleccione una película y un horario
pelicula_seleccionada = peliculas_utils.select_movie(peliculas_disponibles)
horario = peliculas_utils.select_schedule(pelicula_seleccionada)

# Pregunta por descuentos
precio_entrada = 10.0
print(f"\nEl precio por entrada sin descuento es de {precio_entrada} euros\n")
descuento_opcion = input(f"\nTienes algun descuento especial? (s/n): ")

# Aplicar descuento si es necesario
if descuento_opcion.lower() == 's':
    gestor_descuento = descuento.Descuento()  # Crear instancia
    gestor_descuento.mostrar_opciones()
    tipo_descuento = int(input("Seleccione el tipo de descuento (1-3): "))
    precio_entrada = gestor_descuento.aplicar_descuento(tipo_descuento, precio_entrada)  # ✅ Correcto

asientos.mostrar_asientos()
asientos_seleccionados = []

while True:
    asiento_propuesto = asientos.proponer_mejor_asiento()
    print(f"Se le propone el asiento más centrado disponible: Fila {asiento_propuesto[0]}, Columna {asiento_propuesto[1]}")

    fila = int(input("Ingrese el número de fila: "))
    columna = int(input("Ingrese el número de columna: "))
    
    if asientos.seleccionar_asiento(fila, columna):
        asientos_seleccionados.append((fila, columna))
    
    respuesta = input("\n¿Desea comprar otro asiento para esta película? (s/n): ").lower()
    
    if respuesta != 's':
        break
    
    print("\n")
    asientos.mostrar_asientos()

print("\n¡Gracias por su compra!")