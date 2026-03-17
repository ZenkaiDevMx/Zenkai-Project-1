#PILDORAS INFORMATICAS
#PYTHON
#VIDEO 29
#POO 6 HERENCIA
#PARTE 1

#HERENCIA

#La mejor ganancia a usar la herencia es :

#.Para reutilizar código en caso de crear objetos similares.

#Tienes que preguntarte varias cosas para aplicar la herencia.

#¿Qué características en común tienen todos los objetos?

#¿Qué comportamientos en común tienen todos los objetos?


#EJEMPLO 1

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

# class Moto(Vehiculos):
#     pass

# miMoto=Moto("Honda", "CBR")

# miMoto.estado()


#Aquí creamos una clase llamada Vehiculos y hacemos un constructor que el self obtengo marca y modelo y dentro del constructor, 
# el self es igual a marca, modelo y que tiene por parámetro, también otras caracteristicas enmarca, acelera y frena esten en False 
# y cuando se herede ese objeto va estar en reposo, luego este objeto va tener otros comportamiento o métodos de arrancar, acelerar 
# y frenar que esten en True, y si ejecutamos estos métodos va salir del estado de reposo que habíamos señalo en contructor y va mover, 
# acelerar y frenar, luego que imprima en pantalla el estado de nuestros objetos, al final vamos a crear un objeto que herede la clase 
# vehículo, va heredar todas las propiedad y métodos y la sintaxis para heredes es poner una clase en este caso Moto y incluir el nombre 
# entre parentisis de la clase que heredamos en este caso Vehiculos, ponemos un pass para no construir nada en esta clase moto, luego creamos 
# un nombre de instancia de miMoto=Moto y le pasamos la marca y el modelo para que no nos de error, después utilizamos esa instancia para llamar 
# a cualquiera de los métodos que hemos herado como en este caso mostrar el estado.


#NOTA: \n salto de linea en pantalla, con este objeto de miMoto que pertenece a la clase Moto estamos usando características y método de la 
# clase Vehiculos porque heredamos de ella.

#EJEMPLO 2

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

# class Moto():
#     pass

# miMoto=Moto("Honda", "CBR")

# miMoto.estado()

#Aqui eliminamos la herencia de la clase vehiculos nos marcara error, 
# por que no hay parámetros en el constructor, porque al no heredarlo 
# no puede pasarle sus características y métodos.

#PARTE 2

# PROYECTO ZENKAI SINERGIA: SEMANA 6 - MARTES
# INTEGRACIÓN: INGLÉS (LET) + JAPONÉS (CONTADORES) + PYTHON (HERENCIA)

class SoftwareBase():
    def __init__(self, nombre, version):
        self.nombre = nombre
        self.version = version
        self.is_running = False

    def get_status(self):
        # Sinergia Japonés (L1-13): Contadores y Cortesía
        # Usamos "O-ikutsu" para preguntar cuántos procesos hay
        return f"Software: {self.nombre} V{self.version}. O-ikutsu core active? Hitotsu desu."

class Automatizador(SoftwareBase):
    # Heredamos TODO de SoftwareBase (Atributos y Métodos)
    
    def start_process(self, permission):
        # Sinergia Inglés (L29): Verbo LET y Liaison
        # "Let me automate this task"
        if permission:
            self.is_running = True
            return "Permission granted. Let_me_automate_this_task_now."
        else:
            return "Access denied. Don't_let_it_run_without_auth."

# --- EJECUCIÓN DEL MAGO ---
# Creamos la instancia heredada
mi_script = Automatizador("DataShogun", "1.1")

# 1. Checamos status con cortesía japonesa
print(mi_script.get_status())

# 2. Arrancamos con permisos 
print(mi_script.start_process(permission=True))
