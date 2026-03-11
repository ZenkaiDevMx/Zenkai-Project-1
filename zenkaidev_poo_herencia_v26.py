#PILDORAS INFORMATICAS
#PYTHON
#VIDEO 26
#POO 3
#PARTE 1

#Trasladar a código los conceptos teóricos que hemos visto anteriormente.

#EJEMPLO 1

#.Clase: estado, propiedades, comportamiento

#.Comportamiento se determina por un método

#.Para crear un método usamos la palabra reserva def y 
# desplegara en forma de función o en método (defs) y 
# un método es una función especial que pertenece a la 
# clase que se esta creando. 

# class Coche():
#    largoChasis=250
#    anchoChasis=120
#    ruedas=4
#    enmarcha=False

#    def arrancar(self):
#        pass

# miCoche=Coche()

# print("El largo del coche es: ",miCoche.largoChasis)


#Aquí lo que estamos haciendo es asignar una clase poniendo de nombre Coche y dándole las propiedad de larcho, 
# ancho, ruedas, enmarca, despus utilizamos el método def, usando la nomenclatura def, function que se puede cambiar 
# el nombre a lo que tu quieras, en este caso arrancar y self que significa el tipo de clase con la que estas trabajando, 
# sirve como una etiqueta por si existiera mas clases, en este caso es la clase coche, luego creamos nuestro primer objeto 
# miCoche=Coche luego imprimimos el nombre del objeto y la nomenclatura del punto y la propiedad que queremos en este caso largoChasis



#Nota: miCoche=Coche se le llama instanciar una clase

#EJEMPLO 2

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

#Aquí ponemos el nombre de la propiedad a enmarcha pero antes self que es el 
# nombre por defecto de la clase que estamos usando en este caso Coche, y 
# le decimos que este en True, abajo después del print ponemos el objeto.arrancar 
# diciendole que nuestro objeto miCoche se almacene en self y luego ponemos otro método 
# llamado estado y ponemos si es es verda que arranca es true y si no con un else que nos 
# imprima que esta parado, al final que imprima el estado de mi objeto miCoche.

#EJEMPLO 3

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
# #miCoche.arrancar()

# print(miCoche.estado())


#En el ejemplo anterior mi objeto miCoche estaba en marcha es porque antes de preguntarle 
# cual era su estado, lo hemos arrancando en miCoche.arrancar() pero si omitimos esa linea, al mandar 
# la información a self y no dar True se salta el if y nos imprime el else de el coche esta parado.

#Anotaciones:

#Nuestra clase Coche tiene 4 propiedades, tiene 2 comportamientos.

#PARTE 2

# PROYECTO ZENKAI DE SINERGIA: SEMANA 5 - MIÉRCOLES
# BLOQUES: PYTHON (POO) + INGLÉS (SHOULD) + JAPONÉS (NÚMEROS) + DUKE (PROBABILIDAD)

class GundamBunker:
    # --- PROPIEDADES (Japonés L1-11: Números) ---
    ryzen_cores = 8       # 八 (Hachi)
    rtx_vram = 16         # 十六 (Juu-roku)
    clima_temp = 18       # 十八 (Juu-hachi) grados
    
    # --- ESTADO INICIAL (Python POO: Atributos) ---
    is_overclock_active = False
    system_health = "Stable"

    # --- COMPORTAMIENTO (Inglés L27: Should / Duke: Probabilidad Condicional) ---
    def optimize_system(self, ambient_temp):
        # Lógica de Probabilidad Condicional: 
        # P(Fallo | Temp > 25) = Alta. Por eso usamos SHOULD.
        if ambient_temp > 25:
            self.is_overclock_active = False
            return "WARNING: Ambient too hot! You SHOULD NOT overclock."
        else:
            self.is_overclock_active = True
            self.clima_temp = 18 # Forzamos enfriamiento
            return "STATUS: Cold environment. You SHOULD enable Turbo Mode."

    # --- MÉTODO DE ESTADO (Self: La etiqueta de identidad) ---
    def get_specs(self):
        # Usamos self para acceder a las propiedades de ESTE búnker específico
        status = "ACTIVE" if self.is_overclock_active else "IDLE"
        return f"Gundam Specs: {self.ryzen_cores} Cores & {self.rtx_vram}GB VRAM. Mode: {status}"

# --- INSTANCIACIÓN (Crear el objeto real) ---
mi_gundam = GundamBunker()

# 1. Ejecutamos lógica de Pacho y Duke (Should + Condicional)
# Probamos con el calor de Campeche (35°C)
print(mi_gundam.optimize_system(ambient_temp=35))

# 2. Consultamos especificaciones usando self
print(mi_gundam.get_specs())

# 3. Anclaje de Serorinne (Japonés Tech)
print("Kore wa sugoi hardware desu! (Esto es hardware increíble)")
