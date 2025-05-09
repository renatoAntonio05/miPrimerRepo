
class Operaciones:

    def __init__(self,num1,num2):
        self.num1 =  num1
        self.num2 = num2

    def suma(self):
        return  self.num1 + self.num2

    def resta(self):
        return self.num1 - self.num2

    def multiplicacion(self):
        if self.num1 != 0 and self.num2 !=0:
            return self.num1 * self.num2
        else:
            print("No se puede mulplicar un numero por cero")

    def division(self):
        if self.num1 !=0 and self.num2 != 0:
            return self.num1 / self.num2
        else:
            print("No se puede dividir numeros entre cero")



num1 = 10
num2 = 10

operacion = Operaciones(num1, num2)

print("Suma:", operacion.suma())
print("Resta:", operacion.resta())
print("multiplicacion:", operacion.multiplicacion())
print("division:", operacion.division())
