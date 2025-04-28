class Persona:
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def saluda(self):
        print('Hola', self.name)

    def edad(self):
        print('Mi edad es:', self.age)


# Clase
person1 = Persona('Daniel', 25)
person2 = Persona('Renato', 50)

# person1.saluda()
# person1.edad()

# person2.saluda()
# person2.edad()

"""
POO: Pilares de programación

Abstracion: Solo mostrar lo que necesita y oculta la complejidad.
Polimorfismo:
Herencia:
Encapsulamiento:
"""


class Operaciones:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def suma(self):
        print(self.num1 + self.num2)

    def resta(self):
        print(self.num1 - self.num2)


# Objeto de clase
operator = Operaciones(10, 5)

operator.suma()
operator.resta()
