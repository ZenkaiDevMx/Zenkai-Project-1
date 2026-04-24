# PILDORAS INFORMATICAS
# PYTHON
# VIDEO 74a-74b
# DECORADORES 2


#EJEMPLO 1

# def funcion_decoradora(funcion_parametro):

#     def funcion_interior(*args,):

#         # Acciones adicionales que decoran

#         print("Vamos a realizar un cálculo: ")

#         funcion_parametro(*args,)

#         # Acciones adicionales que decoran

#         print("Hemos terminado el cálculo")

#     return funcion_interior

# @funcion_decoradora
# def suma(num1, num2, num3):
#     print(num1+num2+num3)

# @funcion_decoradora
# def resta(num1, num2,):
#     print(num1-num2)

# suma(7,5,8)
# resta(12,10)

#Aqui implementamos el uso de argumentos variables mediante la sintaxis *args dentro de la funcion_interior 
#del decorador. Esta técnica permite que el envoltorio sea flexible, capturando cualquier número de parámetros 
#posicionales y pasándolos directamente a la función original. Al usar args, el búnker ya no colapsa si una 
#función recibe dos datos (como la resta) o tres (como la suma); el decorador se adapta dinámicamente al volumen 
#de los datos procesados. Esta metodología es vital, ya que permite crear decoradores universales que pueden blindar 
#o auditar múltiples funciones con diferentes estructuras en el disco duro.




#EJEMPLO 2

# def funcion_decoradora(funcion_parametro):

#     def funcion_interior(*args):

#         # Acciones adicionales que decoran

#         print("Vamos a realizar un cálculo: ")

#         funcion_parametro(*args)

#         # Acciones adicionales que decoran

#         print("Hemos terminado el cálculo")

#     return funcion_interior

# @funcion_decoradora
# def suma(num1, num2, num3):
#     print(num1+num2+num3)

# @funcion_decoradora
# def resta(num1, num2):
#     print(num1-num2)

# def potencia(base, exponente):

#     print(pow(base, exponente))

# suma(7,5,8)
# resta(12,10)
# potencia(5,3)

#Aqui realizamos un contraste de ejecución entre funciones con y sin decoración. Mientras que suma() y 
#resta() operan bajo el blindaje del decorador (mostrando los mensajes de inicio y fin del cálculo), 
#la función potencia() se ejecuta de forma directa y "desnuda". Esta maniobra demuestra que en la 
#arquitectura de software: el programador decide qué sectores del búnker requieren procesos adicionales 
#de auditoría o registro mediante el uso de la @funcion_decoradora, y qué sectores operan con lógica pura. 
#Es la base para implementar sistemas de seguridad selectiva donde solo los procesos críticos en el disco duro 
#activan las capas de código extra.



#EJEMPLO 3

# def funcion_decoradora(funcion_parametro):

#     def funcion_interior(*args, **kwargs):

#         # Acciones adicionales que decoran

#         print("Vamos a realizar un cálculo: ")

#         funcion_parametro(*args, **kwargs)

#         # Acciones adicionales que decoran

#         print("Hemos terminado el cálculo")

#     return funcion_interior

# @funcion_decoradora
# def suma(num1, num2, num3):
#     print(num1+num2+num3)

# @funcion_decoradora
# def resta(num1, num2):
#     print(num1-num2)

# @funcion_decoradora
# def potencia(base, exponente):

#     print(pow(base, exponente))

# suma(7,5,8)
# resta(12,10)
# potencia(base=5,exponente=3)

#Aqui implementamos la arquitectura definitiva para decoradores mediante el uso combinado de 
#*args y **kwargs. Mientras que *args captura valores posicionados, **kwargs (keyword arguments) 
#permite al sistema recibir parámetros nombrados en formato de diccionario (como base=5). 
#Esta maniobra dota al sistema de una versatilidad absoluta: el decorador ahora es capaz de envolver 
#cualquier tipo de función, sin importar cómo se le entregue los datos. Es la técnica estándar para 
#crear sistemas de monitoreo, seguridad o caché que sean totalmente transparentes para el resto de 
#las aplicaciónes en el disco duro.


