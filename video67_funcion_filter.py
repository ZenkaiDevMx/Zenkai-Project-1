# PILDORAS INFORMATICAS
# PYTHON
# VIDEO 67
# FUNCION FILTER

#.Verifica que los elementos de una secuencia cumplen una condición, 
# devolviendo un iterador con los elementos que cumplen dicha condición.


#EJEMPLO 1

'''def numero_par(num):

    if num % 2==0:

         return True'''

# numeros = [17, 24, 7, 39, 8, 51, 92]


# pares = list(filter(lambda num: num % 2 == 0, numeros))


# print(f"Lista original: {numeros}")
# print(f"Carnita filtrada (Pares): {pares}")

#En este ejercicio implementamos la función de orden superior filter(), una herramienta fundamental para la 
#Soberanía de Datos. Esta instrucción actúa como un tamiz que recorre una lista y evalúa cada elemento bajo 
#una condición booleana (True o False). Al integrarla con una función Lambda, eliminamos la necesidad de 
#declarar funciones externas con def, logrando una extracción de "datos" quirúrgica en una sola línea de 
#código. El sistema evalúa el residuo de la división entre dos (num % 2 == 0) para identificar números 
#pares; aquellos que cumplen la condición son "atrapados" por el filtro y devueltos en una nueva lista. Esta 
#metodología es el estándar para limpiar grandes volúmenes de información en el disco duro de forma #eficiente y rápida.



   
#EJEMPLO 2

# class Empleado:
#     def __init__(self, nombre, cargo, salario):
#          self.nombre = nombre
#          self.cargo = cargo
#          self.salario = salario
      
#     def __str__(self):
        
#         return f"{self.nombre} que trabaja como {self.cargo} tiene un salario de {self.salario} $"

# listaEmpleados = [
#     Empleado("Juan", "Director", 75000), 
#     Empleado("Ana", "Presidenta", 85000),
#     Empleado("Antonio", "Administrativo", 25000),
#     Empleado("Sara", "Secretaria", 27000),
#     Empleado("Mario", "Botones", 21000),
# ]

# # El filtro extrae objetos completos de la clase Empleado
# salarios_altos = filter(lambda empleado: empleado.salario > 50000, listaEmpleados)

# print("--- Reporte de Salarios de Élite ---")
# for empleado_salario in salarios_altos:
#     print(empleado_salario)

#En este ejercicio elevamos la potencia de filter() al aplicarlo sobre una lista de objetos. A diferencia 
#del filtrado de datos simples, aquí el sistema interactúa con los atributos internos de la clase Empleado. 
#La función Lambda actúa como un escáner que accede a la propiedad self.salario de cada instancia; si el 
#valor supera el umbral de los 50,000, el objeto completo es retenido por el filtro. Es fundamental notar 
#que filter() no solo devuelve el dato numérico, sino la instancia completa del objeto, permitiendo que al 
#iterar con el bucle for se ejecute automáticamente el método especial __str__. Esta metodología es clave 
#para realizar auditorías de "datos" compleja y reportes jerárquicos dentro de tu nuestro búnker de datos.


