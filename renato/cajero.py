# mostrar valance
# sacar dinero guardar el monto
# depositar dinero
# guardar el historia de los movimientos
# sacar valance de cuanto dinero saco e ingreso


def menu_cajero(dinero_total, movimientos):
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
            print("Esa opcion no es valida")
            print("vuleve a intentarlo")
            print("---------------------")

        if option == "1":
            retirar_dinero = int(input("ingresa la cantidad que deseas retirar=>   "))
            if retirar_dinero <= dinero_total:
                print("Toma tu dinero")
                dinero_total -= retirar_dinero
                movimientos.append(f"retiros -{retirar_dinero}")  # esta varibale es para almacenar todos retiros
            else:
                print("No tienes Saldo suficiente")

        if option == "2":
            ingresar_dinero = int(input("Ingresa el efectivo=>    "))
            dinero_total += ingresar_dinero
            movimientos.append(f"ingresos: + {ingresar_dinero}")  # se usa esta varible para almacenar todos ingresos
            print("Tu dinero a sido ingresado")

        if option == "3":
            print("Tu nuevo saldo es", dinero_total)

        if option == "4":
            for movimiento in movimientos:
                print(movimiento)

        if option == "5":
            print("Saliste del menu")
            exit()


dinero_total = 1000
movimientos = []

menu_cajero(dinero_total, movimientos)
