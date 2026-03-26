# PILDORAS INFORMATICAS
# PYTHON
# VIDEO 34
# MODULOS
# PARTE 1

#MODULOS

#¿QUE SON?

#Un archivo con extensión .py .pyc (Pyhon compilado) o archivo escrito en C para CPyhon, que posee su propio espacio de nombre y que puede contener variables, funciones, clases e incluso otros módulos.

#¿PARA QUE SIRVEN?

#Para organizar y reutilizar el código (modularizacion y reutilización).

#¿COMO SE CREA UN MODULO?

#Tan sencillo como crear un archivo con extensión .py (o pyc o archivo C) y guardarlo donde nos interese.

#EJEMPLO 1

# def sumar(op1,op2):
#     print("El resultado de la suma es: ", op1+op2)

# def restar(op1,op2):
#     print("El resultado de la suma es: ", op1-op2)

# def multiplicar(op1,op2):
#     print("El resultado de la suma es: ", op1*op2)




#EJEMPLO 4

# class Vehiculos():

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

# class Furgoneta(Vehiculos):

#     def carga(self, cargar):
#         self.cargado=cargar
#         if(self.cargado):
#             return "La furgoneta esta cargada"
#         else:
#             return "La furgoneta no esta cargada"


# class Moto(Vehiculos):
#     hcaballito=""
#     def caballito(self):
#         self.hcaballito="Voy haciendo el caballito"

#     def estado(self):
#         print ("Marca: ", self. marca, "\nModelo:", self.modelo, "\nEn Marcha: ", 
#            self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenado: ", self. frena, "\n", self.hcaballito)    

# class VElectricos(Vehiculos):
#     def __init__(self, marca, modelo):
#         super().__init__(marca, modelo)
#         self.autonomia=100

#     def cargarEnergia(self):

#         self.cargando=True
