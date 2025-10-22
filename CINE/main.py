from PELICULAS.peliculas_disponibles import peliculas_disponibles
from PELICULAS.peliculas_utils import seleccionar_pelicula_y_horario
from DESCUENTOS.descuento import gestionar_descuento
from ASIENTOS.asientos import seleccionar_asientos
from TICKET.ticket import generar_ticket

def main():
    print("---BIENVENIDO AL CINEBICHO---")

    # Seleccionar película y horario
    pelicula_seleccionada, horario = seleccionar_pelicula_y_horario(peliculas_disponibles)

    # Gestionar descuento
    precio_base = 10.0
    precio_final = gestionar_descuento(precio_base)

    # Seleccionar asientos
    asientos_seleccionados = seleccionar_asientos()

    # Generar ticket
    generar_ticket(pelicula_seleccionada, asientos_seleccionados, precio_final)

if __name__ == "__main__":
    main()