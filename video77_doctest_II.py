# PILDORAS INFORMATICAS
# PYTHON
# VIDEO 77
# DOCUMENTACION Y PRUEBAS 2


#EJEMPLO 1


# import math
# import doctest

# def raizCuadrada(listaNumeros):
#      """
#      La función devuelve una lista con la
#      raíz cuadrada de los elementos numéricos
#      pasados por parámetros en otra lista

#      >>> lista=[]
#      >>> for i in [4, 9, 16]:
#      ...    lista.append(i)
#      >>> raizCuadrada(lista)
#      [2.0, 3.0, 4.0]
#      """

#      return [math.sqrt(n) for n in listaNumeros]


# #print (raizCuadrada([9, 16, 25, 36]))

# import doctest
# doctest.testmod()

#Aqui implementamos la Simulación de Bucles dentro de la documentación técnica. El uso de 
#append() es fundamental para la construcción dinámica de los datos que será procesada. 
#Al iterar con el bucle for, inyectamos cada valor en la lista para preparar el escenario 
#de prueba. Por otro lado, la implementación de los tres puntos (... ) actúa como un Label 
#de Continuación, indicando al intérprete que el bloque de código sigue activo. 
#Esta estructura es vital, ya que permite que la documentación técnica replique fielmente 
#el comportamiento de una consola real, garantizando que las pruebas de integración en el 
#disco duro sean precisas y respeten la jerarquía del código.




#EJEMPLO 2


# import math
# import doctest

# def raizCuadrada(listaNumeros):
#      """
#      La función devuelve una lista con la
#      raíz cuadrada de los elementos numéricos
#      pasados por parámetros en otra lista

#      >>> lista=[]
#      >>> for i in [4, 9, 16]:
#      ...    lista.append(i)
#      >>> raizCuadrada(lista)
#      [2.0, 3.0, 4.0]

#      >>> lista=[]
#      >>> for i in [4, -9, 16]:
#      ...    lista.append(i)
#      >>> raizCuadrada(lista)
#      Traceback (most recent call last):
#   File "e:\Descargas\ESTUDIO\PROGRAMACION\video77_doctest_II.py", line 23, in <module>
#     print (raizCuadrada([9, -16, 25, 36]))
#            ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^
#   File "e:\Descargas\ESTUDIO\PROGRAMACION\video77_doctest_II.py", line 20, in raizCuadrada
#     return [math.sqrt(n) for n in listaNumeros]
#             ~~~~~~~~~^^^
# ValueError: expected a nonnegative input, got -16.0
     
#      """

#      return [math.sqrt(n) for n in listaNumeros]


#print (raizCuadrada([9, 16, 25, 36]))

# import doctest
# doctest.testmod()

#Aqui implementamos la validación de errores críticos mediante la simulación de un Traceback 
#dentro del docstring. Al intentar procesar números negativos (como el -9), el motor matemático 
#de Python colapsa y lanza un ValueError. La técnica de Rango SSS aquí consiste en copiar la 
#primera línea del error (Traceback...) y la última línea del error (ValueError...) dentro de la 
#documentación, usando puntos suspensivos para omitir la ruta del archivo. Esta maniobra es 
#vital, ya que permite que el sistema reconozca los errores esperados como "comportamiento 
#correcto", garantizando que el sistema sepa exactamente cómo reaccionar ante los datos 
#corruptos en el disco duro.



#EJEMPLO 3


# import math
# import doctest

# def raizCuadrada(listaNumeros):
#     """
#     La función devuelve una lista con la
#     raíz cuadrada de los elementos numéricos
#     pasados por parámetros en otra lista

#     >>> lista=[]
#     >>> for i in [4, 9, 16]:
#     ...    lista.append(i)
#     >>> raizCuadrada(lista)
#     [2.0, 3.0, 4.0]

#     >>> lista=[]
#     >>> for i in [4, -9, 16]:
#     ...    lista.append(i)
#     >>> raizCuadrada(lista)
#     Traceback (most recent call last):
#         ...
#     ValueError: expected a nonnegative input...
#     """

#     return [math.sqrt(n) for n in listaNumeros]

# if __name__ == "__main__":
    
#     doctest.testmod(optionflags=doctest.ELLIPSIS)

#Aqui implementamos el uso de la bandera ELLIPSIS (Puntos Suspensivos) para simplificar la 
#validación de errores complejos. Al configurar optionflags=doctest.ELLIPSIS, le ordenamos al 
#radar de doctest que ignore partes variables del mensaje de error, como las rutas de archivos 
#en el disco duro o detalles técnicos irrelevantes del sistema, sustituyéndolos por tres puntos 
#(...). Esta técnica es vital, ya que permite crear pruebas de seguridad que funcionen en 
#cualquier sistema (computadora), sin importar que las rutas de las carpetas cambien, 
#enfocándose únicamente en verificar que el tipo de error (ValueError) y la carnita del mensaje 
#sean los correctos.


#EJEMPLO 4


# import math
# import doctest

# def raizCuadrada(listaNumeros):
#     """
#     La función devuelve una lista con la
#     raíz cuadrada de los elementos numéricos
#     pasados por parámetros en otra lista

#     >>> lista=[]
#     >>> for i in [4, 9, 16]:
#     ...    lista.append(i)
#     >>> raizCuadrada(lista)
#     [2.0, 3.0, 4.0]

#     >>> lista=[]
#     >>> for i in [4, 9, 16, 50, 78, -90, 125]:
#     ...    lista.append(i)
#     >>> raizCuadrada(lista)
#     Traceback (most recent call last):
#         ...
#     ValueError: expected a nonnegative input...
#     """

#     return [math.sqrt(n) for n in listaNumeros]

# if __name__ == "__main__":
    
#     doctest.testmod(optionflags=doctest.ELLIPSIS)

#Aqui realizamos una Prueba de Inyección Masiva para validar la robustez del motor de 
#excepciones. Al alimentar la lista con una secuencia mixta de números positivos y negativos, 
#el radar de doctest confirma que el sistema detecta el error en el momento exacto en que los 
#datos presenta un valor prohibido (-90). Gracias al uso de la bandera ELLIPSIS, el sistema se 
#mantiene  al validar la falla técnica sin distraerse con la longitud de la lista o los detalles 
#internos del Traceback. Es la demostración final de cómo una función puede procesar grandes 
#volúmenes de información en el disco duro y aun así mantener un protocolo de seguridad estricto 
#y documentado.

