import modulo_suma as mas
import modulo_division as division_1
import modulo_resta as modulo_2
import modulo_pares as modulo_3
import modulo_multiplicaicon as modulo_4

num_1 = 53123
num_2 = 5


resultado_1 = mas.suma(num_1, num_2)
print('suma:',resultado_1,)
print("_____________________________________")

resultado_2 = modulo_2.resta(num_1, num_2)
print('Resta:',resultado_2)
print("_____________________________________")


resultado_3 =division_1.division(num_1, num_2)
print('Division:', resultado_3)
print("_____________________________________")


resultado_4 = modulo_3.modulo(num_1, num_2)
print('Modulo (residuo):', resultado_4)
print("_____________________________________")


resultado_5 = modulo_4.multiplicacion(num_1, num_2)
print('Multiplicación:', resultado_5)
print("_____________________________________")
