from renato.basic.operaciones_basicas_matematicas.modulo_suma import suma


def menu():
    while True:
        print("Bienvenido al programa de calculadora:")
        print("Selecciona la opción que deseas realizar")
        print("1.- Sumar")
        print("2.- Restar")

        option = input("ingresa la opción que deseas: ")
        num_input_1 = int(input("Ingresa el primero numero: "))
        num_input_2 = int(input("Ingresa el segundo numero: "))

        if option == "1":
            print("Resultado de la suma es: ", suma(num_input_1, num_input_2))
            print("\n")


# Llamamos la función
menu()
