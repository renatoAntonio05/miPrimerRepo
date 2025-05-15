

class Car:
    def __init__(self, nombre):
        self.nombre = nombre
        self.available = True

    def reservar(self):
        if self.available:
            self.available = False
            print(f"El auto {self.nombre} ha sido vendido")
        else:
            print(f"El auto {self.nombre} no está disponible")


class Buyer:
    def __init__(self, name):
        self.name = name
        self.autos_comprados = []

    def comprar_auto(self, auto):
        if auto.available:
            auto.reservar()
            self.autos_comprados.append(auto)
        else:
            print(f"El auto {auto.nombre} no está disponible")


class Concesionaria:
    def __init__(self):
        self.autos = []
        self.compradores = []

    def agregar_auto(self, auto):
        self.autos.append(auto)
        print(f"El auto {auto.nombre} esta en el inventario")

    def registrar_comprador(self, comprador):
        self.compradores.append(comprador)
        print(f"{comprador.name} se ha registrado como comprador")

    def autos_disponibles(self):
        print("Los autos disponibles son:")
        for auto in self.autos:
            if auto.available:
                print(f" {auto.nombre}")

    def vender_auto(self, comprador, auto):
        if auto in self.autos and self.compradores:
            auto.reservar()
            comprador.autos_comprados.append(auto)
            self.autos.remove(auto)
        else:
            print(f"El auto {auto.nombre} no está disponible o no está en el inventario")


concesionaria = Concesionaria()

auto1 = Car("ford")
auto2 = Car("Seat")
auto3 = Car("lobo")

comprador1 = Buyer("Renato Antonio Poblano")
comprador2 = Buyer("Jose Antonio Perez")

concesionaria.registrar_comprador(comprador1)
concesionaria.registrar_comprador(comprador2)

concesionaria.agregar_auto(auto1)
concesionaria.agregar_auto(auto2)
concesionaria.agregar_auto(auto3)
# esta línea de código es para ver autos disponibles
concesionaria.autos_disponibles()

# El comprador quiere comprar un auto
comprador1.comprar_auto(auto1)

concesionaria.vender_auto(comprador1, auto1)
