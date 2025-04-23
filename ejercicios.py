"""
1.- Crear una función que devuelva el cuadrado de un número.
Pista: Investigar como hacer al cuadrado un número.

def cuadrado(numero):
    numero_cuadrado = numero ** 2
    print(f"El resultado es =>",numero_cuadrado)

cuadrado(10)"""


"""# 2.- Verificar si un número es positivo, negativo o cero

# lo hice en un ciclo para poder verificar una infinidad de veces 

while True:
    numero = int(input("Ingresa el numero =>"))
    if numero >= 1:
        print("El numero es positivo")
    elif numero <=-1:
        print("El numero es negativo")
    elif numero ==0:
        print("El numero es cero") """


"""
#3.- Crear una lista de números pares del 1 al 20 usando un bucle
#Pista:
   # - Recuerda como saber que es un número par.
   # - Recuerda que debes agregarlo en una lista.


for numero in range(1,21):
    if numero %2 ==0:
        print(numero)
"""

"""
#4.- Contar el número de vocales en una cadena de texto
#Pista: Debemos tener un contador que guarde el numero de vocales.

palabras = input("Ingresa el texto=>")
vocales = "aeiouAEIOU"
contador = 0

for palabra in palabras:
    if palabra in vocales :
        contador +=1
print(f"El texto tiene {contador} vocales")

"""

"""
#5.- Crear una función que verifique si una lista está vacía
#Pista: Recuerda como debemos saber la logitud de una lista.

def verificador(lista_a):
    if not len(lista_a):
        print("la lista esta vacía")
    else:
        print(lista_a)



verificador(["hola"])"""



"""
# 6.- Encontrar el número máximo en una lista sin usar funciones incorporadas
# tengo la duda de si es asi ejeje
# foma uno
lista_num = [1, 45, 20, 46, 55, 100, 200]
# max sirve para encontrar el valro mas grande
num_mayor = max(lista_num)
print(num_mayor)

# nota lei que esta son funciones incoporadas
#forma dos
mayor = lista_num[0]

for num in lista_num:
    if num > mayor:
        mayor = num
print(mayor) """



"""
# 7.- Encontrar la longitud de la palabra más larga en una lista
#Pista:  existe una funcion llamada max() -> investiga para poder resolverlo.
# key = len se usa como parametro para que se pueda medir el largo delas palabras y ni su valor unicode
lista_palabras = ["hola","renato","crepusculo"," te quiero", " dentro de este cuento de terror"]

palabra_larga = max(lista_palabras, key=len)
print("La palabra mas larga es =>",palabra_larga)


"""



