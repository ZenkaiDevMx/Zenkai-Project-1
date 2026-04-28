# PILDORAS INFORMATICAS
# PYTHON
# VIDEO 76
# DOCUMENTACION Y PRUEBAS


#EJEMPLO 1

# def areaTriangulo(base,altura):

#     """
#     Calcula el área de un triángulo dado

#     >>> areaTriangulo(3,6)
#     9.0

#     """

#     return (base*altura)/2

# import doctest
# doctest.testmod()

#Aqui implementamos el módulo doctest, una herramienta de Pruebas Automatizadas integrada 
#directamente en la documentación. Al utilizar la sintaxis de triple flecha (>>>), simulamos 
#una ejecución en la consola de Python dentro del docstring, indicando el resultado esperado 
#justo debajo. Cuando el sistema ejecuta doctest.testmod(), el radar escanea estas pruebas y 
#verifica si el motor de cálculo devuelve exactamente lo que prometimos. Esta técnica es 
#vital, ya que garantiza que cualquier cambio futuro en el código no rompa las funciones 
#críticas en el disco duro, convirtiendo nuestra sabiduría técnica en una armadura de 
#seguridad activa.



#EJEMPLO 2

# def areaTriangulo(base,altura):

#     """
#     Calcula el área de un triángulo dado

#     >>> areaTriangulo(3,6)
#     8.0

#     """

#     return (base*altura)/2

# import doctest
# doctest.testmod()

#Aqui realizamos una Prueba de Fallo Controlado para verificar la capacidad de respuesta del 
#módulo doctest. Al declarar intencionalmente un resultado incorrecto en la documentación 
#(indicando 8.0 cuando el motor devuelve 9.0), el sistema activa sus protocolos de alerta. 
#A diferencia del silencio de una prueba exitosa, aquí el sistema despliega un reporte 
#detallado que muestra el valor esperado frente al valor real obtenido. Esta técnica es 
#fundamental, ya que actúa como un sistema de detección de intrusos o errores de lógica, 
#asegurando que ningún dato corrupto o cálculo erróneo pase desapercibido en el disco duro.


#EJEMPLO 3

# def areaTriangulo(base,altura):

#     """
#     Calcula el área de un triángulo dado

#     >>> areaTriangulo(3,6)
#     9.0

#     """

#     return "El area del triangulo es: " +str((base*altura)/2)

# import doctest
# doctest.testmod()

#Aqui implementamos una Validación de Formato Estricto. El radar de doctest no solo evalúa 
#el valor numérico, sino la estructura completa de la respuesta. Al modificar el motor para 
#que devuelva un string ("El area del triangulo es: 9.0") en lugar del flotante puro (9.0) 
#que indicamos en la documentación, el sistema marca un error de coincidencia. Esta técnica 
#es vital, ya que garantiza que las funciones no solo entreguen resultados correctos, sino 
#que los entreguen en el tipo de dato exacto (string, int, float) que el resto del sistema 
#espera recibir en el disco duro.



#EJEMPLO 4

# def areaTriangulo(base,altura):

#     """
#     Calcula el área de un triángulo dado

#     >>> areaTriangulo(3,6)
#     'El área del triángulo es: 9.0'

#     """

#     return "El área del triángulo es: " +str((base*altura)/2)

# import doctest
# doctest.testmod()

#Aqui implementamos la Validación Literal de Strings. Al corregir la prueba para que incluya 
#las comillas y el texto exacto que devuelve la función, el radar de doctest vuelve a entrar 
#en estado de silencio positivo (éxito). Esta maniobra demuestra la precisión milimétrica 
#necesaria en la Soberanía de Datos: el sistema no solo verifica el cálculo matemático, 
#sino la integridad absoluta de la cadena de caracteres, incluyendo espacios y tildes. 
#Es la técnica definitiva para asegurar que los reportes generados en el disco duro mantengan 
#siempre el mismo formato profesional sin desviaciones imprevistas.




#EJEMPLO 5

# def areaTriangulo(base,altura):

#     """
#     Calcula el área de un triángulo dado

#     >>> areaTriangulo(3,6)
#     'El área del triángulo es: 9.0'

#     >>> areaTriangulo(4,5)
#     'El área del triángulo es: 10.0'

#     >>> areaTriangulo(9,3)
#     'El área del triángulo es: 13.5'



#     """

#     return "El área del triángulo es: " +str((base*altura)/2)

# import doctest
# doctest.testmod()

#Aqui implementamos una Auditoría de Casos Múltiples dentro del mismo docstring. Al definir 
#varias llamadas a la función con diferentes parámetros, el radar de doctest ejecuta una 
#ráfaga de verificaciones consecutivas. Esta técnica es fundamental, ya que permite poner a 
#prueba el motor de cálculo frente a distintos escenarios (números pares, impares o 
#resultados con decimales) en un solo despliegue. Si tan solo uno de estos casos falla, 
#el sistema reportará la falla específica, garantizando que los datos sean procesados 
#correctamente bajo cualquier circunstancia dentro del disco duro.



#EJEMPLO 6

# def areaTriangulo(base,altura):

#     """
#     Calcula el área de un triángulo dado

#     >>> areaTriangulo(3,6)
#     'El área del triángulo es: 9.0'

#     >>> areaTriangulo(4,5)
#     'El área del triángulo es: 11.0'

#     >>> areaTriangulo(9,3)
#     'El área del triángulo es: 13.5'



#     """

#     return "El área del triángulo es: " +str((base*altura)/2)

# import doctest
# doctest.testmod()

#Aqui realizamos una Prueba de Resistencia de Casos donde forzamos un error específico en la 
##segunda validación (esperando 11.0 cuando el motor devuelve 10.0). Al ejecutar esta 
#maniobra, el radar de doctest detiene su silencio y despliega un informe de daños 
#detallado. Esta técnica es vital, ya que nos enseña que un solo caso erróneo entre cien es 
#suficiente para comprometer la fiabilidad de todo el motor de cálculo. El sistema nos 
#indica exactamente en qué valor falló los datos, permitiendo corregir la documentación o el 
#código antes de que el error se propague por el disco duro.



#EJEMPLO 7= Donde elevamos el nivel de las pruebas a una Lógica de Validación Completa.

# def compruebaMail(mailUsuario):

#     """
#     la función compruebaMail evalúa un mail
#     recibido en busca de la @. Si tiene una @
#     es correcto, si tiene mas de una @ es incorrecto
#     si la @ esta la final es incorrecto

#     >>> compruebaMail('juan@cursos.es')
#     True

#     >>> compruebaMail('juancursos.es@')
#     False

#     >>> compruebaMail('juancursos.es')
#     False
    
#     >>> compruebaMail('juan@cursos@.es')
#     False

#     """
#     arroba=mailUsuario.count('@')

#     if(arroba!=1 or mailUsuario.rfind('@')==(len(mailUsuario)-1) or mailUsuario.find('@')==0):
#          return False

#     else:
#          return True

# import doctest
# doctest.testmod()

#Aqui implementamos una Batería de Pruebas de Validación Lógica. A diferencia de los 
#cálculos matemáticos anteriores, aquí el radar de doctest supervisa un algoritmo de 
#seguridad que utiliza métodos de strings (count, find, rfind) para verificar la integridad 
#de un correo electrónico. Definimos cuatro escenarios críticos: un caso de éxito y tres de 
#fallo (sin arroba, arroba al final o múltiples arrobas). Esta técnica es vital, ya que 
#permite blindar los puntos de entrada de información al búnker, garantizando que solo los 
#datos que cumplan con las reglas del protocolo sea procesada en el disco duro.



#EJEMPLO 8

# def compruebaMail(mailUsuario):

#     """
#     la función compruebaMail evalúa un mail
#     recibido en busca de la @. Si tiene una @
#     es correcto, si tiene mas de una @ es incorrecto
#     si la @ esta la final es incorrecto

#     >>> compruebaMail('juan@cursos.es')
#     True

#     >>> compruebaMail('juancursos.es@')
#     False

#     >>> compruebaMail('juancursos.es')
#     False
    
#     >>> compruebaMail('juan@cursos@.es')
#     False

#     """
#     arroba=mailUsuario.count('@')

#     if(arroba!=0 or mailUsuario.rfind('@')==(len(mailUsuario)-1) or mailUsuario.find('@')==0):
#          return False

#     else:
#          return True

# import doctest
# doctest.testmod()

#Aqui realizamos una Auditoría de Regresión para detectar errores introducidos durante la 
#modificación del código. Al cambiar la condición lógica de arroba!=1 a arroba!=0, el motor 
#ahora marca como False incluso a los correos que tienen una sola arroba (como 'juan@cursos.es'), 
#rompiendo la funcionalidad principal. El radar de doctest lanza inmediatamente una alerta roja 
#porque el resultado obtenido (False) no coincide con el éxito esperado (True) definido en la documentación. 
#Esta técnica es vital, ya que actúa como una red de seguridad que impide que un error de dedo o una mala 
#decisión lógica destruya la integridad del sistema en el disco duro.


