# PILDORAS INFORMATICAS
# PYTHON
# VIDEO 73
# DECORADORES 1

#EJEMPLO 1

# def funcion_decoradora(funcion_parametro):
#     def funcion_interior():
#         # Acciones adicionales que decoran
#         print("Vamos a realizar un cálculo: ")
#         funcion_parametro()
#         # Acciones adicionales que decoran
#         print("Hemos terminado el cálculo")
#     return funcion_interior

# @funcion_decoradora
# def suma():
#     print(15+20)

# @funcion_decoradora
# def resta():
#     print(30-10)

# suma()
# resta()

#Aqui implementamos la estructura básica de un Decorador, una función de orden superior 
#que recibe una función y devuelve una versión potenciada de la misma. El objetivo es 
#inyectar código adicional (comportamiento) antes y después de la ejecución de los datos 
#principales (en este caso, la suma o la resta). Mediante el uso del símbolo @ (azúcar sintáctica), 
#le ordenamos al sistema que envuelva nuestras funciones con la funcion_interior del decorador. 
#Esta técnica es vital, ya que permite estandarizar procesos como auditorías, logs o validaciones 
#de seguridad en el disco duro sin necesidad de repetir código dentro de cada función individual.
