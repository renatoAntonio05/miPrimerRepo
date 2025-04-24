"""5.- Crear una función que verifique si una lista está vacía
Pista: Recuerda como debemos saber la logitud de una lista. """


def verificador_lista(lista_a):
    if not len(lista_a):
        print("La lista esta vacía")
    else:
        print(lista_a)


verificador_lista([])