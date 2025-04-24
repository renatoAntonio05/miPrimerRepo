#1.- Crear una función que devuelva el cuadrado de un número.
#Pista: Investigar como hacer al cuadrado un número.

numero_elevar = int(input("ingresa el numero=> "))

def cuadrado(numero):
    numero_cuadrado = numero ** 2
    print(f"El resultado es => ",numero_cuadrado)

cuadrado(numero_elevar)