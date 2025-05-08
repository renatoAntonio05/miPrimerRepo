num1 = 10
num2 = 30


class Sumar:
    def __init__(self,num1,num2):
        self.num1 =  num1
        self.num2 = num2

    def suma(self):
        return  self.num1 + self.num2


suma = Sumar(num1,num2)
print(suma.suma())


class Resta:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 =num2

    def resta(self):
        return self.num1 - self.num2


resta = Resta(num1,num2)
print(resta.resta())


class multiply:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def multiplicacion(self):
        if self.num1 != 0 and self.num2 !=0:
            return self.num1 * self.num2
        else:
            print("No se puede mulplicar un numero por cero")

multiplicacion = multiply(num1,num2)
print(multiplicacion.multiplicacion())



class Division:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def division(self):
        if self.num1 !=0 and self.num2 != 0:
            return self.num1 / self.num2
        else:
            print("No se puede dividir numeros entre cero")


division = Division(num1,num2)
print(division.division())