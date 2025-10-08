from pelicula import Pelicula


def mostrar_todas(peliculas):
    print("-----------CARTELERA-------------")
    for pelicula in peliculas:
        pelicula.show_movie_info()
        print("-------------------------------")


peliculas = [
        Pelicula("Inception", "Christopher Nolan", 2010, ["18:00", "20:30", "22:45"]),
        Pelicula("Interstellar", "Christopher Nolan", 2014, ["17:00", "21:00"]),
        Pelicula("Parasite", "Bong Joon-ho", 2019, ["16:30", "19:30", "22:00"])
    ]
mostrar_todas(peliculas)