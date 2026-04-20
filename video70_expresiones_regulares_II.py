# PILDORAS INFORMATICAS
# PYTHON
# VIDEO 70
# EXPRESIONES REGULARES 2



#EJEMPLO 1

# import re

# lista_nombres=['Ana Gómez',
#                 'María Martín',
#                 'Sandra López',
#                 'Santiago Martín',
#                 'Sandra Fernández',]

# for elemento in lista_nombres:
#     if re.findall('^Sandra', elemento):

#        print(elemento)

#Aquí implementamos el metacarácter acento circunflejo (^), una herramienta de Anclaje 
#Inicial dentro del módulo re. Al colocar el símbolo ^ antes del patrón ("^Sandra"), le 
#ordenamos al radar que solo valide los datos si esta aparece estrictamente al comienzo 
#de la cadena de texto. El sistema recorre la lista y el condicional if re.findall(...) 
#actúa como un filtro de seguridad; si el nombre no empieza con el patrón indicado, es 
#ignorado. Esta técnica es fundamental para la Soberanía de Datos, ya que permite 
#realizar búsquedas jerárquicas y organizar grandes volúmenes de información 
#(como directorios o bases de datos de clientes) basándose en su raíz inicial, 
#optimizando el #tiempo de respuesta del sistema.


#EJEMPLO 2


# import re

# lista_nombres=['Ana Gómez',
#                 'María Martín',
#                 'Sandra López',
#                 'Santiago Martín',
#                 'Sandra Fernández',]

# for elemento in lista_nombres:
#     if re.findall('Martín$', elemento):

#        print(elemento)

#Aqui implementamos el metacarácter signo de dólar (), que actúa como un ancla de 
#finalización dentro del modulo re. Al colocar el símbolo inmediatamente después del 
#patrón (Martín$), le indicamos al radar que solo valide los datos si esta aparece 
#estrictamente al final de la cadena de texto. A diferencia del ejemplo anterior, aquí 
#ignoramos lo que haya al principio y nos enfocamos en el cierre del dato. Esta técnica 
#es vital para la Soberanía de Datos, ya que permite filtrar registros por apellidos, 
#sufijos o extensiones de archivos, asegurando que el sistema solo procese la información 
#que cumple con el criterio de terminación establecido


#EJEMPLO 3


# import re

# lista_nombres=['http://pildorasinformaticas.es',
#                 'ftp://pildorasinformaticas.es',
#                'http://pildorasinformaticas.com',
#                'ftp://pildorasinformaticas.com']

# for elemento in lista_nombres:
#     if re.findall('es$', elemento):

#        print(elemento)

#Aqui aplicamos el anclaje final mediante el signo de dólar () para realizar una 
#filtración técnica de dominios de internet. Al definir patrones, el radar ignora el 
#protocolo de inicio (http o ftp) y se enfoca exclusivamente en identificar las 
#direcciones que terminan con la extensión territorial de España (.es). Esta metodología 
#es fundamental para la Soberanía de Datos, ya que permite organizar y segmentar grandes 
#volúmenes de URLs o archivos en el disco duro basándose únicamente en su sufijo, 
#garantizando que el sistema solo procese la carnita que pertenece a una región o tipo de 
#archivo específico.


#EJEMPLO 4


# import re

# lista_nombres=['http://pildorasinformaticas.es',
#                 'ftp://pildorasinformaticas.es',
#                'http://pildorasinformaticas.com',
#                'ftp://pildorasinformaticas.com']

# for elemento in lista_nombres:
#     if re.findall('^ftp', elemento):

#        print(elemento)

#Aqui aplicamos el anclaje inicial mediante el acento circunflejo (^) para realizar una 
#filtración por protocolo de transferencia. Al definir el patrón ^ftp, el radar ignora la 
#extensión final del dominio y se enfoca exclusivamente en identificar las direcciones 
#que comienzan con el protocolo FTP. Esta técnica es esencial para la Soberanía de Datos, 
#ya que permite segregar los datos de la información basándose en su origen o método de 
#conexión, garantizando que el sistema solo procese registros que cumplen con una 
#jerarquía de inicio específica dentro del disco duro.



#EJEMPLO 5


# import re

# lista_nombres=['http://informaticaespaña.es',
#                 'hftp://pildorasinformaticas.es',
#                'http://pildorasinformaticas.com']
               
# for elemento in lista_nombres:
#     if re.findall('[ñ]', elemento):

#        print(elemento)

#Aqui implementamos los corchetes [ ], que definen una Clase de Caracteres en el módulo 
#re. Al colocar un carácter dentro de ellos, le ordenamos al radar que localice cualquier 
#coincidencia que contenga ese elemento específico en cualquier posición de la cadena. En 
#este caso, lo usamos para detectar la letra ñ, demostrando la capacidad del sistema para 
#filtrar caracteres especiales o regionales. Esta técnica es la base para crear filtros 
#de búsqueda flexibles donde podemos definir un conjunto de posibilidades dentro de 
#nuestros  datos en el disco duro, permitiendo identificar registros que contienen 
#caracteres que podrían causar problemas en sistemas que no los soportan. 


#EJEMPLO 6


# import re

# lista_nombres=['hombres',
#                 'mujeres',
#                 'mascotas',
#                 'niños',
#                 'niñas']
# for elemento in lista_nombres:
#     if re.findall('niñ[oa]s', elemento):

#        print(elemento)

#Aqui aplicamos la potencia de los corchetes [ ] para realizar búsquedas con variaciones 
#de género o caracteres opcionales en una posición específica. Al definir el patrón 
#niñ[oa]s, el radar entiende que después de la letra ñ puede aparecer tanto una o como 
#una a. El sistema valida los datos si encuentra niños o niñas, pero ignora cualquier 
#otro término que no encaje con ese molde exacto. Esta técnica es fundamental para la 
#Soberanía de Datos, ya que permite normalizar búsquedas en el disco duro, capturando 
#diferentes versiones de una misma palabra sin tener que escribir múltiples líneas de 
#código o funciones separadas.



#EJEMPLO 7


# import re

# lista_nombres=['hombres',
#                 'mujeres',
#                 'mascotas',
#                 'camión',
#                 'camion']
# for elemento in lista_nombres:
#     if re.findall('cami[oó]n', elemento):

#        print(elemento)

#Aqui utilizamos los corchetes [ ] para solucionar el problema de la acentuación en las 
#búsquedas de texto. Al definir el patrón cami[oó]n, le indicamos al radar que acepte 
#tanto la letra o sin tilde como la ó con tilde en esa posición específica de la palabra. 
#Esta técnica es vital para la Soberanía de Datos, ya que permite que el sistema recupere 
#los datos sin importar errores ortográficos o diferencias en la codificación de caracteres. 
#Es un método de normalización que garantiza que ninguna información valiosa quede fuera del 
#análisis por una simple tilde, optimizando el rastreo masivo en el disco duro.



