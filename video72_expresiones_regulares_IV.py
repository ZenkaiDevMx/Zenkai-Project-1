# PILDORAS INFORMATICAS
# PYTHON
# VIDEO 72
# EXPRESIONES REGULARES 4


#EJEMPLO 1

# import re

# nombre1="Sandra López"

# nombre2="Antonio Gómez"

# nombre3="María López"

# if re.match("Sandra", nombre1):

#     print("Hemos encontrado el nombre")

# else:

#      print("no lo hemos encontrado")

#Aqui implementamos el método match(), cuya función principal es el Rastreo al Inicio de 
#la cadena. A diferencia de otros métodos de búsqueda global, match() evalúa estrictamente 
#si el patrón indicado aparece al comienzo del texto. Si la coincidencia no se encuentra en 
#el primer carácter, el radar devuelve None, incluso si la palabra existe más adelante. 
#Esta técnica es vital, ya que permite realizar validaciones de seguridad inmediatas y 
#filtrar registros que deben cumplir con una estructura jerárquica obligatoria desde 
#su origen en el disco de duro.



#EJEMPLO 2

# import re

# nombre1="Sandra López"

# nombre2="Antonio Gómez"

# nombre3="sandra López"

# if re.match("Sandra", nombre3, re.IGNORECASE):

#     print("Hemos encontrado el nombre")

# else:

#      print("no lo hemos encontrado")

#Aqui implementamos el parámetro re.IGNORECASE, una bandera de configuración que 
#desactiva el Case Sensitive (sensibilidad a mayúsculas y minúsculas) en el radar. 
#Por defecto, las expresiones regulares son estrictas con la grafía de las letras, 
#pero al inyectar esta instrucción, el método match() valida la carnita de forma flexible. 
#El sistema ahora localiza "sandra" aunque el molde sea "Sandra", eliminando errores de 
#coincidencia provocados por la capitalización de los datos. Esta técnica es fundamental, 
#ya que permite normalizar búsquedas en el disco duro sin importar cómo haya ingresado la 
#información el usuario original.



#EJEMPLO 3

# import re

# nombre1="Jara López"

# nombre2="Antonio Gómez"

# nombre3="Lara López"

# if re.match(".ara", nombre3, re.IGNORECASE):

#     print("Hemos encontrado el nombre")

# else:

#      print("no lo hemos encontrado")

#Aqui implementamos el uso del punto (.) como Metacarácter Comodín. Al colocar un punto 
#al inicio del patrón (.ara), le ordenamos al radar que acepte cualquier carácter 
#individual en esa posición, siempre y cuando vaya seguido de la secuencia "ara". 
#El sistema valida los datos de forma exitosa tanto para "Jara" como para "Lara", 
#ya que el punto actúa como una máscara universal para un solo espacio. Esta técnica 
#es vital, ya que permite realizar búsquedas por rima o estructura interna en el disco duro, 
#localizando variaciones de una palabra sin tener que especificar cada letra inicial posible.


#EJEMPLO 4

# import re

# cadena1="Sandra López"

# cadena2="546546546"

# cadena3="a54654654"

# if re.match("\\d", cadena2):

#     print("Hemos encontrado el nombre")

# else:

#      print("no lo hemos encontrado")

#Aqui implementamos la secuencia de escape \d, que funciona como el Radar de Dígitos en 
#el módulo re. Al utilizar este patrón, le ordenamos al sistema que verifique si los 
#datos comienzan con cualquier número entre el 0 y el 9. A diferencia de buscar una cifra 
#específica, \d actúa como una Clase de Carácter Numérica universal. Es fundamental, ya 
#que permite validar de forma instantánea si una cadena de texto en el disco duro 
#contiene información numérica al inicio, permitiendo separar registros alfanuméricos de 
#registros puramente de texto antes de su procesamiento.



#EJEMPLO 5


# import re

# nombre1="Jara López"

# nombre2="Antonio Gómez"

# nombre3="Lara López"

# if re.search("López", nombre2,):

#     print("Hemos encontrado el nombre")

# else:

#      print("no lo hemos encontrado")

#Aqui implementamos el método search(), el cual funciona como el Radar de Rastreo Global. 
#A diferencia de match(), que solo vigila la entrada, search() escanea la cadena completa 
#en el disco duro buscando el patrón en cualquier posición (inicio, medio o final). 
#Al intentar localizar "López" en "Antonio Gómez", el sistema devuelve None porque los datos 
#no coinciden, pero si lo aplicáramos a "Jara López", el hallazgo sería exitoso. 
#Esta técnica es vital para la Soberanía de Datos, ya que permite detectar palabras clave o 
#registros específicos dentro de párrafos extensos o bases de datos no estructuradas, 
#garantizando que ninguna información relevante pase desapercibida.



#EJEMPLO 6


# import re

# codigo1="jdshkfjhsdkfjhdsjfjhsdkjh71hdgfjsdfhgsjdfhgsdjg"

# codigo2="jfhdgsd71kjdhfkjsdhf ksjdhkfsdjh jh"

# codigo3="ufdh gdfhg dh kdhg kjdfhgkjfd hkd"

# if re.search("71", codigo1,):

#     print("Hemos encontrado el nombre")

# else:

#      print("no lo hemos encontrado")

#Aqui ponemos a prueba el Radar de Rastreo Global (search) frente a cadenas de texto de 
#alta complejidad o ruido. Al definir el patrón "71", el sistema ignora la enorme 
#cantidad de caracteres aleatorios y se enfoca exclusivamente en localizar la 
#coincidencia numérica sin importar que esté oculta en el centro de la cadena. 
#Esta técnica es fundamental, ya que permite extraer identificadores, folios 
#o códigos de seguridad embebidos dentro de archivos de registro (logs) o 
#bloques de datos corruptos en el disco duro. Mientras match() fallaría en 
#este escenario por no encontrar el número al inicio, search() garantiza 
#la captura de los datos en cualquier coordenada del bloque.


