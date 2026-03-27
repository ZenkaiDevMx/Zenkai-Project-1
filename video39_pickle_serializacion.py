#PILDORAS INFORMATICAS
# PYTHON
# VIDEO 39
# SERIALIZACION 1

#BIBLIOTECAS NECESARIAS

#.Pickle

#-Metodo dump(): volcado de datos al fichero binario externo.
#-Metodo load():carga de los datos del fichero binario externo.

#EJEMPLO 1

# import pickle

# lista_nombres=["Pedro", "Ana", "María", "Isabel"]

# fichero_binario=open(r"E:\Descargas\ESTUDIO\PROGRAMACION\MODULOS\lista_nombres", "wb")

# pickle.dump(lista_nombres, fichero_binario)

# fichero_binario.close()

# del (fichero_binario)

#Aqui utilizamos el metodo pickle para que hacer una lista de nombres, 
#convertirlo en un fichero binario con la funcion dump del metodo pickle,
#muy importante especificar la ruta donde se va guardar, cerrar y limpiar 
#la memoria.

#EJEMPLO 2

# import pickle

# fichero=open(r"E:\Descargas\ESTUDIO\PROGRAMACION\MODULOS\lista_nombres", "rb")
# lista=pickle.load(fichero)

# print(lista)

# fichero.close()

# del (fichero)

#Aqui simplemente importamos el metodo pickle, indicamos
#que queremos abrir la lista convertida a binaria, la lea, 
#y la pueda cargar con la funcion load del metodo pickle y 
#lo imprima esa lista en pantalla.
