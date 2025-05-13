class Cajero:
    # se define el constructor
    def __init__(self, dinero_total):
        self.dinero_total = dinero_total
        self.movimientos = []

    def retirar_dinero(self):
        retirar_dinero = int(input("monto a retirar=> "))
        if retirar_dinero <= self.dinero_total:
            print("Toma tu efectivo")
            self.dinero_total -= retirar_dinero
            self.movimientos.append(f"Retiro:, - {retirar_dinero}")
        else:
            print("Saldo insuficiente")

    def ingresar_dinero(self):
        ingresar_dinero = int(input("Ingresa el efectivo=>    "))
        self.dinero_total += ingresar_dinero
        self.movimientos.append(f"ingresos: + {ingresar_dinero}")  # se usa esta varible para almacenar todos ingresos
        print("Tu dinero a sido ingresado")

    def mostrar_saldo(self):
        print(f"Saldo actual es:, {self.dinero_total}")

    def mostrar_movimiento(self):
        if not self.movimientos:
            print("Aun no hay movimientos")
        else:
            print("movimientos")
            for mov in self.movimientos:
                print(mov)


cajero1 = Cajero(1000)

while True:
    print("Bienvenido, Elige una opcion: ")
    print("1 Efectuar un retiro")
    print("2 Ingresar dinero")
    print("3 Mostrar tu saldo")
    print("4 Mostrar Movimientos")
    print("5 Salir")
    option = input("ingresa tu opcion =>  ")

    print("--------------------------------------")

    if option == "1":
        cajero1.retirar_dinero()
    elif option == "2":
        cajero1.ingresar_dinero()
    elif option == "3":
        cajero1.mostrar_saldo()
    elif option == "4":
        cajero1.mostrar_movimiento()
    elif option == "5":
        print("Gracias por usar tu cajero")
        break
    else:
        print("Opción inválida, vuelve a intentarlo.")
