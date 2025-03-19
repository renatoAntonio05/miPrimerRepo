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
# 6. No se admiten espacios vasios


# Este bucle tiene una condicional para cerciorarse que los campos no vayan en blanco.
while True:
    name_user = input('ingresa tu usuario-> ').strip().lower()
    if name_user:
        break
    print('no se admiten espacios vacios')

# Esta bucle tiene una condicional para cerciorarse que los campos no vayan en blanco.
while True:
    password = input('ingresa tu password-> ').strip()
    if password:
        break
    print('no se admiten espacios vacios')

if name_user.strip().lower() == email_user_db.strip().lower():
    if password == password_user_db:
        print('Bienvenido')
    else:
        print('Email o contraseña es incorrectos')
else:
    print('No ingresaste Email o contraseña correcto')




