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

#import random

numero_aleatorio = random.randint(1, 100)

print(numero_aleatorio)

while True:
    numero_usuario = int(input('ingresa el numero: '))
    if numero_usuario < numero_aleatorio:
        print('El número es más grande.')
    elif numero_usuario > numero_aleatorio:
        print('El número es más pequeño.')
    elif numero_usuario == numero_aleatorio:
        print('¡Ganaste, felicidades!')
    else:
        break






