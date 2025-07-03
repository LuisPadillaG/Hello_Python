#006 - Entrada de usuario (input()) - Version simplificada
# La función input() permite obtener datos de usuario a través de lo que escriba en la consola
#print("Hola, ¿Cómo te llamas?")
#nombre = input()

nombre2 = input("Hola, como te llamas?\n")
print(f"Hola {nombre2}, encantado de conocerte :D")

age = input("Cuantos anos tienes?\n")

print(f"Wow, {age} son muchos anos")

print("Obtener multiples valores a la vez")
country, city = input("En que pais y ciudad vives?\n").split()
print(f"Hola, vives en {country}, {city}")

