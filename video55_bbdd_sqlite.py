# PILDORAS INFORMATICAS
# PYTHON
# VIDEO 55
# BASE DE DATOS 1



#EJEMPLO #1

# import sqlite3

# miConexion=sqlite3.connect(r"E:\Descargas\ESTUDIO\PROGRAMACION\PrimeraBase")

# miCursor=miConexion.cursor()

# miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

#miConexion.commit()

# miConexion.close()


#Primero importamos el módulo sqlite3, que es el motor que ya viene 
#integrado en el ADN de Python para manejar bases de datos. Creamos el 
#objeto miConexion para abrir el "túnel" hacia nuestro archivo de base de 
#datos en la ruta del disco duro; si el archivo no existe, Python lo crea 
#automáticamente en ese instante. Luego, activamos el miCursor, que 
#funciona como nuestro "obrero especializado" que ejecutará las órdenes 
#dentro de las tablas. Con el método execute, le damos la instrucción 
#maestra en lenguaje SQL para crear nuestra primera tabla llamada 
#PRODUCTOS, definiendo tres columnas con sus tipos de datos: VARCHAR para 
#texto (nombres y secciones) e INTEGER para números (precios). Finalmente, 
#usamos commit() para asegurar que los cambios se graben en el disco y 
#cerramos la conexión para liberar memoria.

#NOTA: Para ir creando diferentes estructuras o bases de datos, solo tienes 
#que modificar la ruta y la instrucción de ejecución:
#miConexion=sqlite3.connect(r"Ruta\NuevaBase")
#miCursor.execute("CREATE TABLE NOMBRE_TABLA (COLUMNA1 TIPO, COLUMNA2 #TIPO)")
#Cada vez que le des al "Play" con una instrucción de CREATE, se fabricará 
#una nueva tabla física en tu archivo, lista para ser llenada con libros o #videos.



#EJEMPLO #2

# import sqlite3

# miConexion=sqlite3.connect(r"E:\Descargas\ESTUDIO\PROGRAMACION\PrimeraBase")

# miCursor=miConexion.cursor()


# miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALON', 15, 'DEPORTES')")

# miConexion.commit()




# miConexion.close()

#Con esta segunda parte, pasamos de crear la estructura a inyectar los 
#datos en nuestra base de datos. Una vez abierta la conexión y activado el 
#miCursor, utilizamos el comando SQL INSERT INTO para indicarle al programa 
#que queremos meter un nuevo registro en la tabla de PRODUCTOS. Entre 
#paréntesis, definimos los VALUES respetando el orden de las columnas que 
#creamos antes: el nombre del artículo como texto ('BALON'), el precio como 
#número (15) y la sección también como texto ('DEPORTES'). Es fundamental 
#usar el método commit() después de la ejecución; sin esta orden, los 
#cambios solo se quedarían flotando en la memoria RAM y no se grabarían 
#físicamente en el archivo del disco duro. Al final, cerramos la conexión 
#para asegurar la integridad de los datos y dejar todo listo para la 
#siguiente operación.

#NOTA: Para ir llenando la tabla con diferentes productos o datos, solo 
#tienes que cambiar el contenido dentro de los paréntesis del VALUES:
#miCursor.execute("INSERT INTO PRODUCTOS VALUES('NUEVO_DATO', PRECIO, 'SECCION')")
#Cada vez que des al "Play", se inyectará una fila nueva en la base de 
#datos, creando un historial acumulativo que no se borra aunque apagues la PC.


