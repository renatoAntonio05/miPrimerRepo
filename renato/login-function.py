from helpers import validation_not_empty as validation


# Esta es una funcion para login de un usuario.
def validation_email_password(email_db,password_db,email_input,password_input):
    if email_db.strip().lower() == email_input.strip().lower():
        if password_db == password_input:
            print('Bienvenido')
        else:
            print('Email o contraseña es incorrectos')
    else:
        print('No ingresaste Email o contraseña correcto')


email_user_db = "tony2@gmail.com"
password_user_db= "12345"

name_user = input('ingresa tu usuario-> ').strip().lower()
password = input('ingresa tu password-> ')

# Validar que el email no venga vacio.
validation.validation_not_empty(name_user,'Falta usuario')

# Validar que la contraseña no venga vacia.
validation.validation_not_empty(password,'Falta enviar una contraseña')

validation_email_password(email_user_db,password_user_db,name_user,password)

