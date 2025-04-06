"""
Pide al usuario un número entero y suma todos sus dígitos usando un ciclo.

En este ejercicio trabajamos con el contenido del input.
"""


# Recibir un número entero. ✅
# Recorrer el número que inserto el usuario. ✅
# Sumar los números.

def suma_valores(total_2, valor):
    print('Subtotal actual es: ', total_2, 'numero sumado es: ', valor)
    return total_2 + int(valor)


numero_ingresado = input('Ingresa un numero: ')

total = 0
for numero in numero_ingresado:
    total = suma_valores(total, numero)

print('Total de la suma es:', total)

print('-------------------------------------------')

len_numeros_ingresados = len(numero_ingresado)
total = 0

for x in range(len_numeros_ingresados):
    total = suma_valores(total, numero_ingresado[x])

print('Total de la suma es:', total)
