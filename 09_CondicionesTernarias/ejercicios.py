###
# Ejercicios
###

# Ejercicio 1: Determinar el mayor de dos numeros
# Pide al usuario que introduzca dos numeros y muestra un mensaje
# indicando cual es o si son iguales
    #Opcion 1:
print("Introduzca el 1er numero")
numero1 = input()
numero2 =  input("Introduce el 2do numero\n")
    #Opcion corta:
#numero1, numero2 = input("Introduce los dos numeros que deseas sumar\n").split()
if numero1 > numero2: 
    print(f"El numero {numero1} es mayor al numero {numero2}")
elif numero1 < numero2:
    print(f"El numero {numero2} es mayor al numero {numero1}")
else:
    print("Los numeros son iguales")

# Ejercicio 2: Calculadora simple
# Pide al usuario dos numeros y una operacion (+,-,*,/)
# Realiza la operacion y muestra el resultado (maneja la division entre cero)
print("\n\n------------O P E R A C I O N E S--------------")
operador = input("Escribe el caracter de la operacion (*, /, +, -)")
numero1, numero2 = input("Introduce los dos numeros que deseas hacer su operacion\n").split()
resultado = 0
if operador == "+":
    resultado = float(numero1) + float(numero2)
    print(f"Tu resultado es {resultado}")
elif operador == "-" or operador == "resta":
    resultado = float(numero1) - float(numero2)
    print(f"Tu resultado es {resultado}")
elif operador == "*" or operador == "multiplicar":
    resultado = float(numero1) * float(numero2)
    print(f"Tu resultado es {resultado}")
elif operador == "/" or operador == "dividir":
    resultado = float(numero1) - float(numero2)
    print(f"Tu resultado es {resultado}")
else:
    print("No señalaste correctamente el signo")

# Ejercicio 4: Edades
# Pide al usuario que intruduzca una edad y la clasifique en:
# - Bebe (0 - 2 años)
# - Niño (3 - 12 años)
# - Adolescente (13 - 17 años)
# - Adulto (18 - 64 años)
# - Adulto mayor (65 años o más)

print("\n\n------------E D A D E S--------------")
edad = input("Mete tu edad y ya hermano \n")
edad = int(edad)
if edad >= 0 and edad <= 2:
    print("eres un bebe, impresionante que sepas teclear")
elif edad >= 3 and edad <= 12:
    print("niño")
elif edad >= 13 and edad <= 17:
    print("eres adolescente")
elif edad >= 18 and edad <= 64:
    print("Ya estás grande. Todo un adulto.")
elif edad >= 65:
    print("Estas anciano o sea, un adulto mayor")


