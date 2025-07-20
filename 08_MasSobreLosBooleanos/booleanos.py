## Mas sobre boooleanos
# Valores lógicos: True y False. Fundamental para el flujo de control y lógica en programación

import os
os.system("clear")

print("\nOperadores de comparacion")
print("5 > 3: ", 5 > 3)         # True
print("5 < 3: ", 5 < 3)         # False
print("5 == 5: ", 5 == 5)       # True (igualdad)
print("5 != 3: ", 5 != 3)       # True (desigualdad)
print("5 >= 5: ", 5 >= 5)       # True (mayor o igual a)
print("5 >= 5: ", 5 <= 3)       # True (menor o igual a)

print("\nComparacion de cadenas: ")
print("manzana < pera:", "manzana" < "pera") # True 

# Tablas de verdad (para referencia)
print("\nTablas de verdad:")
print("and:")
print("A        B       A and B")
print("True     True    ", True and True)
print("True     False   ", True and False)
print("False    True    ", False and True)
print("True     False   ", True and False)
print("False    False   ", False and False)

print("\nor:")
print("A        B       A and B")
print("True     True    ", True or True)
print("True     False   ", True or False)
print("False    True    ", False or True)
print("True     False   ", True or False)
print("False    False   ", False or False)

print("\nor:")
print("A        B       A and B")
print("True     True    ", True or True)
print("True     False   ", True or False)
print("False    True    ", False or True)
print("True     False   ", True or False)
print("False    False   ", False or False)

print("\nnot:")
print("A        not A")
print("True     ", not True)
print("False    ",  not False)

numero = 5
if numero: # False
    print("El numero no es cero")

nombre = "Juan"
if nombre: # False
    print("No esta vacio")