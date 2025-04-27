"""
7.- Encontrar la longitud de la palabra más larga en una lista
Pista: Existe una función llamada max() -> investiga para poder resolverlo.
"""

lista_palabras = ["hola", "renato", "crepúsculo", " te quiero", "terrenal"]

palabra = max(lista_palabras, key=len)
print("la palabra mas larga es =>", {palabra})

# TODO: Ahora hazlo con ciclos.
