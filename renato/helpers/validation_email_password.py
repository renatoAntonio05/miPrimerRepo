# Pasar funcion de validar email y contraseña con la base de datos.

def validation_email_password(email_db,password_db,email_input,password_input):
    if email_db.strip().lower() == email_input.strip().lower():
        if password_db == password_input:
            print('Bienvenido')
        else:
            print('Email o contraseña es incorrectos')
    else:
        print('No ingresaste Email o contraseña correcto')
