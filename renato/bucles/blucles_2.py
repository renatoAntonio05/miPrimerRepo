# es el conjunto de frutas

frutas = ["manzana", "naranja", "piña", "sandia", "pera", "melon", "platano", "papaya", "naranja", "guayaba", "mango"]

# inicializamos el tamaño de la varible
index_of_frutas = 0

# con el for recorremos la lista
for fruta in frutas:
    # incrementa la variable en cada bucle
    index_of_frutas = index_of_frutas + 1

    # se imprime el elemento de la lista y el tamaño
    print('indice de la fruta es: ', index_of_frutas, 'nombre fruta:', fruta)

print('-------------------------------------------------------------')
########################################################################################################

# la lista se opcupa un varible
len_mylist = len(frutas)

# el otro metodo es mediante un ciclo
for x in range(len_mylist):
    print('Nombre de la fruta:', frutas[x])

print("--------------------------------------------------------------")

########################################################################################################
# este codigo se cuentan los elementos de cada uno de los strings
# total_caracteres sera la variable con la que se guardan lo recorrido por el ciclo
total_caracteres = 0
# el ciclo que recorre la lista
for fruto in frutas:
    # con esta linea de codigo se cuenta los caractres de cada uno de los string
    total_caracteres = len(fruto)
    # con esta condicion se imprime unicamnete las palabras que son mayores a
    if total_caracteres >= 7:
        # se imprime el resultado
        print('Fruta que tiene mas de 7 caracteres:', fruto)
