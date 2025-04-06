numero = int(input('numero: '))


def es_par_2(numero):
    if numero % 2 == 0:
        print('es un numero par')
    else:
        print('no es un numero par')


es_par_2(numero)


def es_par(numero):
    return numero % 2 == 0


resultado_2 = es_par(numero)
print(resultado_2)
