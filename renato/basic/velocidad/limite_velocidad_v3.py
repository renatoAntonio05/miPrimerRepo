velocidad_permitida_1 = 120
velocidad_auto_1 = 90


def validar_limite_velocidad_v2(velocidad_permitida, velocidad_auto):
    if velocidad_permitida > velocidad_auto:
        return True
    else:
        return False


is_limit = validar_limite_velocidad_v2(velocidad_permitida_1, velocidad_auto_1)

if is_limit:
    print('Estas dentro del limite de velocidad')
else:
    print('Estas fuera del limite de velocidad')
