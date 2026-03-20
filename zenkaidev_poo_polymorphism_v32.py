# PILDORAS INFORMATICAS
# PYTHON
# VIDEO 32
# POO 9 HERENCIA 4
# PARTE 1

# HERENCIA 4 POLIFORMISMO

#Un mismo objeto puede cambiar de forma, ejemplo un carro puede pasar una moto y sus características y atributos también cambian.

#EJEMPLO 1

# class Coche():

#     def desplazamiento(self):
#         print("Me desplazo utilizando cuatro ruedas")

# class Moto():

#     def desplazamiento(self):
#         print("Me desplazo utilizando dos ruedas")

# class Camion():

#     def desplazamiento(self):
#         print("Me desplazo utilizando seis ruedas")

# miVehiculo=Moto()

# miVehiculo.desplazamiento()

# miVehiculo2=Coche()

# miVehiculo2.desplazamiento()

# miVehiculo3=Camion()

# miVehiculo3.desplazamiento()

#Aquí tenemos tres instancias de objetos diferentes (Moto, Coche, Camion) 
# utilizando el método o comportamiento desplazamiento hacemos la llamada de cada uno de ellos.

#EJEMPLO 2

# class Coche():

#     def desplazamiento(self):
#         print("Me desplazo utilizando cuatro ruedas")

# class Moto():

#     def desplazamiento(self):
#         print("Me desplazo utilizando dos ruedas")

# class Camion():

#     def desplazamiento(self):
#         print("Me desplazo utilizando seis ruedas")

# def desplazamientoVehiculo(vehiculo):
#     vehiculo.desplazamiento()

# miVehiculo=Camion()
# desplazamientoVehiculo(miVehiculo)


#Aquí utilizamos una función llamada desplazamientoVehiculo 
# y recibe un objeto por parámetro llamado vehiculo y lo utilizara 
# para llamar al método desplazamiento, luego creamos un objeto de 
# tipo camión y utilizamos el método desplazamientoVehiculo y le 
# pasamos por parámetros el objeto miVehiculo y luego se almacena 
# dentro de vehiculo y se transforma en un objeto de tipo camión 
# y eso hace que llame al método de desplazamiento de tipo camión 
# y imprime que se desplaza a 6 ruedas.

#NOTA: En python no tenemos que especificar de ninguna forma, 
# es mas directo que en otros lenguajes de programación. 

#PARTE 2

# PROYECTO ZENKAI SINERGIA: SEMANA 6 - VIERNES
# INTEGRACIÓN: POLIMORFISMO + 7 VELOCIDADES + LIAISON

class Shadowing_Ingles():
    def ejecutar_entrenamiento(self):
        # Kanji: 英語 (Eigo - Inglés)
        # Sinergia Inglés: Liaison (_)
        print("Executing_Ingles_Session... Speed: 2.0x (Double_Meat) 🥩")
        print("Liaison_Check: I’ll_automate_it_now.")

class Shadowing_Japones():
    def ejecutar_entrenamiento(self):
        # Kanji: 日本語 (Nihongo - Japonés)
        print("Executing_Japones_Session... Speed: 1.75x (Zenkai_Bridge) ⛩️")
        print("Radar_Check: Katta! (勝った - We won!)")

# --- LÓGICA DE POLIMORFISMO (EL MAGO DE LOS DATOS) ---

def activar_modo_rafaga(idioma):
    """
    Esta función es POLIMÓRFICA. 
    No le importa qué idioma sea, ella solo 'dispara' el entrenamiento.
    """
    idioma.ejecutar_entrenamiento()

# --- EJECUCIÓN EN EL MONITOR 4K ---

# 1. El Mago elige su arma del día
sesion_hoy = Shadowing_Japones()

# 2. El Polimorfismo hace su magia: Trata a la sesión como un "objeto de entrenamiento"
print("--- STARTING_BUNKER_SESSION ---")
activar_modo_rafaga(sesion_hoy) 

# 3. Si mañana cambiamos a Inglés, la función activar_modo_rafaga sigue funcionando igual.
# Eso es SOBERANÍA de código.
