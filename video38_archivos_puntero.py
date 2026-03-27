#PILDORAS INFORMATICAS
# PYTHON
# VIDEO 38
# ARCHIVOS EXTERNOS 2

#EJEMPLO 1

# from io import open

# archivo_texto=open(r"E:\Descargas\ESTUDIO\PROGRAMACION\MODULOS\archivo.txt","r")

# archivo_texto.seek(11)

# print(archivo_texto.read())

# archivo_texto.close()

#Aqui con el metodo seek, le decimos al puntero que empiece en la posicion 11 
#y imprima desde ahi.

#EJEMPLO 2

# from io import open

# archivo_texto=open(r"E:\Descargas\ESTUDIO\PROGRAMACION\MODULOS\archivo.txt","r")

# print(archivo_texto.read(11))

# archivo_texto.close()

#Aqui el metodo read hara una lectura hasta el caracter 11.

#NOTA: Esa es la diferencia entre seek y read, seek empieza desde la posicion del puntero
#y read te lee y imprime hasta el caracter especifico que le dijiste.

#EJEMPLO 3

# from io import open

# archivo_texto=open(r"E:\Descargas\ESTUDIO\PROGRAMACION\MODULOS\archivo.txt","r")

# print(archivo_texto.read(11))

# print(archivo_texto.read())


# archivo_texto.close()

#Aqui hace doble lectura con el metodo read, primero lectura hasta el caracter 11
#y la segunda lectura empieza a partir del caracter donde se quedo la primera lectura,
#en este caso en el caracter numero 12 (l).

#EJEMPLO 4

# from io import open

# archivo_texto=open(r"E:\Descargas\ESTUDIO\PROGRAMACION\MODULOS\archivo.txt","r")

# archivo_texto.seek(len(archivo_texto.read())/2)

# print(archivo_texto.read())

# archivo_texto.close()

#Aqui en combinacion del metodo seek, usamos el metodo len (nos dice la cantidad de caracteres que tiene un string),
#hacemos que lo lea con el metodo read y lo divida entre dos, por ejemplo si tuviera 100 caracteres lo divide entre 2 
#y seria 50 y en ese caracter empezaria y si luego le decimos que imprima el texto, solo imprimira la mitad de nuestro 
#archivo de texto. 

#EJEMPLO 4

# from io import open

# archivo_texto=open(r"E:\Descargas\ESTUDIO\PROGRAMACION\MODULOS\archivo.txt","r")

# archivo_texto.seek(len(archivo_texto.readline()))

# print(archivo_texto.read())

# archivo_texto.close()

#Aqui con el metodo len mas el readline, va leer el texto y se va
#a situar al final de la primera linea y va empezar a leer y imprimir
#desde la segunda linea.

#EJEMPLO 5

# from io import open

# archivo_texto=open(r"E:\Descargas\ESTUDIO\PROGRAMACION\MODULOS\archivo.txt","r+")

# archivo_texto.write("Comienzo del texto")

# archivo_texto.close()


#Aqui le estamos deciendo que dentro del archivo.txt el segundo parametro
#del parametro open r+ que significa que haga lectura y escritura a la vez,
#y ademas con el metodo write le dicimos que escriba Comienzo del texto y como
#no le especificamos en que linea empezar, por defecto va sobreescribir la primera
#linea de texto.

#EJEMPLO 6

# from io import open

# archivo_texto=open(r"E:\Descargas\ESTUDIO\PROGRAMACION\MODULOS\archivo.txt","r+")

# print(archivo_texto.readlines())

# archivo_texto.close()

#Aqui nos devuelve una lista, con saltos de linea y detecta donde esta 
#y los representa con \n en la terminal.


#EJEMPLO 7

# from io import open

# archivo_texto=open(r"E:\Descargas\ESTUDIO\PROGRAMACION\MODULOS\archivo.txt","r+")

# lista_texto=archivo_texto.readlines();

# lista_texto[1]=" Esta línea a ha sido incluida desde el exterior \n"

# archivo_texto.seek(0)

# archivo_texto.writelines(lista_texto)

# archivo_texto.close()

#Aqui le estamos diciendo que lea todo el parrafo y nos convierta a listas el texto,
#con sus respectivos saltos de linea en pantalla, almacenara la lista y le indicamos 
#que sobreescriba una frase, especificamente al principio de la linea del elemento 2,
#gracias al metodo writelines especificandole que haga salto de linea. 