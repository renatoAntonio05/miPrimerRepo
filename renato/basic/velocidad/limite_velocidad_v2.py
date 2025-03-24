# Esto es una función (velocidad_auto)
# Lo que esta dentro de los "parentesis" son los parametros de la función. (los parametros se separan por ",")
# Necesitamos 2 valores:
# 1.- Velocidad permitida
# 2.- La velocidad en que va el auto.
def validar_limite_velocidad(velocidad_permitida, velocidad_auto):
    if velocidad_permitida > velocidad_auto:
        print('Esta dentro del limite de velocidad')
    else:
        print('No esta dentro del limite de velocidad,', 'el limite permitido es: ', velocidad_permitida)


# Variables (velocidad_permitida_1,velocidad_auto_1)
velocidad_permitida_1 = 80
velocidad_auto_1 = 120

validar_limite_velocidad(velocidad_permitida_1, velocidad_permitida_1)
print('-------------------------------------------')
validar_limite_velocidad(120, 90)
