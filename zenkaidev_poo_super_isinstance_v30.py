#PILDORAS INFORMATICAS
#PYTHON
#VIDEO 30
#POO 7 HERENCIA 2
#PARTE 1

#HERENCIA 2

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
#     hcaballito=""
#     def caballito(self):
#         self.hcaballito="Voy haciendo el caballito"

#     def estado(self):
#         print ("Marca: ", self. marca, "\nModelo:", self.modelo, "\nEn Marcha: ", 
#            self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenado: ", self. frena, "\n", self.hcaballito)     

# miMoto=Moto("Honda", "CBR")

# miMoto.caballito()

# miMoto.estado()

#Aquí continuamos el ejemplo anterior y le añadimos una característica a nuestro objeto heredado 
# de la clase vehiculo de clase Moto que es hcaballito y le incluimos y le damos su propia llamada

#NOTA: Cuando estamos en nuestra segunda clase o mas heredada y llamamos en este caso el método de 
# estado de clase Moto invalida/anula/sobreescribe el método estado de clase padre.

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

# miMoto=Moto("Honda", "CBR")

# miMoto.caballito()

# miMoto.estado()

# miFurgoneta=Furgoneta("Renault", "Kangoo")

# miFurgoneta.arrancar()

# miFurgoneta.estado()

# print(miFurgoneta.carga(True))

#Aquí creamos otro objeto llamado Furgoneta que hereda entre otras cosas el constructor de la clase padre Vehiculos, 
# y eso nos pide por parámetro la marca y el modelo y se lo asignamos, también nuestro objeto Furgoneta podrá arrancar, 
# el estado y cargar poniéndole un True para decirle al programa que esta cargada lo envolvemos en un print para que nos 
# imprima que la furgoneta esta cargada.

#EJEMPLO 3

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

# class VElectricos():
#     def __init__(self):
#          self.autonomia=100

#     def cargarEnergia(self):

#         self.cargando=True

# miMoto=Moto("Honda", "CBR")

# miMoto.caballito()

# miMoto.estado()

# miFurgoneta=Furgoneta("Renault", "Kangoo")

# miFurgoneta.arrancar()

# miFurgoneta.estado()

# print(miFurgoneta.carga(True))

# class BicicletaElectrica(VElectricos,Vehiculos):
 
#     pass

# miBici=BicicletaElectrica()

#Aquí agregamos dos objetos nuevos uno que es Velectricos y el otro BicicletaElectrica, que ambos objetos compartan bastante afinidad 
# al tener el núcleo que son eléctricos, el objeto Velectricos no hereda ninguna clase es independiente y el objeto BicicletaElectrica 
# hacemos que herede tanto la clase Velectricos y la clase padre Vehiculos porque también tiene afinidad base con el, y obtiene todos 
# los métodos y propiedades de ambos


#NOTA: En Python permite herencia multiple fácilmente, y cuando usamos dos o mas clases heredadas 
# siempre se da preferencia a la primera o a la que este mas a la izquierda para usar ese constructor.

#PARTE 2

# PROYECTO ZENKAI SINERGIA: SEMANA 6 - MIÉRCOLES
# INTEGRACIÓN: LIAISON + KANJIS + HERENCIA MÚLTIPLE

class BaseSistemas():
    def __init__(self):
        # Kanji: 情報 (Jhouhou - Información)
        self.data_status = "情報 OK"

class HerramientaAutomatica():
    def __init__(self):
        # Kanji: 自動 (Jidou - Automático)
        self.mode = "自動 ON"

    def run_script(self):
        # Sinergia Inglés: Liaison (_)
        return "I’ll_automate_this_task_now."

# HERENCIA MÚLTIPLE: Hereda de ambos padres
class MagoDatos(BaseSistemas, HerramientaAutomatica):
    def __init__(self):
        # Llamamos al primer padre (BaseSistemas)
        super().__init__()
        # Inicializamos el modo manual para no chocar
        self.mode = "自動 ACTIVE"

    def check_efficiency(self):
        # Sinergia Japonés: 効率 (Kouritsu - Eficiencia)
        return "効率 (Efficiency) is high."

# --- EJECUCIÓN ---
mi_bot = MagoDatos()

# 1. Verificamos el motor (Liaison)
print(mi_bot.run_script())

# 2. Verificamos el Radar de Kanjis
print(f"Status: {mi_bot.data_status} | Mode: {mi_bot.mode}")
print(mi_bot.check_efficiency())
