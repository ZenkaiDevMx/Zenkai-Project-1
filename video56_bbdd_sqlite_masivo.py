# PILDORAS INFORMATICAS
# PYTHON
# VIDEO 56
# BASE DE DATOS 2

#.INSERCION DE VARIOS REGISTROS
#.RECUPERACION DE VARIOS REGISTROS

#EJEMPLO #1

# import sqlite3

# miConexion=sqlite3.connect(r"E:\Descargas\ESTUDIO\PROGRAMACION\PrimeraBase")

# miCursor=miConexion.cursor()


# variosProductos=[


#     ("Camiseta", 10, "Deportes"),
#     ("Jarrón", 90, "Cerámica"),
#     ("Camión", 20, "Juguetería"),


# ]

# miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", variosProductos)





# miConexion.commit()




# miConexion.close()

#Aquí aprendemos a realizar una carga masiva de datos para no tener que inyectar los registros uno por uno. Primero, 
#definimos una lista de Python llamada variosProductos, donde cada elemento es una tupla que contiene los datos de un 
#artículo (Nombre, Precio, Sección). La clave de este código es el método executemany, que es mucho más eficiente que 
#el comando simple; este recibe la instrucción SQL de inserción y utiliza los signos de interrogación (?,?,?) como 
#"marcadores de posición" o comodines. Estos comodines le indican a SQLite que debe tomar los valores de la lista y 
#repartirlos automáticamente en las columnas correspondientes de la tabla. Finalmente, ejecutamos el commit() para que 
#toda la lista se grabe en el disco duro y cerramos la conexión para mantenerlo optimizado.



#EJEMPLO #2

# import sqlite3

# miConexion=sqlite3.connect(r"E:\Descargas\ESTUDIO\PROGRAMACION\PrimeraBase")

# miCursor=miConexion.cursor()



# miCursor.execute("SELECT * FROM PRODUCTOS")

# variosProductos=miCursor.fetchall()

# print(f" Registros totales recuperados: {len(variosProductos)}")
# print(f" Lista bruta de datos: {variosProductos}")


# miConexion.commit()


# miConexion.close()


#Aquí aprendemos a extraer la información que ya tenemos guardada para poder visualizarla. Utilizamos el comando SQL 
#SELECT *, donde el asterisco funciona como un comodín que le ordena al cursor seleccionar "todas las columnas" de la 
#tabla PRODUCTOS. La pieza clave aquí es el método fetchall(), que actúa como una red de pesca: recupera todos los 
#registros que el cursor encontró y los guarda en la variable variosProductos en forma de una lista de tuplas. 
#Finalmente, usamos un print para mostrar esa lista en la consola y cerramos la conexión. En este caso, el commit() no 
#es estrictamente necesario porque solo estamos leyendo datos y no modificando nada, pero se mantiene para asegurar que 
#la sesión se cierre correctamente.


#EJEMPLO #3

# import sqlite3

# miConexion=sqlite3.connect(r"E:\Descargas\ESTUDIO\PROGRAMACION\PrimeraBase")

# miCursor=miConexion.cursor()



# miCursor.execute("SELECT * FROM PRODUCTOS")

# variosProductos=miCursor.fetchall()

# print(" --- REPORTE DE PRODUCTOS EN EXISTENCIA ---")
# for producto in variosProductos:

#     print(f" Artículo: {producto[0]:<12} | Sección: {producto[2]}")


# miConexion.commit()



# miConexion.close()



#Aquí aprendemos a darle formato y claridad a la información que extraemos de la base de datos, evitando que se muestre 
#como una lista bruta de código. Una vez que el método fetchall() ha capturado todos los registros en la variable 
#variosProductos, utilizamos un bucle for para recorrer esa lista fila por fila. En cada vuelta del bucle, accedemos a 
#los datos específicos de cada registro usando los índices: producto[0] para obtener el nombre y producto[2] para la 
#sección (recordando que en programación empezamos a contar desde 0). Al usar el print dentro del bucle, logramos que 
#la terminal nos entregue un reporte limpio y ordenado de los datos, en lugar de un bloque de texto desordenado. 
#Finalmente, cerramos la conexión para mantenerlo optimizado.
