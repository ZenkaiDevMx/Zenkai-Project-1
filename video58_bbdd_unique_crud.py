# PILDORAS INFORMATICAS
# PYTHON
# VIDEO 58
# BASE DE DATOS 4

#.Clausula UNIQUE
#.Operaciones CRUD

#EJEMPLO 1


# import sqlite3


# RUTA_BBDD = r"E:\Descargas\ESTUDIO\PROGRAMACION\GestionProductos"

# miConexion = sqlite3.connect(RUTA_BBDD)
# miCursor = miConexion.cursor()

# Agregamos la cláusula UNIQUE al nombre del artículo para evitar duplicados lógicos
# miCursor.execute('''
#        CREATE TABLE IF NOT EXISTS PRODUCTOS (
#        ID INTEGER PRIMARY KEY AUTOINCREMENT,
#        NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
#        PRECIO INTEGER,
#        SECCION VARCHAR(20))
# ''')

# productos = [
#      ("pelota", 20, "juguetería"),
#      ("pantalón", 15, "confección"),
#      ("destornillador", 25, "ferretería"),
#      ("jarrón", 45, "cerámica"),
# ]

# Usamos try para evitar que el programa colapse si intentamos insertar nombres repetidos
# try:
#     miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos)
#     print(f"Éxito: Se han inyectado {len(productos)} registros con ID automático en {RUTA_BBDD}")
# except sqlite3.IntegrityError:
#     print(f"AVISO: Uno o más productos ya existen en {RUTA_BBDD}. No se duplicó los 'datos'.")

# miConexion.commit()
# miConexion.close()

#En esta actualización del sistema elevamos la seguridad del proyecto al introducir la restricción UNIQUE en la columna 
#NOMBRE_ARTICULO. Esto significa que, además de tener un ID automático irrepetible, el motor de la base de datos ahora 
#impedirá que existan dos productos con el mismo nombre, blindando la información contra redundancias lógicas. 
#Mantenemos la estructura de AUTOINCREMENT para que el ID se gestione solo, pero al usar executemany, ahora el sistema 
#valida doblemente la integridad de los "datos" antes de guardarla. Implementamos un bloque try/except para que, si el 
#sistema detecta un nombre duplicado, emita un reporte controlado mediante f-strings en lugar de detener la ejecución 
#del programa de forma violenta.



#EJEMPLO 2


# import sqlite3

# RUTA_BBDD = r"E:\Descargas\ESTUDIO\PROGRAMACION\GestionProductos"

# miConexion = sqlite3.connect(RUTA_BBDD)
# miCursor = miConexion.cursor()

# Mantenemos el blindaje UNIQUE para proteger la integridad de los datos
# miCursor.execute('''
#        CREATE TABLE IF NOT EXISTS PRODUCTOS (
#        ID INTEGER PRIMARY KEY AUTOINCREMENT,
#        NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
#        PRECIO INTEGER,
#        SECCION VARCHAR(20))
# ''')

# INTENTO DE INYECCIÓN: El segundo 'pantalón' causará una colisión de datos
# productos = [
#      ("pelota", 20, "juguetería"),
#      ("pantalón", 15, "confección"),
#      ("destornillador", 25, "ferretería"),
#      ("jarrón", 45, "cerámica"),
#      ("pantalón", 35, "confección"), 
# ]

# try:
#     miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos)
#     miConexion.commit()
#     print(f"Éxito: Se han inyectado {len(productos)} nuevos registros en {RUTA_BBDD}")
# except sqlite3.IntegrityError:
#     # f-string para reportar que el sistema de defensa UNIQUE bloqueó el duplicado
#     print(f"BLOQUEO DE SEGURIDAD: Se detectó un nombre duplicado en la lista. No se realizaron cambios para evitar basura en el disco.")

# miConexion.close()

#En este ejercicio realizamos una prueba de colisión lógica para verificar el funcionamiento de la restricción UNIQUE. 
#Al intentar inyectar una lista que contiene dos veces el artículo "pantalón", el motor de la base de datos detecta una 
#violación de integridad y detiene la operación. Gracias al uso de la variable RUTA_BBDD, tenemos localizado el archivo 
#en el disco duro, y mediante el bloque try/except, evitamos que el programa colapse con errores rojos. El sistema 
#prioriza la limpieza de los "datos"; si un solo elemento de la lista falla por estar repetido, la transacción completa 
#se bloquea, asegurando que no entre información redundante ni contradictoria (como dos precios diferentes para el 
#mismo nombre) en nuestro proyecto.



#EJEMPLO 3


# import sqlite3

# RUTA_BBDD = r"E:\Descargas\ESTUDIO\PROGRAMACION\GestionProductos"

# miConexion = sqlite3.connect(RUTA_BBDD)
# miCursor = miConexion.cursor()

# Mantenemos la estructura blindada con UNIQUE
# miCursor.execute('''
#        CREATE TABLE IF NOT EXISTS PRODUCTOS (
#        ID INTEGER PRIMARY KEY AUTOINCREMENT,
#        NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
#        PRECIO INTEGER,
#        SECCION VARCHAR(20))
# ''')

# Lista de datos corregida: "pantalónes" ya no colisiona con "pantalón"
# productos = [
#      ("pelota", 20, "juguetería"),
#      ("pantalón", 15, "confección"),
#      ("destornillador", 25, "ferretería"),
#      ("jarrón", 45, "cerámica"),
#      ("pantalónes", 35, "confección"),
# ]

# try:
#     miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos)
#     miConexion.commit()
    # f-string para reporte dinámico de inyección exitosa
#     print(f"Éxito: Se han inyectado {len(productos)} registros con ID automático en {RUTA_BBDD}")
# except sqlite3.IntegrityError:
#     print(f"ERROR: No se pudo inyectar la información en {RUTA_BBDD}. Revisa duplicados.")

# miConexion.close()

#Aquí verificamos que la restricción UNIQUE es estrictamente literal. Al modificar el nombre de "pantalón" a 
#"pantalónes", el motor de la base de datos deja de considerarlo un duplicado y permite la inyección masiva de los 5 
#registros de forma exitosa. Utilizamos la variable RUTA_BBDD para asegurar que los "datos" se guarde exactamente en 
#nuestro archivo del disco duro. El método executemany procesa la lista completa y, gracias al commit(), los datos 
#quedan grabados físicamente con sus respectivos IDs autoincrementales, manteniendo la integridad del proyecto sin 
#conflictos de identidad.



#EJEMPLO 4


# import sqlite3

# RUTA_BBDD = r"E:\Descargas\ESTUDIO\PROGRAMACION\GestionProductos"

# miConexion = sqlite3.connect(RUTA_BBDD)
# miCursor = miConexion.cursor()

# Búsqueda filtrada: Importante respetar mayúsculas, minúsculas y acentos (Case Sensitive)
# seccion_buscada = "confección"
# miCursor.execute(f"SELECT * FROM PRODUCTOS WHERE SECCION='{seccion_buscada}'")

# productos = miCursor.fetchall()

# Reporte detallado usando f-strings para cada registro encontrado
# print(f"Resultados encontrados en la sección '{seccion_buscada}':")
# for p in productos:
#     print(f"ID: {p[0]} | Artículo: {p[1]} | Precio: {p[2]}")

# miConexion.close()

#Aqui implementamos el filtrado de datos mediante la cláusula WHERE. Esta instrucción le permite al cursor localizar 
#únicamente los "datos" que cumplan con una condición específica (en este caso, que pertenezcan a la sección 
#'confección'). Es vital entender que las búsquedas en SQL son Case Sensitive, lo que significa que el sistema 
#distingue estrictamente entre mayúsculas, minúsculas y tildes; si escribiéramos "confeccion" sin acento, el búnker no 
#devolvería ningún resultado. Usamos el método fetchall() para capturar los registros coincidentes y los mostramos de 
#forma organizada mediante un bucle y f-strings, extrayendo la información directamente del disco duro de forma precisa 
#y localizada.



#EJEMPLO 5


# import sqlite3

# RUTA_BBDD = r"E:\Descargas\ESTUDIO\PROGRAMACION\GestionProductos"

# miConexion = sqlite3.connect(RUTA_BBDD)
# miCursor = miConexion.cursor()

# Actualización de datos: Cambiamos el precio de un artículo específico
# nuevo_precio = 35
# articulo = 'pelota'

# Usamos f-string para construir la instrucción SQL de forma limpia
# miCursor.execute(f"UPDATE PRODUCTOS SET PRECIO={nuevo_precio} WHERE NOMBRE_ARTICULO='{articulo}'")

# Confirmación en consola del cambio realizado
# print(f"Éxito: El precio de '{articulo}' ha sido actualizado a {nuevo_precio} en el proyecto.")

# miConexion.commit()
# miConexion.close()

#Con este código implementamos la instrucción UPDATE, que nos permite modificar los "datos" que ya residen en nuestro 
#disco duro sin necesidad de crear registros nuevos. La clave de esta operación es la cláusula SET, donde definimos el 
#nuevo valor para la columna PRECIO, seguida de la cláusula WHERE, que actúa como un rifle de precisión para indicar 
#exactamente qué registro queremos alterar (en este caso, el artículo 'pelota'). Es extremadamente importante usar 
#siempre el WHERE en una actualización; de lo contrario, el sistema cambiaría el precio de todos los artículos de la 
#tabla por error. Finalizamos con el método commit() para asegurar que el cambio de precio se grabe permanentemente en 
#la base de datos antes de cerrar la conexión.




#EJEMPLO 6


# import sqlite3

# RUTA_BBDD = r"E:\Descargas\ESTUDIO\PROGRAMACION\GestionProductos"

# miConexion = sqlite3.connect(RUTA_BBDD)
# miCursor = miConexion.cursor()

# Eliminación quirúrgica: Borramos un registro específico usando su ID único
# id_a_eliminar = 5

# Ejecutamos la orden de borrado filtrando por la Llave Primaria
# miCursor.execute(f"DELETE FROM PRODUCTOS WHERE ID={id_a_eliminar}")

# Confirmación de la purga de datos
# print(f"Misión cumplida: El registro con ID {id_a_eliminar} ha sido eliminado de {RUTA_BBDD}.")

# miConexion.commit()
# miConexion.close()

#En esta etapa final del bloque implementamos la instrucción DELETE, que nos permite eliminar definitivamente los 
#"datos" que ya no es necesaria en nuestro disco duro. La pieza fundamental aquí es la cláusula WHERE, la cual 
#utilizamos junto con el ID (Llave Primaria) para realizar un borrado quirúrgico y preciso; esto garantiza que solo 
#eliminemos el registro exacto que deseamos (en este caso, el ID 5) sin afectar al resto de la tabla. Al igual que con 
#la actualización, omitir el WHERE en un DELETE causaría una catástrofe de datos, borrando absolutamente toda la 
#información de la tabla de un solo golpe. Tras ejecutar la orden, el método commit() sella la eliminación físicamente 
#en la base de datos, optimizando el espacio y manteniendo el orden jerárquico del proyecto.

