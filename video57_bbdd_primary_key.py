# PILDORAS INFORMATICAS
# PYTHON
# VIDEO 57
# BASE DE DATOS 3

#.Claves principales en las BBDD


#EJEMPLO 1

# import sqlite3


# RUTA_BBDD = r"E:\Descargas\ESTUDIO\PROGRAMACION\GestionProductos"

# miConexion = sqlite3.connect(RUTA_BBDD)
# miCursor = miConexion.cursor()

# Agregamos IF NOT EXISTS para evitar errores si la tabla ya vive en el disco
# miCursor.execute('''
#        CREATE TABLE IF NOT EXISTS PRODUCTOS (
#        CODIGO_ARTICULO VARCHAR(4) PRIMARY KEY,
#        NOMBRE_ARTICULO VARCHAR(50),
#        PRECIO INTEGER,
#        SECCION VARCHAR(20))
# ''')

# productos = [
#      ("AR01", "pelota", 20, "jugueteria"),
#      ("AR02", "pantalón", 15, "confección"),
#      ("AR03", "destornillador", 25, "ferretería"),
#      ("AR04", "jarrón", 45, "cerámica"),
# ]

# miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?,?)", productos)


# print(f"Se han inyectado {len(productos)} registros correctamente en el búnker.")

# miConexion.commit()
# miConexion.close()

#Con este código establecemos la infraestructura del proyecto usando una variable de ruta 
#(RUTA_BBDD), lo que nos da soberanía total para mover la base de datos sin romper el 
#script. Introducimos el blindaje IF NOT EXISTS en la creación de la tabla, asegurando que 
#el programa sea antifrágil y no colapse si la tabla ya fue creada anteriormente. Definimos 
#la columna CODIGO_ARTICULO como PRIMARY KEY, garantizando que cada pieza de datos tenga una 
#identidad única e irrepetible. Para la carga de datos, usamos executemany con los 
#marcadores de posición correspondientes (?,?,?,?) y finalizamos con un reporte en consola 
#mediante f-strings, que nos confirma en tiempo real cuántos registros se grabaron 
#físicamente en el disco duro tras ejecutar el commit(). 
#Si intentáramos correr este código dos veces con los mismos códigos de artículo, Python 
# #lanzaría un error, protegiendo la integridad de nuestra base de datos.



#EJEMPLO 2


# import sqlite3

# RUTA_BBDD = r"E:\Descargas\ESTUDIO\PROGRAMACION\GestionProductos"

# miConexion = sqlite3.connect(RUTA_BBDD)
# miCursor = miConexion.cursor()


# miCursor.execute("INSERT INTO PRODUCTOS VALUES ('AR05', 'tren', 15, 'juguetería')")


# print(f"Registro individual inyectado con éxito en {RUTA_BBDD}")

# miConexion.commit()
# miConexion.close()


#Aquí aplicamos una inserción individual de datos manteniendo la estructura organizada 
#mediante la variable RUTA_BBDD. El comando INSERT INTO se encarga de inyectar una nueva 
#fila de datos en la tabla, asegurándonos de proporcionar un código único ('AR05') para no 
#entrar en conflicto con la PRIMARY KEY establecida. Hemos optimizado el flujo de 
#información utilizando una f-string en el mensaje de confirmación, lo que nos permite 
#verificar visualmente y de forma dinámica la ruta donde se está grabando la información. 
#Como siempre, el método commit() es el encargado de cerrar la transacción y asegurar que el 
#nuevo producto quede blindado permanentemente en el disco duro antes de cerrar la conexión.





#EJEMPLO 3


# import sqlite3


# RUTA_BBDD = r"E:\Descargas\ESTUDIO\PROGRAMACION\GestionProductos"

# miConexion = sqlite3.connect(RUTA_BBDD)
# miCursor = miConexion.cursor()

# Inyección directa a ciegas. Si 'AR03' ya existe, el programa se detendrá aquí.
# miCursor.execute("INSERT INTO PRODUCTOS VALUES ('AR03', 'tren', 15, 'juguetería')")

# Si el código llega aquí, es que no hubo colisión
# print(f"Registro inyectado con éxito en {RUTA_BBDD}")

# miConexion.commit()
# miConexion.close()

#Aqui realizamos una prueba de colisión de datos para verificar la eficacia de la Llave 
#Primaria. Al intentar inyectar un nuevo registro con el código 'AR03', el sistema detecta 
#que esa identidad ya existe en la base de datos (fue creada en el Ejemplo 1). Como 
#definimos esa columna como PRIMARY KEY, SQLite bloquea la operación automáticamente y lanza 
#un error de integridad (IntegrityError). Esto es fundamental en nuestra ingeniería de 
#datos, ya que evita que los datos se dupliquen o se sobrescriban por error, garantizando 
#que cada pieza de información en nuestro disco duro sea única y esté perfectamente 
#localizada. Usamos la variable RUTA_BBDD para tener localizado el punto exacto del 
#conflicto y una f-string que solo se ejecutará si la operación es exitosa, confirmando la 
#validez del nuevo dato. El código termina cerrando la conexión, pero el cambio nunca se 
#graba porque el sistema prioriza la seguridad del archivo existente.




#EJEMPLO 4

# import sqlite3

# RUTA_BBDD = r"E:\Descargas\ESTUDIO\PROGRAMACION\GestionProductos"

# miConexion = sqlite3.connect(RUTA_BBDD)
# miCursor = miConexion.cursor()

# Creamos la tabla con ID automático para no volver a pelear con códigos manuales
# miCursor.execute('''
#        CREATE TABLE IF NOT EXISTS PRODUCTOS (
#        ID INTEGER PRIMARY KEY AUTOINCREMENT,
#        NOMBRE_ARTICULO VARCHAR(50),
#        PRECIO INTEGER,
#        SECCION VARCHAR(20))
# ''')

# productos = [
#      ("pelota", 20, "juguetería"),
#      ("pantalón", 15, "confección"),
#      ("destornillador", 25, "ferretería"),
#      ("jarrón", 45, "cerámica"),
# ]

# Usamos NULL para que la BBDD asigne el ID automáticamente
# miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos)


# print(f"Éxito: Se han inyectado {len(productos)} registros con ID automático en {RUTA_BBDD}")

# miConexion.commit()
# miConexion.close()


#Con este código implementamos la estrategia de ID Autoincremental, que es la evolución 
#definitiva para gestionar la identidad del proyecto. Al definir la columna ID como INTEGER 
#PRIMARY KEY AUTOINCREMENT, le delegamos a SQLite la tarea de asignar un número único y 
#correlativo a cada registro, eliminando para siempre la necesidad de inventar códigos 
#manuales y el riesgo de errores de duplicidad. En la inserción masiva con executemany, 
#pasamos el valor NULL en la primera posición para que el motor de base de datos se encargue 
#de generar la secuencia. Luego con un f-string que nos confirma la inyección exitosa de los 
#datos en el disco duro, Al final, el commit() graba una tabla perfectamente numerada y 
#organizada en el disco duro, facilitando las futuras búsquedas y relaciones entre datos.

