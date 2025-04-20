# menu donde muestres las cuatro opciones
# la primera es que agregue un número y no permitir valores repetidos
# segunda que pueda eliminar un número
# tercera ver los números
# cuarto sumar valores
# quinto salir del menu.
# primero se delcaran las funciones y luego se ejecutan.
mi_lista = []

def ingresar_numero():
    numero = int(input("ingresa tu numero => "))
    mi_lista.append(numero)
    mi_lista.sort()  # Ordena la lista.
    print(mi_lista)

def eliminar_numero():
    numero_eliminar = int(input("ingresa el numero que deseas eliminar =>"))
    if numero_eliminar in mi_lista:
        mi_lista.remove(numero_eliminar)
        print("El numero que ingresaste si se puede eliminar")
    else:
        print("El numero no esta en la lista no se puede eliminar")


def mostrar_lista():
    print(mi_lista)


def sumar_numeros():
    sumar = 0
    for numero in mi_lista:
        sumar += numero
    print(sumar)

def salir_menu():
    print("Saliste del menu")
    exit()

def mostrar_menu():
    while True:
        print("1 Ingresa un numero")
        print("2 ¿Que numero deseas eliminar?")
        print("3 Mostrar los números que se han ingresado")
        print("4 Suma todos los numeros de la lista")
        print("5 Salir del menu")
        option = input("Elige una opción: ")
        if option not in ["1","2","3","4","5"]:
            print("Esa opcion no es valida")
            print("vuleve a intentarlo")
            print("---------------------")
        if option == "1":
            ingresar_numero()
        if option == "2":
            eliminar_numero()
        if option == "3":
            mostrar_lista()
        if option == "4":
            sumar_numeros()
        if option == "5":
            salir_menu()


mostrar_menu()
