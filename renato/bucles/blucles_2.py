# es el conjunto de frutas

frutas = ["manzana", "naranja", "piña", "sandia", "pera", "melon", "platano", "papaya", "naranja", "guayaba", "mango"]

# inicializamos el tamaño de la varible
size = 0
# con el for recorremos la lista
for fruta in frutas:
    # incrementa la variable en cada bucle
    size = size + 1  # TODO: esto lo haces para saber cual es el index de las frutas
    # se imprime el elemento de la lista y el tamaño
    print(size, fruta)

########################################################################################################
# la lista se opcupa un varible
len_mylist = len(frutas)
# el otro metodo es mediante un ciclo
for x in range(len_mylist):
    print(frutas[x])

########################################################################################################
# este codigo se cuentan los elementos de cada uno de los strings
# total_caracteres sera la variable con la que se guardan lo recorrido por el ciclo
total_caracteres = 0
# el ciclo que recorre la lista
for fruto in frutas:
    # con esta linea de codigo se cuenta los caractres de cada uno de los string
    # TODO: Esta bien solo que quiero que imprimas las que tiene 7 o mas caracteres.
    # TODO: Tenemos que hacer una validación
    total_caracteres = len(fruto)
    # se imprime el resultado
    print(total_caracteres)
