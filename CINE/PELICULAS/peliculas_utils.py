from .pelicula import Pelicula  # Importación relativa para evitar errores

def mostrar_todas(peliculas):
    print("-----------CARTELERA-------------")
    for pelicula in peliculas:
        pelicula.show_movie_info()
        print("-------------------------------")

def select_movie(peliculas):
    # Mostrar menú
    print("---- SELECTOR DE PELÍCULAS ----\n")
    for i, pelicula in enumerate(peliculas, start=1):
        print(f"[{i}] {pelicula.titulo}")

    # Pedir selección al usuario
    while True:
        try:
            opcion = int(input("\nSelecciona una película por su número: "))
            if 1 <= opcion <= len(peliculas):
                seleccionada = peliculas[opcion - 1]
                print(f"\nHas seleccionado: {seleccionada.titulo}\n")
                return seleccionada
            else:
                print(f"Por favor, elige un número entre 1 y {len(peliculas)}.")
        except ValueError:
            print("Ha habido un error al leer la película. Escribe un número válido.")

def select_schedule(pelicula):
    # Mostrar horarios disponibles
    print(f"Horarios disponibles para '{pelicula.titulo}':")
    for i, horario in enumerate(pelicula.horarios, start=1):
        print(f"[{i}] {horario}")

    # Pedir selección de horario
    while True:
        try:
            opcion = int(input("\nSelecciona un horario por su número: "))
            if 1 <= opcion <= len(pelicula.horarios):
                horario_seleccionado = pelicula.horarios[opcion - 1]
                print(f"\nHas seleccionado '{pelicula.titulo}' a las {horario_seleccionado}.")
                return horario_seleccionado
            else:
                print(f"Por favor, elige un número entre 1 y {len(pelicula.horarios)}.")
        except ValueError:
            print("Entrada no válida. Escribe un número.")

def seleccionar_pelicula_y_horario(peliculas_disponibles):
    """Muestra las películas disponibles y permite al usuario seleccionar una película y un horario."""
    mostrar_todas(peliculas_disponibles)
    pelicula_seleccionada = select_movie(peliculas_disponibles)
    horario = select_schedule(pelicula_seleccionada)
    return pelicula_seleccionada, horario