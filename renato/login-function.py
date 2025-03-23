from helpers import validation_not_empty as validation
from helpers import validation_email_password as verificacion
from helpers import get_info_input as inputs
from helpers import  get_info_db as db
from helpers import validacion_correo as correo

values = db.get_info_db()

name_user = inputs.get_information_email_input('Ingresa tu email:')


password = inputs.get_information_input('Ingresa tu password:')

# se llama a la funcion validacion de corroe
correo.validar_correo(name_user)


# Validar que el email no venga vacio.
validation.validation_not_empty(name_user,'el valor debe tener algo')

# Validar que la contraseña no venga vacia.
validation.validation_not_empty_default_message(password)

verificacion.validation_email_password(values['email'],values['password_user_db'],name_user,password)

