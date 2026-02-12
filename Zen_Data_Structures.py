#PARTE 1: APRENDIZAJE (TEORÍA)
#TUPLAS


#Ejemplo 1

mitupla=("Juan", 13,1,1995)
print(mitupla[2])

1

#Esta marcando en el ejemplo el elemento 2

#también se pueden convertir tuplas en listas y listas en tuplas,para convertir una tupla en lista usamos con el método list

#Ejemplo 2

mitupla=("Juan", 13,1,1995)
milista=list(mitupla)
print(milista)

['Juan', 13, 1, 1995]

#Imprime una lista porque empieza por los corchetes [ y cierra en ].

#Ejemplo 3

mitupla=("Juan", 13,1,1995)
milista=list(mitupla)
print(mitupla)

('Juan', 13, 1, 1995)

#Imprime una tupla porque empieza por parentisis( y cierra en ).

#Ejemplo 4

milista=["Juan", 13,1,1995]
milista=tuple(milista)
print(mitupla)

('Juan', 13, 1, 1995)

#Para convertir una lista en tupla usamos el método tuple

#Ejemplo 5

milista=["Juan", 13,1,1995]
milista=tuple(milista)
print("Juan" in mitupla)

#Para comprobar si hay elementos dentro de la tupla, declarar primero una lista y luego convertirlo como tupla para almacenarlo en la variable mitupla se usa el metodo in, si se encuentra debe decir True sino False.

#Ejemplo 6

milista=["Juan", 13,1,1995]
milista=tuple(milista)
print(mitupla.count(13))

1

#El método count nos permite averiguar cuantos elementos están dentro de una tupla, en el ejemplo es buscar cuantos  numeros entero 13 hay en la tupla, arroja 1

#Ejemplo 7

milista=["Juan", 13,1,1995,13]
mitupla=tuple(milista)
print(mitupla.count(13))

2

#En este ejemplo agregamos un elemento repetido en la dupla que es un numero entero 13 al final, entonces cuando busque cuantos elementos hay, pondrá 2

#Ejemplo 8

milista=["Juan", 13,1,1995,13]
mitupla=tuple(milista)
print(len(mitupla))

5

#Para averiguar la longitud de una tupla usamos el método len, te dice cuantos elementos hay, en este caso arroja 5.

#Ejemplo 9

mitupla=("Juan",)
print(len(mitupla))

1

#Se pueden crear tuplas unitarias, una tupla con un único elemento, el elemento que queramos almacenar poner en comillas, ejemplo ("Juan")

#Ejemplo 10

mitupla="Juan",13,1,1995
print(mitupla)

('Juan', 13, 1, 1995)

#Se puede poner una tupla sin paréntesis, pero puedo crear confusiones con otros parámetros, por eso es mejor poner los parantesis, ponerlo sin parentisis, se llama empaquetado de tupla


#Ejemplo 11

mitupla=("Juan",13,1,1995)
nombre, dia, mes, agno=mitupla
print(nombre)
print(dia)
print(agno)
print(mes)

#Desempaquetado de tuplas, que significa estas variables separadas por comas es igual a la tupla que hemos creado, la instrucción del ejemplo es asignar cada uno de los valores de la tupla por orden a las variables declaradas o sea es asi

#y no importa que no declares la impresión en orden, automáticamente se imprime en el orden que almacenaste la tupla.

#No se pueden modificar las tuplas.

#DICCIONARIOS

#Ejemplo 1

midiccionario={"Alemania":"Berlin","Francia": "Paris","Reino Unido":"Londres", "España":"Madrid"}
print(midiccionario["Francia"])

#Los diccionarios responden a códigos específicos, en este caso el Pais seria el código y lo asignamos con los dos puntos : a otro elemento, en este caso es la capital de dicho país y en el ejemplo arroja Paris.

#Ejemplo 2

midiccionario={"Alemania":"Berlin","Francia": "Paris","Reino Unido":"Londres", "España":"Madrid"}
print(midiccionario)

#Si queremos que nos imprima o acceder a todo el diccionario, le ponemos el nombre del diccionario

#Ejemplo 3

midiccionario={"Alemania":"Berlin","Francia": "Paris","Reino Unido":"Londres", "España":"Madrid"}
midiccionario["Italia"]="Lisboa"
print(midiccionario)

#Como agregar un elemento mas a un diccionario ya construido después de haberlo declarado, hay que poner el nombre del diccionario, y asignar una clave a este nuevo valor en este caso el país Italia pones igual al valor que vas a poner en este caso Lisboa.

#Ejemplo 4

midiccionario={"Alemania":"Berlin","Francia": "Paris","Reino Unido":"Londres", "España":"Madrid"}
midiccionario["Italia"]="Lisboa"
print(midiccionario)
midiccionario["Italia"]="Roma"
print(midiccionario)


#Como modificar un elemento erróneo o corregirlo, hacer que imprima el diccionario dos veces, solo es necesario sobreescribirla con la misma clave en este caso Italia y poner el valor corregido Roma, nunca puede existir 2 claves iguales

#Ejemplo 5

midiccionario={"Alemania":"Berlin","Francia": "Paris","Reino Unido":"Londres", "España":"Madrid"}
midiccionario["Italia"]="Lisboa"
print(midiccionario)
midiccionario["Italia"]="Roma"
print(midiccionario)
del midiccionario["Reino Unido"]
print(midiccionario)

#Como eliminar un elemento, en este caso a Reino Unido y Londres usando el método del, pones el método del, nombre del diccionario y la clave cuyo valor que quieres eliminar, en este caso seria la pareja clave-valor (Reino Unido - Londres)

#Ejemplo 6

midiccionario={"Alemania":"Berlin",23:"Jordan", "Mosqueteros":3}
print(midiccionario) 


#Como seria un diccionario que haya una mezcla en cuanto tipos (string, texto, etc)

#Ejemplo 7

milista=["España", "Francia", "Reino Unido", "Alemania"]
midiccionario={milista[0]:"Madrid", milista[1]:"Paris", milista[2]:"Londres", milista[3]:"Berlin"}
print(midiccionario)


#Usar una lista con valores de texto, ahora hay que declarar un diccionario, si queremos que ese diccionario tome a la lista para asignar las claves a cada uno de los valores hay que acceder a los elementos de una lista y imprimes el diccionario


#Ejemplo 8

mitupla=("España", "Francia", "Reino Unido", "Alemania") # <--- USAMOS PARÉNTESIS
midiccionario={mitupla[0]:"Madrid", mitupla[1]:"Paris", mitupla[2]:"Londres", mitupla[3]:"Berlin"}
print(midiccionario["Francia"])


#Acceder a un elemento en concreto, puedes decirle en print de tu diccionario que quieras buscas y poner el valor que quieres aaceder en este caso Francia o también puedes decirle diccionario de mi lista 1.

#Ejemplo 9

midiccionario={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago","anillos":[1991,1992,1993,1996,1997,1998]}
print(midiccionario)

#Como hacer que un diccionario almacene en su interior junto con otros valores una lista entera de valores, creamos un diccionario y le vamos asignando los valores, especificamos en la clave anillos varios valores de tipo string (1991, etc) respetando los corchetes al principio y al final, imprimo mi diccionario para que me muestre todo los elementos.

#Ejemplo 10

midiccionario={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago","anillos":[1991,1992,1993,1996,1997,1998]}
print(midiccionario["anillos"])


#Si quiero acceder a la clave anillos, le tuviera que poner a mi diccionario de anillos, la cual es la clave que hemos asignado una lista, imprimimos y nos debería mostrar en este caso Chicago.

#Ejemplo 11

midiccionario={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago","anillos":{"temporadas":[1991,1992,1993,1996,1997,1998]}}
print(midiccionario)


#Guardar un diccionario dentro de otro diccionario y el segundo diccionario tiene dentro una lista en anillos, abrimos una llave y ponemos un subdiccionario (temporadas) y en los valores string esta la lista y cerramos todo con otra llave.

#Ejemplo 12

midiccionario={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago","anillos":{"temporadas":[1991,1992,1993,1996,1997,1998]}}
print(midiccionario.keys())
print(midiccionario.values())
print(len(midiccionario))

#Si usamos keys nos imprimi todas las claves del diccionario como 23, value nos imprimi los valores de las claves como Jordan y len la longitud del diccionario, el numero de cuantos hay en este caso 4.







#PARTE 2: IMPLEMENTACIÓN REAL (RETO ZENKAI)

# Diccionario con el inventario actual de mi Búnker
bunker_setup = {
    "CPU": "Ryzen 7 7700X",
    "GPU": "RTX 5060 Ti",
    "VRAM_GB": 16,
    "Motherboard": "ASRock B650M",
    "Monitor": "19 inch VGA (Legacy)",
    "Status": "Zenkai Mode Active"
}

# Tupla con mis metas inmutables para Agosto 2026
# (Usamos tupla porque estas metas NO se cambian, se cumplen)
metas_agosto_2026 = ("Inglés B2", "Python Junior", "Primer Empleo Tech")

# Probando el acceso a los datos
print("--- REPORTE DE SISTEMA ZENKAIDEVMX ---")
print(f"Hardware detectado: {bunker_setup['GPU']} con {bunker_setup['VRAM_GB']}GB de VRAM.")
print(f"Estado del Guerrero: {bunker_setup['Status']}")
print(f"Hoja de ruta sellada: {metas_agosto_2026}")

# Verificando si el escudo CyberPower ya está en el diccionario
print("¿Escudo CyberPower activo?:", "Shield" in bunker_setup)