#2.- Verificar si un número es positivo, negativo o cero
# lo hice en un ciclo para poder verificar una infinidad de veces
while True:
    verificador_numero = int(input("ingresa el numero a verificar=> "))
    if verificador_numero >= 1:
        print("El numero es positivo")
    elif verificador_numero <= -1:
        print("El numero es negativo")
    elif verificador_numero == 0:
        print("El numero es cero")
