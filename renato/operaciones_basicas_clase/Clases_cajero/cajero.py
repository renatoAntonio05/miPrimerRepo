class Cajero:
    def __init__(self, dinero_total):
        self.dinero_total = dinero_total
        self.movimientos = []
    def menu_cajero(self):
        while True:
            print("Bienvenido, Elige una opcion: ")
            print("1 Efectuar un retiro")
            print("2 Ingresar dinero")
            print("3 Mostrar tu saldo")
            print("4 Mostrar Movimientos")
            print("5 Salir")
            option = input("Ingresa tu opcion=> ")
            print("--------------------------------")

            if option not in ["1", "2", "3", "4", "5"]:
                print("Esa opción no es válida")
                print("Vuelve a intentarlo")
                print("---------------------")
                continue  # Para volver a mostrar el menú

            if option == "1":
                retirar_dinero = int(input("Ingresa la cantidad que deseas retirar=> "))
                if retirar_dinero <= self.dinero_total:
                    print("Toma tu dinero")
                    self.dinero_total -= retirar_dinero
                    self.movimientos.append(f"Retiro: -{retirar_dinero}")
                else:
                    print("No tienes saldo suficiente")

            elif option == "2":
                ingresar_dinero = int(input("Ingresa el efectivo=> "))
                self.dinero_total += ingresar_dinero
                self.movimientos.append(f"Ingreso: +{ingresar_dinero}")
                print("Tu dinero ha sido ingresado")

            elif option == "3":
                print("Tu nuevo saldo es:", self.dinero_total)

            elif option == "4":
                print("Movimientos:")
                for movimiento in self.movimientos:
                    print(movimiento)

            elif option == "5":
                print("Saliste del menú")
                break  # Mejor que exit()

cajero = Cajero(1000)
cajero.menu_cajero()