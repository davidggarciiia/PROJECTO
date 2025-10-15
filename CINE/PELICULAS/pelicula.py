class Pelicula:
    def __init__(self, titulo,director,año,horarios):
        self.titulo = titulo
        self.director = director
        self.año = año
        self.horarios = horarios
        # self.tipo = tipo
    
    def show_movie_info(self):
        print(f"{self.titulo} \nDirector: {self.director} \nAño: {self.año} ")
    