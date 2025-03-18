# Validar que el usuario que se loguea sea el mismo que esta en la base de datos

# Datos de la base de datos
email_user_db = "daniel23.da74@gmail.com"
password_user_db= "12345678"


# ¿Que vas hacer?
# 1. Pedirle al usuario que ingrese su email (terminal usando input)
# 2. Pedirle al usuario que ingrese su contraseña (terminal usando input)
# 3. Validar que el email y contraseña sean correctos
# 4. Si son correctos imprimir "Bienvenido"
# 5. Si no son correctos imprimir "Email o contraseña incorrectos"

name_user = input('ingresa tu usuario-> ')
password = ""


if name_user.strip().lower() == email_user_db.strip().lower():
    password = input('Ingresa tu contraseña -> ')
    if password == password_user_db:
        print('Bienvenido')
    else:
        print('Email o contraseña es incorrectos')
else:
    print('El usuario no existe')

