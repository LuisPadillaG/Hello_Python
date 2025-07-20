###
# 01 - Sentencias condicionales (if, elif, else)
# Permiten ejecutar bloques de código solo si se cumplen ciertas condiciones
###

import os 
os.system("clear")


print("\n Sentencia simple condicional")

edad = 30
if edad >= 18:
    print("eres mayor de edad")
print("Este print se ejecuta no importa tu edad fijate")

edad = 15
if edad >= 18:
    print("eres mayor de edad")
else:
    print("Eres menor de edad")

nota = 7

print("\n Setencia condicional con elif")
if nota >= 9:
    print("Sobresaliente!")
elif nota >= 7:
    print("Notable!")
elif nota >=6:
    print("Aprobado")
else:
    print("Pues habra que mejorar, reprobado lo lamento.")

print(" \n Condiciones multiples")
edad = 25
tiene_carnet = True

# de JavaScript a Python
# && -> and
# || -> or
# ! -> not
if edad >= 18 and tiene_carnet:
    print("Puedes conducir")
else:
    print("POLICIAAAAAA WIU WIU WIU")

# un pueblo de Isla margarita
# aqui la diferencia es que con una condicion se cumpla ya se puede conducir
if edad >= 18 or tiene_carnet:
    print("Puedes conducir en Isla margarita")
else:
    print("Paga al policia y te deja conducir")

print("Chequemos si es fin de semana")
es_fin_de_semana = False
if not es_fin_de_semana:
    print("Venga, que hay que trabajar!")

print("\n Anidar condicionales")

edad = 20
tiene_dinero = True
if edad >= 18:
    if tiene_dinero:
        print("Puedes ir a la discoteca")
    else:
        print("Quedate en casa, te falta dinero")
else:
    print("No puedes entrar a la disco")

