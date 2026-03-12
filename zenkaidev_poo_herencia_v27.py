#PILDORAS INFORMATICAS
#PYTHON
#VIDEO 27
#POO 4
#PARTE 1

#EJEMPLO 1

# class Coche():
#    largoChasis=250
#    anchoChasis=120
#    ruedas=4
#    enmarcha=False

#    def arrancar(self):
#        self.enmarcha=True

#    def estado(self):
#        if(self.enmarcha):
#            return "El coche esta en marcha"
 
#        else:

#            return "El coche esta parado"

# miCoche=Coche()

# print("El largo del coche es: ",miCoche.largoChasis)
# print("El coche tiene ", miCoche.ruedas, "ruedas")
# miCoche.arrancar()

# print(miCoche.estado())

# print("-------A continuación creamos el segundo objeto-------")

# miCoche2=Coche()
# print("El largo del coche es: ",miCoche2.largoChasis)
# print("El coche tiene ", miCoche2.ruedas, "ruedas")
# #miCoche.arrancar()
# print(miCoche2.estado())


#Aquí usamos el mismo código que ayer y le agregamos un segundo objeto llamado miCoche2 de la misma clase Coche, 
# con las mismas propiedades y preguntándole su estado, en este caso no arrancaría y mostraría el coche esta parado 
# en el segundo objeto.

#EJEMPLO 2

# class Coche():
#    largoChasis=250
#    anchoChasis=120
#    ruedas=4
#    enmarcha=False

#    def arrancar(self,arrancamos):
#        self.enmarcha=arrancamos

#        if(self.enmarcha):
#             return "El coche esta en marcha"
 
#        else:

#            return "El coche esta parado"

#    def estado(self):
#        print("El coche tiene " , self.ruedas, " ruedas. Un ancho de ", self.anchoChasis, " y un largo de ", self.largoChasis)
                  

# miCoche=Coche()

# print(miCoche.arrancar(True))
# (miCoche.estado())

# print("-------A continuación creamos el segundo objeto-------")

# miCoche2=Coche()

# print(miCoche2.arrancar(False))
# (miCoche2.estado())

#Aquí el método arrancar hace 2 tareas, recibe un parámetro, arranca el coche o no y evalúa 
# y el método estado nos informa las propiedades de la clase Coche, las llamadas al método 
# arrancar tienen que estar en un print, y ya que el método estado esta mostrando las propiedades 
# de la clase Coche, la llamada a ese segundo método de estado debe ir sin el print, ya el código 
# nos mostraría las propiedades de la clase coche y su estado, de cada objeto de miCoche1 y miCoche2, 
# compartirían datos de las propiedades al sacar la info en la misma clase,  el del primer objeto arrancaría 
# por estar en True y el segundo objeto no arrancaría por estar en False por parámetro, que quiere decir, que 
# le "inducimos" a estar en false por lo tanto se va a guardar asi en arrancamos detallando que usamos la etiqueta 
# de la misma clase self enmarcha=arrancamos que previamente es False y por lo tanto se salta el if y nos muestra el 
# else que es el coche esta parado.


#EJEMPLO 3


# class Coche():
#     def __init__(self): 
#         self.__largoChasis = 250
#         self.__anchoChasis = 120
#         self.__ruedas = 4
#         self.__enmarcha = False

#     def arrancar(self, arrancamos):
#         self.__enmarcha = arrancamos
#         if(self.__enmarcha):
#             return "El coche esta en marcha"
#         else:
#             return "El coche esta parado"

#     def estado(self):
#         print("El coche tiene ", self.__ruedas, " ruedas. Un ancho de ", self.__anchoChasis, " y un largo de ", self.__largoChasis)

# # --- INSTANCIACIÓN ---
# miCoche = Coche()
# print(miCoche.arrancar(True))
# miCoche.estado()

# print("------- A continuación creamos el segundo objeto -------")

# miCoche2 = Coche()
# print(miCoche2.arrancar(False))

# # Encapsulamiento en acción: Aunque intentes cambiarlo aquí, 
# # la propiedad __ruedas está protegida por los dos guiones bajos.
# miCoche2.ruedas = 5 
# miCoche2.estado()

#Aquí siguiendo el código del ejemplo anterior, para que usemos los datos de 
# las propiedades especificas iniciales para los objetos que queremos crear, 
# usamos un constructor y para no poder modificar esas mismas propiedades y 
# sean intocable desde fuera de la clase, encapsulamos o blindamos esa parte del código 
# para hacerlo impenetrable, esto nos sirve por ejemplo en el objeto dos tratar de cambiar 
# que las ruedas tienen 5, con esto no importa si le pones __, ya blindamos esa propiedad 
# desde fuera de la clase y es imposible modificarlo asi.

#NOTA: Al crear un objeto ya tiene un estado inicial perteneciente a una clase, y utilizamos 
# un constructor para especificarlo, la sintaxis del constructor seria def__init_(self), 
# encapsulamos con dos guiones bajos __tanto en propiedades como en el objeto, si a un objeto 
# lo dejas sin __ y al otro si tiene, seria como estar diciéndole que son dos distintos y no hubiera 
# repercusión el uno con el otro.

#PARTE 2

# PROYECTO ZENKAI DE SINERGIA: SEMANA 5 - JUEVES
# INTEGRACIÓN: BAYES + PRONOMBRES OBJETO + NÚMEROS 1-99 + ENCAPSULAMIENTO

class BúnkerZenkai():
    # 1. CONSTRUCTOR (Punto de origen del Guerrero)
    def __init__(self):
        # 2. ENCAPSULAMIENTO (Propiedades blindadas con __)
        self.__ryzen_cores = 8          # 八 (Hachi)
        self.__rtx_vram = 16            # 十六 (Juu-roku)
        self.__target_pessu = 60000     # 六万 (Roku-man)
        self.__clima_temp = 18          # 十八 (Juu-hachi)
        self.__is_safe = False

    # 3. COMPORTAMIENTO (Pacho L28: Pronombres Objeto + Duke: Bayes)
    def update_security(self, has_evidence):
        # Lógica Bayesiana: Actualizamos la seguridad basada en evidencia
        # "If there is evidence of power failure, I must check IT" (IT = El No-Break)
        if has_evidence:
            self.__is_safe = True
            return "Evidence received. I checked IT. System is PROTECTED."
        else:
            self.__is_safe = False
            return "No evidence found. I can't protect THEM (The components) yet."

    # 4. ESTADO (Acceso a datos protegidos mediante self)
    def get_status(self):
        # Usamos self.__ para leer las propiedades que nadie más puede tocar
        return f"Specs: {self.__ryzen_cores} Cores / {self.__rtx_vram}GB VRAM. Temp: {self.__clima_temp}°C."

# --- INSTANCIACIÓN Y PRUEBA DE BLINDAJE ---
mi_bunker = BúnkerZenkai()

# Intentamos hackear las especificaciones desde fuera (Como el Ejemplo 3 de hoy)
mi_bunker.__ryzen_cores = 128 # <-- Esto creará una propiedad nueva, NO cambiará la original
mi_bunker.__clima_temp = 40   # <-- El blindaje impide que el calor entre al núcleo

# Ejecución de Lógica Bayesiana (Duke) y Pronombres (Pacho)
print(mi_bunker.update_security(has_evidence=True))

# Verificación de que el blindaje funcionó (Python POO)
print(mi_bunker.get_status())

# Cierre con el "Loot" de Serorinne (Japonés)
print("Kore wa watashi no saikyou no hardware desu! (Este es mi hardware más fuerte)")
