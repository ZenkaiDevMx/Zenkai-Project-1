#PILDORAS INFORMATICAS
#PYTHON
#VIDEO 28
#POO 5
#PARTE 1



#EJEMPLO 1

# class Coche():
#     def __init__(self): 
#         self.__largoChasis = 250
#         self.__anchoChasis = 120
#         self.__ruedas = 4
#         self.__enmarcha = False

#     def arrancar(self, arrancamos):
#         self.__enmarcha = arrancamos

#         if(self.__enmarcha):
#             chequeo=self.chequeo_interno()

#         if(self.__enmarcha and chequeo):
#             return "El coche esta en marcha"

#         elif(self.__enmarcha and chequeo==False):
#              return "Algo ha ido mal en el chequeo, no podemos arrancar"

#         else:
#             return "El coche esta parado"

#     def estado(self):
#         print("El coche tiene ", self.__ruedas, " ruedas. Un ancho de ", self.__anchoChasis, " y un largo de ", self.__largoChasis)

#     def chequeo_interno(self):
#         print("realizando chequeo interno")

#         self.gasolina="ok"
#         self.aceite="ok"
#         self.puertas="cerradas"

#         if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):

#             return True

#         else:

#             return False


# miCoche = Coche()

# print(miCoche.arrancar(True))

# miCoche.estado()

# print("------- A continuación creamos el segundo objeto -------")

# miCoche2 = Coche()
# print(miCoche2.arrancar(False))

# miCoche2.estado()


#Aquí seguimos con el código anterior, y queremos ahora que antes de todo, 
# haga un chequeo interno donde la gasolina, aceita y las puertas esta en orden, 
# para eso usamos un método chequeo_interno y aplicamos un if si todo esta ok nos 
# devuelve un True y si no un else y nos devuelve un False, todo esto se va  a comprobar 
# con un if en el bloque del método arrancar, haciendo un if que si es True se guarda en 
# la variable chequeo y devuelva el coche esta en marcha y si no sea un False el coche esta 
# un parado y además agregamos un elif, si haciendo el chequeo algo se hizo mal nos devuelva 
# algo ha ido mal en el chequeo, lo que hará es que la instancia de la clase coche y imprimimos 
# el resultado de ese arranque si esta parado o arrancado y después muestra el estado del coche y 
# también la instancia del objeto dos es exactamente el mismo proceso.


#EJEMPLO 2

# class Coche():
#     def __init__(self): 
#         self.__largoChasis = 250
#         self.__anchoChasis = 120
#         self.__ruedas = 4
#         self.__enmarcha = False

#     def arrancar(self, arrancamos):
#         self.__enmarcha = arrancamos

#         if(self.__enmarcha):
#             chequeo=self.chequeo_interno()

#         if(self.__enmarcha and chequeo):
#             return "El coche esta en marcha"

#         elif(self.__enmarcha and chequeo==False):
#              return "Algo ha ido mal en el chequeo, no podemos arrancar"

#         else:
#             return "El coche esta parado"

#     def estado(self):
#         print("El coche tiene ", self.__ruedas, " ruedas. Un ancho de ", self.__anchoChasis, " y un largo de ", self.__largoChasis)

#     def chequeo_interno(self):
#         print("realizando chequeo interno")

#         self.gasolina="ok"
#         self.aceite="ok"
#         self.puertas="cerradas"

#         if(self.gasolina=="ok" and self.aceite=="mal" and self.puertas=="cerradas"):

#             return True

#         else:

#             return False


# miCoche = Coche()

# print(miCoche.arrancar(True))

# miCoche.estado()

# print("------- A continuación creamos el segundo objeto -------")

# miCoche2 = Coche()
# print(miCoche2.arrancar(False))

# miCoche2.estado()

#Aquí en el chequeo interno, y detectara que el aceite este mal 
# nos va devolver False porque todos deben estar en ok si uno falla 
# daba False, en nuestro primer coche arranca y se almacena el False 
# en nuestro primer if, no se cumple el primer if entonces se va al elif 
# y nos imprime que algo ha ido mal en el chequeo, no podemos arrancar.



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
#             chequeo=self.__chequeo_interno()

#         if(self.__enmarcha and chequeo):
#             return "El coche esta en marcha"

#         elif(self.__enmarcha and chequeo==False):
#              return "Algo ha ido mal en el chequeo, no podemos arrancar"

#         else:
#             return "El coche esta parado"

#     def estado(self):
#         print("El coche tiene ", self.__ruedas, " ruedas. Un ancho de ", self.__anchoChasis, " y un largo de ", self.__largoChasis)

#     def __chequeo_interno(self):
#         print("realizando chequeo interno")

#         self.gasolina="ok"
#         self.aceite="ok"
#         self.puertas="cerradas"

#         if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):

#             return True

#         else:

#             return False


# miCoche = Coche()

# print(miCoche.arrancar(True))

# miCoche.estado()



# print("------- A continuación creamos el segundo objeto -------")

# miCoche2 = Coche()
# print(miCoche2.arrancar(False))

# miCoche2.estado()


#Aquí también podemos encapsular/blindar al método para que no podamos manipularlo desde afuera, 
# en capsulamos el método chequeo_interno y donde vayamos a usarlo también tiene que ser encapsulado 
# con __ y asi aunque pongamos un print que haga un chequeo interno, no podrá hacerlo ni poniendolo también __ ahi. 

#NOTA: Solo debes encapsular variables/métodos solo cuando tu objeto/clase asi lo necesite bajo tu criterio lógico 
# de como funciona tu código.


#PARTE 2

# PROYECTO ZENKAI DE SINERGIA: EL ESCUDO DEL BÚNKER (V28)
# INTEGRACIÓN: PYTHON (MÉTODOS PRIVADOS) + INGLÉS (LET) + JAPONÉS (CORTESÍA) + DUKE (BAYES)

class SistemaZenkai():
    def __init__(self):
        # Propiedades Encapsuladas (Blindaje de Rango SSS)
        self.__temp_clima = 18          # 十八 (Juu-hachi)
        self.__no_break_status = "OK"   # Evidence (Bayes)
        self.__is_safe = False

    # MÉTODO PÚBLICO (La interfaz que usamos)
    def arrancar_render(self, permission_granted):
        # Lógica de Pacho (LET): "Let me check the system first"
        if permission_granted:
            # LLAMADA AL MÉTODO PRIVADO (El corazón del video 28)
            chequeo = self.__chequeo_seguridad_interno()

            if permission_granted and chequeo:
                self.__is_safe = True
                return "SUCCESS: Let IT render. System is cold and protected."
            else:
                return "FAIL: Something is wrong. Don't let THEM start the GPU."
        else:
            return "ACCESS DENIED: No permission granted."

    # MÉTODO ENCAPSULADO (Blindado/Privado - Lo que aprendiste hoy)
    # Nadie puede llamar a este método desde fuera del búnker
    def __chequeo_seguridad_interno(self):
        print("\n[MÉTODO PRIVADO]: Ejecutando verificación de Bayes...")
        
        # Sinergia Duke: Evidencia de probabilidad de éxito
        self.voltaje = "estabilizado"
        self.limpieza_fans = "ok"

        if self.voltaje == "estabilizado" and self.limpieza_fans == "ok":
            return True
        else:
            return False

    # Método de Estado (Cortesía Japonesa L1-13)
    def o_ikutsu_status(self):
        # Preguntamos "¿Cuántos?" elementos están activos con respeto
        return f"O-ikutsu cores active? -> {8} cores. Temp: {self.__temp_clima}°C."

# --- EJECUCIÓN DEL SISTEMA ---
mi_bunker = SistemaZenkai()

# 1. Intentamos arrancar (LET + Encapsulamiento)
print(mi_bunker.arrancar_render(permission_granted=True))

# 2. Verificamos specs con respeto (Kira-sensei)
print(mi_bunker.o_ikutsu_status())

# 3. PRUEBA DE BLINDAJE (Intento de Hackeo del Día 13)
# Si intentas llamar al chequeo desde fuera, Python lanzará un Error (AttributeError)
# mi_bunker.__chequeo_seguridad_interno() <-- ESTO CAERÍA EN EL ESCUDO
