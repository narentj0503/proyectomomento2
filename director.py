class Director:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Pelicula:
    directores = {}

    def agregar_director(self, nombre_director, apellido_director):
        director = Director(nombre_director, apellido_director)
        self.directores[(nombre_director, apellido_director)] = director
        print(f"Director {director} agregado correctamente.")

    def mostrar_directores(self):
        print("Directores:")
        for director in self.directores.values():
            print(director)
