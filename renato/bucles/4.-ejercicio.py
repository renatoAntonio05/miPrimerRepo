"""
Genera un número aleatorio del 1 al 100 y permite al usuario adivinar. Da pistas (“más alto” o “más bajo”) hasta que lo adivine.
"""

"""
        ?##### PASOS PARA RESOLVER EL PROBLEMA. #####
        
    Generar un número rando que este entre 1 y 100 (int)
    Recibir un numero del usuario. (str -> int) (str != int)
    Validar que sea el mismo numero.
        Si es el mismo numero: ganaste. (Condicional)
        Si no es el mismo numero y es mas grande: el numero es mas pequeño. (Condicional)
        Si no es el mismo numero y es mas pequeño: el numero es mas grande. (Condicional)
"""

"""
    Agregar un numero de intentos y validar que no supere esos limites.
    5 intentos.
    Tienes que hacer un contador que sume cada vez que falle y si supera el numero de intentos decirle cual es el 
    numero y decirle que perdio.
"""

import random

numero_aleatorio = random.randint(1, 100)

#se agregaron dos variables para verificar el numero de intentos
intentos = 0

max_intentos = 5

while intentos < max_intentos:
    numero_usuario = int(input('ingresa el numero: '))
    intentos += 1
    if numero_usuario < numero_aleatorio:
        print('El número es más grande.')
    elif numero_usuario > numero_aleatorio:
        print('El número es más pequeño.')
    elif numero_usuario == numero_aleatorio:
        print('¡Ganaste, felicidades!')
        break
# le agregue esta condicional para verificar el numero de intentos.
if intentos == max_intentos:
    print("superaste el numero intentos el numero ganador es", numero_aleatorio, "Has perdido")
