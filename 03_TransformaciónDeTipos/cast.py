###
#03 - casting de tipos
# transformar de un tipo de un valor a otro
# int, float, complex, str, boool, noneType, list, tuple, dict, range, set...
###

print("conversion de tipos")
print(type("100")) #esto es la cadena
print(type(int("100"))) # esto es la transformacion a int

#print("100"+2) #can only concatenate str (not int) to str. o sea error
#print("100"+str(2)) 
#print(int(3.9416))
print(round(2.49))
print(round(2.5))
print(round(3.5))
print(round(3.51))


print(bool(3))
print(bool(0))
print(bool(-1))
print(bool("")) #no tiene contenido = False
print(bool(" ")) #ya tiene contenido por ese espacio
print(bool("False")) #tiene contenido