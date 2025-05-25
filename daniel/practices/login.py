# Este archivo nos permite validad el emial y contraseña del usuario

email_user = "daniel23.da74@gmail.com"
password_user= "12345678"

email_user_db = "daniel23.da74@gmail.com"
password_user_db= "12345678"

if email_user == email_user_db:
    if password_user == password_user_db:
        print("Bienvenido")
    else:
        print("Contraseña incorrecta")
else:
    print("Email incorrecto")
