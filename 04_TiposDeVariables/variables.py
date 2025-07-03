###
#04 - Variables
# Las variables sirven para guardar datos en memoria.
# Python es un lenguaje de tipado dinámico y de tipado fuerte.
###

#Asignar una varibale
# solo hace falta poner esto

age = 20
print(age)

age = 29
print(age)
#Tipado dinámico: el tipo de dato que se asigna a una variable 
# depende del tipo de dato que se asigne a la variable. //Se determina en tiempo de ejecución
my_name = "luisito"
print(type(my_name))
my_name = 20
print(type(my_name))

my_name_real = "Luis"
#Tipado fuerte: Python no realiza conversiones automáticas
#print(10 + "2") #no funciona obvio
#Si quieres evaluar un numero de un texto puedes
print(f"Hola soy {my_name_real}, tengo {my_name + 1} anios")


n, age, city = "Alberto", 23, "Caracas" # No recomendada forma de asignar variables

# Convenciones de nombres de variable
mi_nombre_de_variable = "ok"
 
MI_CONSTANTE = 31.4 #Las UPPER_CASE se pensaron para constantes, realmente no existen constantes en python, pero allí te informo
print(MI_CONSTANTE)

### ---------------------------------------------------------------------
### ---------------------------------------------------------------------
### ---------------------------------------------------------------------
##05 AGREGAR TIPADO DE VARIABLES
### ---------------------------------------------------------------------

is_user_logged_in: bool = True
print(is_user_logged_in)

is_user_logged_in = 2424
print(is_user_logged_in)