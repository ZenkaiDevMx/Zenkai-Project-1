# PILDORAS INFORMATICAS
# PYTHON
# VIDEO 66
# FUNCIONES LAMBDAS

#EJEMPLO 1


# def area_triangulo(base, altura):

#     return (base*altura)/2

# triangulo1=area_triangulo(5,7)

# triangulo2=area_triangulo(9,6)

# print(triangulo1)

# print(triangulo2)


# area_triangulo=lambda base, altura:(base*altura)/2

# triangulo1=area_triangulo(5,7)

# triangulo2=area_triangulo(9,6)

# print(triangulo1)

# print(triangulo2)


#En este ejercicio implementamos las Funciones Lambda, también conocidas como funciones anónimas o "al vuelo" (on the go). 
#La ingeniería detrás de una lambda nos permite sintetizar la estructura tradicional de una función (def, return) en una 
#sola línea de código altamente eficiente. Al declarar area_triangulo = lambda base, altura: (base*altura)/2, estamos 
#creando un objeto ejecutable que recibe parámetros y devuelve un resultado de forma directa, eliminando la carga sintáctica 
#innecesaria para cálculos simples. Esta técnica es vital para la Soberanía de Código, ya que permite escribir scripts más 
#limpios y legibles cuando la lógica no requiere procesos complejos como bucles o condicionales anidados, optimizando el 
#rendimiento  al procesar datos rápidos bajo demanda.



#EJEMPLO 2

#al_cubo=lambda numero:pow(numero, 3)

#al_cubo=lambda numero:numero**3

#print(al_cubo(13))

#En este ejercicio simplificamos la operación de potenciación mediante la sintaxis anónima de Lambda. Al utilizar el 
#operador de doble asterisco (**) o la función interna pow(), logramos elevar cualquier número al cubo en una sola 
#línea de ejecución. Esta técnica demuestra la versatilidad de las funciones on-demand: en lugar de reservar espacio en 
#memoria para una función tradicional con def, creamos un recurso ligero que procesa la "carnita" matemática de forma 
#inmediata. Es la herramienta ideal para procesos de Ingeniería de Datos donde necesitamos transformar valores 
#rápidamente antes de inyectarlos en nuestra base de datos de SQL o analizarlos en un reporte.




#EJEMPLO 3

# destacar_valor = lambda comision: f"¡{comision}! $"

# comision_Ana = 15585

# print(destacar_valor(comision_Ana))

#En este ejercicio aplicamos una Lambda para el formateo de strings, demostrando que estas funciones anónimas no solo 
#sirven para cálculos matemáticos, sino también para la manipulación rápida de texto. Al integrar la potencia de las 
#f-strings dentro de la lambda. Esta estructura es ideal para crear "etiquetadores" rápidos que preparan la información 
#antes de ser mostrada en una interfaz o reporte, permitiendo que la "carnita" de los datos sea presentada con un 
#formato profesional (como el símbolo de moneda o signos de exclamación) en una sola línea de ejecución on-the-go.

