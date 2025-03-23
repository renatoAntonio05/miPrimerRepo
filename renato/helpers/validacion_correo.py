import re

def validar_correo(email):
    patron = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
    if re.match(patron, email) is None:
        print('Esto no es un correo')
        exit(0)



# return para devolver la informacion