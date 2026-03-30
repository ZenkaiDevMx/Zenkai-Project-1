#PILDORAS INFORMATICAS
# PYTHON
# VIDEO 40
# SERIALIZACION 2

#EJEMPLO 1

# import pickle

# class Vehiculo():

#     def __init__(self, marca, modelo):

#        self.marca=marca
#        self.modelo=modelo
#        self.enmarcha=False
#        self.acelera=False
#        self.frena=False

#     def arrancar(self):
#        self.enmarcha=True

#     def acelerar(self):
#        self.acelera=True

#     def frenar(self):
#        self.frena=True

#     def estado(self):
#         print ("Marca: ", self. marca, "\nModelo:", self.modelo, "\nEn Marcha: ", 
#            self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenado: ", self. frena)

# coche1=Vehiculo("Mazda", "MX5")

# coche2=Vehiculo("Seat", "Leon")

# coche3=Vehiculo("Renault", "Megane")

# coches=[coche1, coche2, coche3]

# fichero = open(r"E:\Descargas\ESTUDIO\PROGRAMACION\MODULOS\losCoches", "wb")

# pickle.dump(coches, fichero)

# fichero.close()

# del (fichero)

#Aquí importamos el modulo pickle para empaquetar todos los objetos de la clase padre 
# #vehículos y sus subclases, especificando la ruta exacta en el fichero open y usamos 
# #el pickle dump para serializarlos el nombre de la colección y el nombre del fichero 
# #donde queremos volcar la info, cerramos y borramos el fichero de la memoria.

#EJEMPLO 2

# import pickle

# class Vehiculo():

#     def __init__(self, marca, modelo):

#        self.marca=marca
#        self.modelo=modelo
#        self.enmarcha=False
#        self.acelera=False
#        self.frena=False

#     def arrancar(self):
#        self.enmarcha=True

#     def acelerar(self):
#        self.acelera=True

#     def frenar(self):
#        self.frena=True

#     def estado(self):
#         print ("Marca: ", self. marca, "\nModelo:", self.modelo, "\nEn Marcha: ", 
#            self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenado: ", self. frena)

# coche1=Vehiculo("Mazda", "MX5")

# coche2=Vehiculo("Seat", "Leon")

# coche3=Vehiculo("Renault", "Megane")

# coches=[coche1, coche2, coche3]

# fichero = open(r"E:\Descargas\ESTUDIO\PROGRAMACION\MODULOS\losCoches", "wb")

# pickle.dump(coches, fichero)

# fichero.close()

# del (fichero)

# ficheroApertura = open(r"E:\Descargas\ESTUDIO\PROGRAMACION\MODULOS\losCoches", "rb")

# misCoches=pickle.load(ficheroApertura)

# ficheroApertura.close()

# for c in misCoches:

#     print(c)

#Aquí estamos abriendo/leyendo el archivo previamente empaquetado(serializado), 
# con el método pickle.load y va mostrar los datos de los 3 objetos de misCoches.

#EJEMPLO 3

# import pickle

# class Vehiculo():

#     def __init__(self, marca, modelo):

#        self.marca=marca
#        self.modelo=modelo
#        self.enmarcha=False
#        self.acelera=False
#        self.frena=False

#     def arrancar(self):
#        self.enmarcha=True

#     def acelerar(self):
#        self.acelera=True

#     def frenar(self):
#        self.frena=True

#     def estado(self):
#         print ("Marca: ", self. marca, "\nModelo:", self.modelo, "\nEn Marcha: ", 
#            self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenado: ", self. frena)

# coche1=Vehiculo("Mazda", "MX5")

# coche2=Vehiculo("Seat", "Leon")

# coche3=Vehiculo("Renault", "Megane")

# coches=[coche1, coche2, coche3]

# fichero = open(r"E:\Descargas\ESTUDIO\PROGRAMACION\MODULOS\losCoches", "wb")

# pickle.dump(coches, fichero)

# fichero.close()

# del (fichero)

# ficheroApertura = open(r"E:\Descargas\ESTUDIO\PROGRAMACION\MODULOS\losCoches", "rb")

# misCoches=pickle.load(ficheroApertura)

# ficheroApertura.close()

# for c in misCoches:

#     print(c.estado())

#Aquí va imprimir los datos que están guardado en el estado del objeto padre.

