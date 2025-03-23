import re

def validar_correo(messenger):
    patron = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
    if re.match(patron, messenger):
        return bool(re.match(patron, messenger))

