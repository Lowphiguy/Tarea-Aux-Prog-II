# Acho Lugarani Emanuel Adrian
# Abstracción de servidor de Minecraft
class ServidorMinecraft:
    def __init__(self):
        self.__jugadores = []
        self.__diamantes = []
        self.__capacidad = 10


    def agregar_jugador(self, nombre, diam):
        if len(self.__jugadores) < self.__capacidad:
            self.__jugadores.append(nombre)
            self.__diamantes.append(diam)
            print("Jugador agregado:", nombre)
        else:
            print("El servidor esta lleno")


    def stacks_jugadores(self):
        i = 0
        while i < len(self.__jugadores):
            stacks = self.__diamantes[i] // 64
            print(self.__jugadores[i], "tiene", stacks, "stacks de diamantes")
            i += 1


    def jugador_mas_diamantes(self):
        if len(self.__jugadores) == 0:
            print("No hay jugadores")
            return
        maxdiam = self.__diamantes[0]
        pos = 0
        i = 1
        while i < len(self.__diamantes):
            if self.__diamantes[i] > maxdiam:
                maxdiam = self.__diamantes[i]
                pos = i
            i += 1
        print("Jugador con mas diamantes:", self.__jugadores[pos])


    def total_diamantes(self):
        total = 0
        i = 0
        while i < len(self.__diamantes):
            total += self.__diamantes[i]
            i += 1
        print("Total de diamantes en el servidor:", total)


# Programa de prueba
server = ServidorMinecraft()
n = int(input("Cuantos jugadores deseas agregar (max 10): "))
i = 0
while i < n:
    nombre = input("Nombre del jugador: ")
    diam = int(input("Diamantes del jugador: "))
    server.agregar_jugador(nombre, diam)
    i += 1
server.stacks_jugadores()
server.jugador_mas_diamantes()
server.total_diamantes()