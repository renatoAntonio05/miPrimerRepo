valor1 = 2
valor2 = 4(1, 2, 3, 4, )

# 1 * 2 = 2
# 2 * 2 = 4
# 2 * 4 = 8
# 2 * 8 = 16


print("1) calcular ppotencia de los numeros que se ingresaron")

respuesta = input("selecciones una opcion: ")

if respuesta == "1":
    veces = valor2 - 1

    print('veces: ', veces)

    resultado = valor1
    print('resultado', resultado)

    while veces > 0:  # se ejecuta 3 veces.
        resultado = resultado * valor1
        # 2 * 2 = 4 ( interacion 1)
        # 4 * 2 = 8 (interacion 2)
        # 8 * 2 = 16 (interacion 3)
        # resultado = 4
        # resultado = 8
        # resultado = 16
        veces = veces - 1
    #     veces = 3 - 1 = 2
    #     veces = 2 - 1 = 1
    #     veces = 1 - 1 = 0
    print(resultado)
