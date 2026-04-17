# PILDORAS INFORMATICAS
# PYTHON
# VIDEO 69
# EXPRESIONES REGULARES 1

#Iniciamos el despliegue del módulo re (Regular Expressions), la herramienta definitiva 
# para la búsqueda y manipulación de patrones de texto.


#EJEMPLO #1

# import re

# cadena="Vamos a aprender expresiones regulares"

# print(re.search("aprender", cadena))


#Aqui utilizamos el método search(), el cual escanea una cadena de texto buscando una 
#coincidencia específica. A diferencia de un simple "buscar y reemplazar", re.search() 
#devuelve un objeto match que contiene la ubicación exacta (índices de inicio y fin) de 
# los datos dentro de la cadena. Si el patrón existe, el sistema confirma el hallazgo; si no, 
#devuelve None. Este es el primer paso para construir sistemas de filtrado inteligente que 
#permitan procesar y validar información masiva de forma automatizada.
 



#EJEMPLO #2

# import re

# cadena="Vamos a aprender expresiones regulares"

# print(re.search("aprenderrrr", cadena))

#Aqui verificamos el comportamiento de seguridad del método search() ante la ausencia de 
#coincidencias. Al intentar localizar el patrón "aprenderrrr" (el cual no existe en la 
#cadena original), el sistema no lanza un error que colapse el programa, sino que devuelve 
#un valor None. Esta es una característica crítica para la Antifragilidad de nuestro 
#sistema, ya que nos permite implementar condicionales if/else para manejar búsquedas 
#fallidas de forma elegante. En la ingeniería de datos, esta respuesta es fundamental para 
#validar si un registro, un correo o una clave de seguridad cumple con el patrón requerido 
#antes de proceder con el procesamiento de la "carnita".



#EJEMPLO #3

# import re

# cadena="Vamos a aprender expresiones regulares"

# textoBuscar="aprender"

# if re.search(textoBuscar, cadena) is not None:

#     print("He encontrado el texto")

# else:

#     print("No he encontrado el texto")

#Aqui aplicamos un Control de Flujo de Seguridad para interpretar los resultados del módulo re. 
#En lugar de imprimir el objeto en bruto, utilizamos un condicional if/else para validar si el 
#hallazgo es distinto de None. Esta estructura es la base de la Soberanía de Datos en el 
#procesamiento de texto, ya que permite que el búnker tome decisiones automatizadas basadas 
#en la presencia o ausencia de un patrón. Al capturar la coincidencia de esta forma, garantizamos 
#que el sistema sea antifragil, evitando errores de ejecución y permitiendo que el programa reporte 
#el estado de la búsqueda de "carnita" de manera clara y profesional en #la consola.


#EJEMPLO #4

# import re

# cadena="Vamos a aprender expresiones regulares"

# textoBuscar="aprendfsdfdsder"

# if re.search(textoBuscar, cadena) is not None:

#     print("He encontrado el texto")

# else:

#     print("No he encontrado el texto")

#Aquí al intentar localizar el patrón "aprendfsdfdsder" (una cadena deliberadamente errónea), 
#el sistema ejecuta el bloque de seguridad else. Esta estructura demuestra que el sistema no 
#solo es capaz de encontrar "carnita", sino que es inmune a las alucinaciones de búsqueda; 
#si el patrón no es una coincidencia exacta de caracteres, el objeto devuelto es None, 
#disparando la respuesta negativa. Este nivel de control es vital cuando procesamos volúmenes 
#masivos de información en el disco duro, asegurando que solo los datos que cumplen estrictamente 
#con el patrón de rastreo sean procesados, manteniendo así la pureza de nuestra base de datos.


#EJEMPLO #5

# import re

# cadena="Vamos a aprender expresiones regulares"

# textoBuscar="aprender"

# textoEncontrado=re.search(textoBuscar, cadena)

# print(textoEncontrado.start())

# print(textoEncontrado.end())

# print(textoEncontrado.span())

#Aquí implementamos la Metodología de Posicionamiento del módulo re. Una vez que el radar 
#localiza los datos, el objeto match (en este caso textoEncontrado) nos permite extraer 
#las coordenadas exactas de su ubicación mediante tres métodos fundamentales: start(), 
#que nos da el índice del carácter donde comienza el patrón; end(), que nos indica dónde 
#termina; y span(), que devuelve una tupla con ambos valores (inicio, fin). Esta información 
#es vital para la Ingeniería de Datos, ya que permite realizar cortes quirúrgicos en 
#archivos masivos de texto alojados en el disco duro, permitiendo al sistema saber no solo 
#qué encontró, sino exactamente en qué sector del bloque de memoria se encuentra el dato.



#EJEMPLO #6

# import re

# cadena="Vamos a aprender expresiones regulares en Python. Python es un lenguaje de sintaxis sencilla"

# textoBuscar="Python"

# print(re.findall(textoBuscar, cadena))

#Aquí implementamos el método findall(), una herramienta diseñada para el Rastreo Global 
#dentro de grandes volúmenes de texto. A diferencia de search(), que se detiene tras 
#localizar la primera coincidencia, findall() escanea la cadena completa en el disco duro y 
#extrae todas las ocurrencias del patrón "Python", devolviéndolas organizadas en una lista. 
#Esta funcionalidad es vital para la Soberanía de Datos, ya que nos permite cuantificar de 
#forma inmediata cuántas veces aparece un registro o palabra clave en un documento. 
#Es la base para construir sistemas de conteo, auditoría y análisis estadístico de 
#información no estructurada de manera automatizada y eficiente.


#EJEMPLO #7

# import re

# cadena = "Vamos a aprender expresiones regulares en Python. Python es un lenguaje de sintaxis sencilla"
# textoBuscar = "Python"

# print(len(re.findall(textoBuscar, cadena)))

#Aqui implementamos la Cuantificación de Patrones, integrando la función nativa len() con el 
#método re.findall(). Al ejecutar esta maniobra, el sistema no solo localiza los rastros de 
#"Python" en la cadena, sino que devuelve un valor entero que representa el total de 
#coincidencias encontradas. En la ingeniería de datos, esta técnica es fundamental para 
#realizar análisis de frecuencia y auditorías de seguridad en el disco duro; nos permite 
#saber instantáneamente cuántas veces se repite una información sensible o una palabra clave 
#sin tener que recorrer la lista manualmente. Es el cierre perfecto para un sistema de 
#rastreo automatizado que busca medir el volumen de los datos detectada en el sistema.

