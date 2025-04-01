from renato.basic.operaciones_basicas_matematicas.modulo_multiplicaicon import multiplicacion
from renato.basic.operaciones_basicas_matematicas.modulo_resta import resta
from renato.basic.operaciones_basicas_matematicas.modulo_suma import suma
from renato.basic.operaciones_basicas_matematicas.modulo_division import division


# le agregue el modulo

def menu():
    while True:
        print("Bienvenido al programa de calculadora:")
        print("Selecciona la opción que deseas realizar")
        print("1.- Sumar")
        print("2.- Restar")
        print("3.- Multiplicar")
        print("4.- Division")

        option = input("ingresa la opción que deseas: ")

        if option in ["1", "2", "3", "4"]:
            num_input_1 = int(input("Ingresa el primero numero: "))
            num_input_2 = int(input("Ingresa el segundo numero: "))

            if option == "1":
                print("Resultado de la suma es: ", suma(num_input_1, num_input_2))
                print("\n")
                # os.system('cls' if os.name == 'nt' else 'clear')

            if option == "2":
                print("Resultado de la resta es: ", resta(num_input_1, num_input_2))
                print("\n")

            if option == "3":
                print("Resultado de la multiplicacion es: ", multiplicacion(num_input_1, num_input_2))
                print("\n")

            if option == "4":
                print("Resultado de la division es: ", division(num_input_1, num_input_2))
                print("\n")
        else:
            print('no hay opcion, vuelve a eleguir una correcta')
            print('\n')


# Llamamos la función
menu()
