from pelicula import Pelicula


def mostrar_todas(peliculas):
    print("-----------CARTELERA-------------")
    for pelicula in peliculas:

        pelicula.show_movie_info()
        print("-------------------------------")

def select_movie(peliculas):
    # Mostrar menú
    print("---- SELECTOR DE PELÍCULAS ----\n")
    for i,pelicula in enumerate(peliculas,start=1):
        print(f"[{i}] {pelicula.titulo}")
    print("\nSelecciona una pelicula su número: ")

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
                # seleccionada.show_movie_info()  # Mostrar la información
                return seleccionada
            else:
                print(f"Por favor, elige un número entre 1 y {len(peliculas)}.")
        except ValueError:
            print("Ha habido un error al leer la película. Escribe un número válido.")

peliculas = [
        Pelicula("Inception", "Christopher Nolan", 2010, ["18:00", "20:30", "22:45"]),
        Pelicula("Interstellar", "Christopher Nolan", 2014, ["17:00", "21:00"]),
        Pelicula("Parasite", "Bong Joon-ho", 2019, ["16:30", "19:30", "22:00"])
    ]
mostrar_todas(peliculas)
select_movie(peliculas)