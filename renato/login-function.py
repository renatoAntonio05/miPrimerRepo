from helpers import validation_not_empty as validation
from helpers import validation_email_password as verificacion




email_user_db = "tony2@gmail.com"
password_user_db= "12345"

name_user = input('ingresa tu usuario-> ').strip().lower()
password = input('ingresa tu password-> ')

# Validar que el email no venga vacio.
validation.validation_not_empty(name_user,'el valor debe tener algo')

# Validar que la contraseña no venga vacia.
validation.validation_not_empty_default_message(password)

verificacion.validation_email_password(email_user_db,password_user_db,name_user,password)

