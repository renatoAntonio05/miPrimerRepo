"""
4.- Contar el número de vocales en una cadena de texto
Pista: Debemos tener un contador que guarde el numero de vocales

"""

palabras = input("Ingresa el texto => ")
vocales = "aeiouAEIOU"
contador = 0

for palabra in palabras:
    if palabra in vocales:
        contador += 1

print(f"El texto tiene => {contador} vocales")
