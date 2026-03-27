#PILDORAS INFORMATICAS
# PYTHON
# VIDEO 37
# ARCHIVOS EXTERNOS
# PARTE 1

#EJEMPLO 1

# from io import open

# archivo_texto=open(r"E:\Descargas\ESTUDIO\PROGRAMACION\MODULOS\archivo.txt","w")

# frase="Estupendo dia para estudiar Python \n el miercoles"

# archivo_texto.write(frase)

# archivo_texto.close()

#NOTA: podemos abrir el archivo en modo lectura, escritura, 
#append (agregar info de un archivo que ya existe y ya hay info en su interior).

#EJEMPLO 2

# from io import open

# archivo_texto=open(r"E:\Descargas\ESTUDIO\PROGRAMACION\MODULOS\archivo.txt","r")

# texto=archivo_texto.read()

# archivo_texto.close()

# print(texto)


#EJEMPLO 3

# from io import open

# archivo_texto=open(r"E:\Descargas\ESTUDIO\PROGRAMACION\MODULOS\archivo.txt","r")

# lineas_texto=archivo_texto.readlines()

# archivo_texto.close()

# print(lineas_texto[0])


#Usamos el metodo readlines() lee la info linea a linea 
#y almacena la info en una lista para buscar/manipular mas facil,
#le podemos indicar que busque desde el elemento 0 o la primera linea de texto, 
#imprimira solo eso.

#NOTA: aqui podemos usar tambien bucles for, o condicionales para buscar un elemento
#en concreto. 

#EJEMPLO 4

# from io import open

# archivo_texto=open(r"E:\Descargas\ESTUDIO\PROGRAMACION\MODULOS\archivo.txt","a")

# archivo_texto.write("\n siempre es una buena ocasion para estudiar Pyhon")

# archivo_texto.close()

#Aqui usamos el metodo append para abrir el archivo en modo agregar, 
#para añadir una nueva linea con el metodo write.
