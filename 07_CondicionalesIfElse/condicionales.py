###
# 01 - Sentencias condicionales (if, elif, else)
# Permiten ejecutar bloques de código solo si se cumplen ciertas condiciones
###

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