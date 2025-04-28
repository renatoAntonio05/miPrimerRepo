"""
7.- Encontrar la longitud de la palabra más larga en una lista
Pista: Existe una función llamada max() -> investiga para poder resolverlo.
"""

lista_palabras = ["hola", "renato", "crepúsculo", " te quiero", "terrenal"]

palabra = max(lista_palabras, key=len)
print("la palabra mas larga es =>", {palabra})

# TODO: Ahora hazlo con ciclos.
palabra_nombre = ''

# cliclo que recorra toda la lista
# Saber que tan grande es la palabra que esta recorriendo
# Comprar con la logitud de la palabra recorrida con palabra_nombre
