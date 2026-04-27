# PILDORAS INFORMATICAS
# PYTHON
# VIDEO 75
# DOCUMENTACION


#EJEMPLO 1

# def areaCuadrado (lado):

#     """Calcula el área de un cuadrado elevando al cuadrado el lado pasado por parámetro"""

#     return "El área del cuadrado es: "+ str(lado*lado)

# def areaTriangulo(base, altura):

#     return "El área del triangulo es: " + str((base*altura)/2)

# print(areaTriangulo(2,7))

#Aqui implementamos los Docstrings a nivel de función. Al colocar una cadena de texto 
#entre triples comillas ("""...""") inmediatamente después de la definición de la función, 
#estamos inyectando sabiduría técnica directamente en el objeto. Esta técnica es fundamental, 
# ya que permite que cualquier Guerrero o herramienta de análisis entienda el propósito de la 
#función sin tener que descifrar la lógica matemática. Es el primer paso para crear un sistema 
#de código profesional donde los datos viajan junto con el motor de ejecución, garantizando que 
#el sistema sea autoexplicativo y fácil de mantener en el disco duro.



#EJEMPLO 2

# def areaCuadrado (lado):

#     """Calcula el área de un cuadrado elevando al cuadrado el lado pasado por parámetro"""

#     return "El área del cuadrado es: "+ str(lado*lado)

# def areaTriangulo(base, altura):

#     return "El área del triangulo es: " + str((base*altura)/2)

# print(areaCuadrado.__doc__)

#Aqui implementamos la extracción de documentación mediante el atributo especial doc. 
#A diferencia de la función help(), que genera un reporte completo de sistema, el uso 
#de __doc__ permite al Guerrero acceder exclusivamente a la carnita informativa definida 
#entre las triples comillas. Esta técnica es vital, ya que permite imprimir o manipular 
#la sabiduría técnica de una función de forma limpia en la consola, evitando visores 
#externos o pausas innecesarias. Es el método más eficiente para realizar auditorías 
#rápidas de código y verificar que cada motor de cálculo en el disco duro esté 
#correctamente explicado.



#EJEMPLO 3

# def areaCuadrado (lado):

#     """Calcula el área de un cuadrado elevando al cuadrado el lado pasado por parámetro"""

#     return "El área del cuadrado es: "+ str(lado*lado)

# def areaTriangulo(base, altura):

#     """Calcula el área de un triangulo utilizando los parámetros base y altura"""

#     return "El área del triangulo es: " + str((base*altura)/2)

# help(areaTriangulo)

#Aqui implementamos la función help() aplicada a un objeto específico del sistema. 
#A diferencia de ejecutarla sobre un módulo completo, al pasarle una función individual 
#(areaTriangulo), el radar se enfoca exclusivamente en extraer los datos técnicos de ese 
#motor de cálculo: muestra su firma (parámetros que recibe) y su docstring asociado. 
#Esta técnica es vital, ya que permite que cualquier Guerrero consulte la ficha técnica 
#de una herramienta sin necesidad de navegar por todo el manual del sistema, optimizando 
#el tiempo de respuesta y garantizando la correcta implementación de las funciones en el 
#disco duro.


#EJEMPLO 4

# class Areas:

#    """Esta clase calcula las áreas de diferentes figuras geométricas"""

#    def areaCuadrado (lado):

#         """Calcula el área de un cuadrado elevando      al cuadrado el lado pasado por parámetro"""

#         return "El área del cuadrado es: "+ str(lado*lado)

#    def areaTriangulo(base, altura):

#     """Calcula el área de un triangulo utilizando los parámetros base y altura"""

#     return "El área del triangulo es: " + str((base*altura)/2)

# help(Areas)

#Aquí implementamos la Documentación Jerárquica dentro de una Clase. Al colocar un 
#docstring al inicio de la clase y otros dentro de cada método, estamos creando un 
#manual técnico estructurado. Cuando invocamos help(Areas), el radar de Python 
#organiza la información en niveles: primero muestra la descripción general de 
#la clase y luego desglosa los datos técnicos de cada método disponible. 
#Esta técnica es fundamental, ya que permite que el sistema sea auto-documentado, 
#facilitando que cualquier Guerrero entienda no solo qué hace una herramienta, 
#sino cómo se agrupan las funciones dentro del disco duro.


#EJEMPLO 5

# import pydoc 
# from MODULOS.calculos.basicos import operaciones_basicas

# class Areas:
#    """Esta clase calcula las áreas de diferentes figuras geométricas"""

#    def areaCuadrado(lado):
#         """Calcula el área de un cuadrado elevando al cuadrado el lado pasado por parámetro"""
#         return f"El área del cuadrado es: {lado*lado}"

#    def areaTriangulo(base, altura):
#         """Calcula el área de un triangulo utilizando los parámetros base y altura"""
#         return f"El área del triangulo es: {(base*altura)/2}"

# pydoc.pager = pydoc.plainpager 
# pydoc.help(operaciones_basicas)

#Aqui implementamos la soberanía de salida utilizando el módulo pydoc. El objetivo es 
##extraer la documentación de un módulo externo (operaciones_basicas) sin que la terminal 
##de Windows o VS Code interrumpan el flujo con el visor interactivo ("-- Más --"). Al 
#configurar pydoc.pager = pydoc.plainpager, le ordenamos al sistema que trate la ayuda 
#como texto plano y la imprima de corrido en la consola. Esta técnica es vital para la 
#Ingeniería de Datos, ya que permite al Guerrero visualizar manuales técnicos completos 
#en el disco duro de forma inmediata, manteniendo el formato profesional de Python pero 
#eliminando las trabas de navegación de la terminal moderna.

