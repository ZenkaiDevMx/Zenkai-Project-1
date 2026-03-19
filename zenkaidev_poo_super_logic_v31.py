# PILDORAS INFORMATICAS
# PYTHON
# VIDEO 31
# POO 8 HERENCIA 3
# PARTE 1

# HERENCIA 3 SUPER

# EJEMPLO 1

# class Persona:
#     def __init__(self, nombre, edad, lugar_residencia):
#         self.nombre = nombre
#         self.edad = edad
#         self.lugar_residencia = lugar_residencia

#     def descripción(self):
#         print("Nombre: ", self.nombre, "Edad: ", self.edad, "Residencia: ", self.lugar_residencia)

# class Empleado(Persona):
#     def __init__(self, salario, antigüedad):
#         # Inyección de ADN: super() activa el constructor del padre Persona
#         super().__init__("Antonio", 55, "España")
#         self.salario = salario
#         self.antiguedad = antigüedad

# Antonio = Empleado(1500, 15)
# Antonio.descripción()

# Aquí en el objeto Empleado metemos una instrucción super para que pueda ejecutar el método init de la clase padre Persona para hacer una sincronia para que se almacene en nombre, edad y lugar residencia y seguirá con el flujo del constructor normal, y imprimirá los valores correspondientes.
# NOTA: se usa la instrucción super para que los objetos que quieras que hereden la clase padre puedan usar sus atributos sin restricción. 

# EJEMPLO 2

# class Persona:
#     def __init__(self, nombre, edad, lugar_residencia):
#         self.nombre = nombre
#         self.edad = edad
#         self.lugar_residencia = lugar_residencia

#     def descripción(self):
#         print("Nombre: ", self.nombre, "Edad: ", self.edad, "Residencia: ", self.lugar_residencia)

# class Empleado(Persona):
#     def __init__(self, salario, antigüedad, nombre_empleado, edad_empleado, residencia_empleado):
#         # Sincronía dinámica: super() pasa las variables al padre
#         super().__init__(nombre_empleado, edad_empleado, residencia_empleado)
#         self.salario = salario
#         self.antiguedad = antigüedad

#     def descripción(self):
#         # Reutilización: super() ejecuta el método del padre y luego suma el del hijo
#         super().descripción()
#         print(" Salario: ", self.salario, "Antigüedad: ", self.antiguedad)

# Manuel = Empleado(1500, 15, "Manuel", 55, "Colombia")
# Manuel.descripción()

# Aqui en llamada del constructor de la clase padre aplicada en el objeto Manuel de tipo Empleado le va pasar 5 parametros y 3 de esos 5 por medio de la instruccion super se activaría, además cuando llamamos a la descripción, el método def descripción se activa, luego lee la instrucción super descripción y va al método de la clase padre def descripción y ejecuta en su totalidad y luego imprime salario etc.
# NOTA: Al usar super nos ahorramos en el constructor padre repetir la linea de código de todas las variables (nombre, edad, etc).

# EJEMPLO 3

# class Persona:
#     def __init__(self, nombre, edad, lugar_residencia):
#         self.nombre = nombre
#         self.edad = edad
#         self.lugar_residencia = lugar_residencia

#     def descripción(self):
#         print("Nombre: ", self.nombre, "Edad: ", self.edad, "Residencia: ", self.lugar_residencia)

# class Empleado(Persona):
#     def __init__(self, salario, antigüedad, nombre_empleado, edad_empleado, residencia_empleado):
#         super().__init__(nombre_empleado, edad_empleado, residencia_empleado)
#         self.salario = salario
#         self.antiguedad = antigüedad

#     def descripción(self):
#         super().descripción()
#         print(" Salario: ", self.salario, "Antigüedad: ", self.antiguedad)

# Manuel = Empleado(1500, 15, "Manuel", 55, "Colombia")
# print(isinstance(Manuel, Empleado))

# Aquí estamos verificando con la función isinstance si el objeto Manuel de tipo empleado y efectivamente lo es porque se lo estamos indicando.
# NOTA: Principio de sustitución significa que es siempre un/a depende del caso, cuando tenemos herencia, un objeto de la subclase siempre será un objeto de la clase padre y al revés no siempre es. 
# NOTA 2: La función isinstance devuelve True si es cierto que devuelve una clase en concentro y devuelve False si no lo es.

# EJEMPLO 4

# class Persona:
#     def __init__(self, nombre, edad, lugar_residencia):
#         self.nombre = nombre
#         self.edad = edad
#         self.lugar_residencia = lugar_residencia

#     def descripción(self):
#         print("Nombre: ", self.nombre, "Edad: ", self.edad, "Residencia: ", self.lugar_residencia)

# class Empleado(Persona):
#     def __init__(self, salario, antigüedad, nombre_empleado, edad_empleado, residencia_empleado):
#         super().__init__(nombre_empleado, edad_empleado, residencia_empleado)
#         self.salario = salario
#         self.antiguedad = antigüedad

#     def descripción(self):
#         super().descripción()
#         print(" Salario: ", self.salario, "Antigüedad: ", self.antiguedad)

# Manuel_Persona = Persona("Manuel", 55, "Colombia")
# print(isinstance(Manuel_Persona, Empleado))

# Aquí estamos verificando con la función isinstance si el objeto Manuel es de la clase empleado siendo que le estamos indicando que es de tipo Persona nos dará False.

# EJEMPLO 5

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

# miMoto=Moto("Honda", "CBR")

# miMoto.caballito()

# miMoto.estado()

# miFurgoneta=Furgoneta("Renault", "Kangoo")

# miFurgoneta.arrancar()

# miFurgoneta.estado()

# print(miFurgoneta.carga(True))

# class BicicletaElectrica(VElectricos,Vehiculos):
 
#     pass

# miBici=BicicletaElectrica("Orbea", "Ihj")


# Aquí para que pueda imprimir marca y modelo de los atributos de marca y modelo de clase padre el objeto VElectricos le insertamos 
# un super con variables de marca y modelo y además también el constructor del objeto VEelectricos (def init), y al final de la instancia 
# BiclicletaElectrica le podemos poner una marca y un modelo en este caso Orbea y Ihj y no poner que el objeto VEelectricos herede la clase padre Vehiculos.

#PARTE 2

# PROYECTO ZENKAI SINERGIA: SEMANA 6 - JUEVES
# INTEGRACIÓN: SUPER() + LIAISON + KANJIS DE SISTEMA

class SistemaBase:
    def __init__(self, nombre_app, version):
        # Kanji: 情報 (Jhouhou - Información)
        self.nombre_app = nombre_app
        self.version = version
        self.status = "情報 (DATA) LOADED"

    def reporte(self):
        print(f"Sistema: {self.nombre_app} v{self.version} | Status: {self.status}")

class AutomatizadorMago(SistemaBase):
    def __init__(self, salario_meta, nombre_app, version):
        # INYECCIÓN DE ADN: super() conecta con el constructor del padre
        super().__init__(nombre_app, version)
        self.salario_meta = salario_meta
        # Kanji: 自動 (Jidou - Automático)
        self.modo = "自動 (AUTOMATIC) ACTIVE"

    def reporte(self):
        # Reutilizamos el reporte del padre y sumamos el nuestro
        super().reporte()
        # Sinergia Inglés: Liaison (_)
        print(f"I’ll_automate_this_task_now. Target: ${self.salario_meta} USD.")
        print(f"Current_Mode: {self.modo}")

# --- EJECUCIÓN EN EL MONITOR NUEVO 4K ---
# Creamos al Mago inyectando todos los parámetros
mi_meta = AutomatizadorMago(60000, "Zenkai_System", "1.3.1")

# Validamos la identidad (isinstance)
if isinstance(mi_meta, SistemaBase):
    print("Security_Check: Verified_as_Senior_Architect.")
    mi_meta.reporte()

