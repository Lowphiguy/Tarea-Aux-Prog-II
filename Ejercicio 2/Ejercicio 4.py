# Acho lugarani Emanuel Adrian
# Abstracción de bus

class Bus:
    def __init__(self, capacidad):
        self.__capacidad = capacidad
        self.__pasajeros = 0
        self.__precio_pasaje = 1.50
        

    def getCapacidad(self):
        return self.__capacidad
    

    def getPasajeros(self):
        return self.__pasajeros
    

    def subir_pasajeros(self, x):
        if self.__pasajeros + x <= self.__capacidad:
            self.__pasajeros = self.__pasajeros + x
            print("Subieron", x, "pasajeros al bus")
        else:
            print("No hay suficientes asientos disponibles")


    def cobrar_pasaje(self):
        total = self.__pasajeros * self.__precio_pasaje
        print("Total recaudado: Bs.", total)


    def asientos_disponibles(self):
        disponibles = self.__capacidad - self.__pasajeros
        print("Asientos disponibles:", disponibles)


# Programa de prueba
bus1 = Bus(15)
x = int(input("Cuantos pasajeros desean subir al bus: "))
bus1.subir_pasajeros(x)
bus1.cobrar_pasaje()
bus1.asientos_disponibles()