"""6.- Encontrar el número máximo en una lista sin usar funciones incorporadas """
# tengo la duda de cual de las dos formas es la que quieres

lista_num= [1,20,5,2,39,56,1323]
print(max(lista_num))

#---------------------------------------------

mayor = lista_num[0]
for num in lista_num:
    if num > mayor:
        mayor = num
print(f"El numero mayor de la lista es {mayor}")



