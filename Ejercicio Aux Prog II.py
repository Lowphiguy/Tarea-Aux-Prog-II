#Acho Lugarani Emanuel Adrian
class Anime:
    def __init__(self, nombre, genero, nroEpisodios):
        self.nombre = nombre
        self.genero = genero
        self.__nroEpisodios = nroEpisodios
        self.__episodios = []

    def __str__(self):
        return f"Anime(nombre={self.nombre}, genero={self.genero}, nroEpisodios={self.__nroEpisodios})"


class Televisor:
    def __init__(self, marca=None, resolucion=None, tipo=None):
        self.__marca = marca
        self.__resolucion = resolucion
        self.__tipo = tipo

    def __str__(self):
        return f"Televisor(marca={self.__marca}, resolucion={self.__resolucion}, tipo={self.__tipo})"
    

class Instrumento:
    def __init__(self, nombre, material, tipo):
        self.nombre = nombre
        self.__material = material
        self.__tipo = tipo

    def getMaterial(self):
        return self.__material

    def getTipo(self):
        return self.__tipo

    def setMaterial(self, material):
        self.__material = material

    def setTipo(self, tipo):
        self.__tipo = tipo

    def __str__(self):
        return f"Instrumento(nombre={self.nombre}, material={self.__material}, tipo={self.__tipo})"
    


a1 = Anime("Dragon Ball Z", "Shonen", 550)
a2 = Anime("Wonder Egg Priority", "Suspenso", 12)

t1 = Televisor("Samsung", 55, "OLED")
t2 = Televisor("LG", 65, "IPS")

i1 = Instrumento("Guitarra", "Madera", "Cuerda")
i2 = Instrumento("Flauta", "Metal", "Aire")

print(a1)
print(a2)

print(t1)
print(t2)

print(i1)
print(i2)