# PILDORAS INFORMATICAS
# PYTHON
# VIDEO 68
# FUNCION MAP


#.Aplica una función a cada elemento de una lista iterable 
# (listas,tuplas,etc) devolviendo una lista con los resultados.

#EJEMPLO 1

# class Empleado:
#     def __init__(self, nombre, cargo, salario):
#          self.nombre = nombre
#          self.cargo = cargo
#          self.salario = salario
      
#     def __str__(self):
        
#         return f"{self.nombre} (Cargo: {self.cargo}) | Nuevo Salario: {self.salario:.2f} $"

# listaEmpleados = [
#     Empleado("Juan", "Director", 6700), 
#     Empleado("Ana", "Presidenta", 7500),
#     Empleado("Antonio", "Administrativo", 2100),
#     Empleado("Sara", "Secretaria", 2150),
#     Empleado("Mario", "Botones", 1800),
# ]

# # Transformación masiva: Aplicamos el bono del 3%
# # map() aplica la función a CADA elemento de la lista original
# def calculo_comision(empleado):
#     # Usamos un multiplicador directo para la actualización de la "carnita"
#     empleado.salario *= 1.03
#     return empleado

# listaEmpleadosComision = map(calculo_comision, listaEmpleados)

# print("--- Actualización de Nómina con Comisión SSS ---")
# for empleado in listaEmpleadosComision:
#     print(empleado)

#En este ejercicio implementamos la función de orden superior map(), una herramienta diseñada 
#para la Transformación de Datos. A diferencia de filter(), que reduce la lista, map() aplica 
#una lógica específica a cada elemento de la colección, devolviendo una nueva estructura con los 
#datos modificados. En esta operación, el sistema recorre la lista de objetos Empleado e inyecta 
#un incremento del 3% en el atributo salario mediante la función calculo_comision. Es 
#fundamental notar que map() procesa la información de forma iterativa y eficiente, lo que nos 
#permite actualizar miles de registros en el disco duro de un solo golpe, manteniendo la 
#integridad de los objetos originales pero elevando su valor.



#EJEMPLO 2

# class Empleado:
#     def __init__(self, nombre, cargo, salario):
#          self.nombre = nombre
#          self.cargo = cargo
#          self.salario = salario
      
#     def __str__(self):
#         return f"{self.nombre} (Cargo: {self.cargo}) | Salario Final: {self.salario:.2f} $"

# listaEmpleados = [
#     Empleado("Juan", "Director", 6700), 
#     Empleado("Ana", "Presidenta", 7500),
#     Empleado("Antonio", "Administrativo", 2100),
#     Empleado("Sara", "Secretaria", 2150),
#     Empleado("Mario", "Botones", 1800),
# ]

# # Transformación con Criterio de Selección
# def calculo_comision(empleado):
#     # Solo inyectamos el bono a los rangos bajos (<= 3000)
#     if empleado.salario <= 3000:
#         empleado.salario *= 1.03
#     return empleado

# listaEmpleadosComision = map(calculo_comision, listaEmpleados)

# print("--- Nómina con Bono para Rangos de Apoyo SSS ---")
# for empleado in listaEmpleadosComision:
#     print(empleado)

#En este ejercicio implementamos una Transformación Condicional utilizando la función map(). 
# A diferencia del ejemplo anterior, aquí la función calculo_comision actúa como un regulador 
#lógico que evalúa el atributo salario antes de aplicar el incremento. Esta metodología es 
#fundamental en el análisis de datos, ya que permite realizar actualizaciones masivas de forma 
#discriminada: solo los empleados con salarios iguales o inferiores a 3,000 reciben el bono del 
#3%, mientras que los salarios altos permanecen intactos. Al pasar esta lógica a través de 
#map(), el sistema procesa toda la colección de objetos en el disco duro con una eficiencia 
#quirúrgica, garantizando que cada registro sea evaluado y modificado según los parámetros 
#establecidos por el Arquitecto de Datos.




