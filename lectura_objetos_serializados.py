#EJEMPLO 4

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


# ficheroApertura = open(r"E:\Descargas\ESTUDIO\PROGRAMACION\MODULOS\losCoches", "rb")

# misCoches=pickle.load(ficheroApertura)

# ficheroApertura.close()

# for c in misCoches:

#     print(c.estado())

#Aquí tenemos que incluir el código inicial especifico de lo que estamos pidiendo de 
#los datos que queremos mostrar, en este caso queremos que muestre los datos de estado 
#del objeto padre Vehiculo, y por eso esta al principio del código, si lo hubiéramos 
#puesto solo desde ficheroApertura, el código no hubiera sabido que leer y hubiera 
#marcado error, pero como lo especificamos, muestra la info correspondiente.