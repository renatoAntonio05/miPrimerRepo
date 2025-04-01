"""
Problema: Escribir un programa que reciba una lista de números y imprimir solo los números impares.
"""

"""
Pasos para resolver el problema

1.- Recorremos la lista de números en este caso.
2.- Validamos que los números sean impares. (Crear una validación if/else)
3.- Imprimimos los números que son impares.   
"""

# Array (javaScript) - Python (lista) - contiene futras
frutas = ['manzana', 'mango', 'melon']

# Array (javaScript) - Python (lista) - contiene multiples tipos de variables. (string,int,bolean,float)
other = ['manzana', 1, True, 1.9]

# Array (javaScript) - Python (lista) - contiene números.
numbers = [1, 3, 4, 6, 4, 6, 2, 5, 1, 7, 9, 3, 4, 5]  # -> Valores que contiene la lista.
#         [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13 -> Indices.

"""
Tu puedes acceder a la lista con su indece.
nombre_lista[posicion que quieres]

Ejemplo:
numbers[11] = 3
"""

# El inidce es la posicion de una lista. [0,1,2,3,4,5,6,7.......]

# lista estatica - el tamaño no va a cambiar.
"""
Ejemplo: longitud es de '3'
"""

# lista dinmica - el tamaño cambira.
"""
Ejemplo: longitud es calculada con el len()
"""

# For (Recorer la lista de numeros)
# Recorriendo el lista.
for number in numbers:
    # % -> obtenemos el residuo de una división.
    if number % 2 != 0:
        print('El numero es impar: ', number)

print('----------------------------------------------')
# ---------------------------------------------------------------------------------------
# Accediendo a el indice del arreglo

# Obteniendo la longitud de nuestra lista. (14)
len_numbers = len(numbers)

# Imprimiendo un rango de 0 al numero de logitud de la lista. (14-1 = 13) Recordar que en las listas el indice es 0:
# x tomara los valores del rango -> 0, 1,2,3,4,5,6 .... al fin de rango.
for x in range(len_numbers):
    # numbers[number] -> acceder al arreglo por medio de su indice al lista.
    # numbers[number] = al numero que tiene la lista en esa posicion del indice.
    if numbers[x] % 2 != 0:
        print('El numero es impar: ', numbers[x])
