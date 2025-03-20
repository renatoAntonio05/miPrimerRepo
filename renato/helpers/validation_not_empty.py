def validation_not_empty(value, message):
    if value == '':
        print(message)


def validation_not_empty_default_message(value):
    if value == '':
        print('El valor no puede venir vacio')
