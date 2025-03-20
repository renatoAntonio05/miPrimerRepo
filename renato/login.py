# Validar que el usuario que se loguea sea el mismo que esta en la base de datos
import password

# Datos de la base de datos
email_user_db = "tony2@gmail.com"
password_user_db= "12345"


# ¿Que vas hacer?
# 1. Pedirle al usuario que ingrese su email (terminal usando input)
# 2. Pedirle al usuario que ingrese su contraseña (terminal usando input)
# 3. Validar que el email y contraseña sean correctos
# 4. Si son correctos imprimir "Bienvenido"
# 5. Si no son correctos imprimir "Email o contraseña incorrectos"
# 6. No se admiten espacios vasios


# Este bucle tiene una condicional para cerciorarse que los campos no vayan en blanco.
# TODO: anota para que sirve cada uno.
# Strip: elimine los espacios vacios
#lower: para que pase todas los caracteres a minusculas
name_user = input('ingresa tu usuario-> ').strip().lower()
password = input('ingresa tu password-> ').strip()

# Validamos que el campo no este vació.
if name_user == '':
    print('Falta usuario')

if password == '':
    print('Flata contraseña')

if name_user.strip().lower() == email_user_db.strip().lower():
    if password == password_user_db:
        print('Bienvenido')
    else:
        print('Email o contraseña es incorrectos')
else:
    print('No ingresaste Email o contraseña correcto')

