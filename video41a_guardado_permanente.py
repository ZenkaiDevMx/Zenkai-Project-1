#PILDORAS INFORMATICAS
#PYTHON
#VIDEO 41a
#GUARDADO PERMANENTE
#PARTE 1

#.Guardar datos de forma permanente en ficheros externos.

#EJEMPLO 1

# import pickle

# class Persona:

#     def __init__(self,nombre, genero, edad):
#         self.nombre=nombre
#         self.genero=genero
#         self.edad=edad
#         print("Se ha creado una persona nueva con el nombre de ", self. nombre)

#     def __str__(self):
#         return "{} {} {}".format(self.nombre, self.genero, self.edad)

# p=Persona("Sandra", "Femenino", 29)

#Primero importamos el módulo pickle para empaquetar objetos más tarde. Creamos la clase 
#Persona y su constructor (__init__) para definir nombre, género y edad. Luego, creamos el 
#método __str__ para presentar esa info en formato texto legible. Finalmente, creamos el 
#objeto p basado en la clase Persona, le asignamos los datos de Sandra y, al nacer, el 
#constructor imprime el mensaje de confirmación.


#EJEMPLO 2

# import pickle

# class Persona:

#     def __init__(self,nombre, genero, edad):
#         self.nombre=nombre
#         self.genero=genero
#         self.edad=edad
#         print("Se ha creado una persona nueva con el nombre de ", self. nombre)

#     def __str__(self):
#         return "{} {} {}".format(self.nombre, self.genero, self.edad)


# class ListaPersonas:

#     personas=[]

#     def agregarPersonas(self, p):
#         self.personas.append(p)

#     def mostrarPersonas(self):
#         for p in self.personas:
#             print(p)

# miLista=ListaPersonas()
# p=Persona("Sandra", "Femenino", 29)
# miLista.agregarPersonas(p)
# p=Persona("Antonio", "Masculino", 39)
# miLista.agregarPersonas(p)
# p=Persona("Ana", "Femenino", 19)
# miLista.agregarPersonas(p)

# miLista.mostrarPersonas()


#Aquí lo que hicimos fue crear una segunda clase llamada ListaPersonas, que funciona como un 
#archivador para meter a todas las personas que vamos creando. Primero definimos una lista 
#vacía llamada personas donde se van a ir guardando los objetos. Luego creamos el método 
#agregarPersonas para meter a cada persona al archivador y el método mostrarPersonas que usa 
#un ciclo for para leer la ficha (el __str__) de cada uno de un solo tirón. Al final, creamos 
#nuestra lista miLista, le metimos a Sandra, Antonio y Ana, y con una sola orden imprimimos 
#toda la base de datos.

#EJEMPLO 3


# import pickle

# class Persona:

#     def __init__(self,nombre, genero, edad):
#         self.nombre=nombre
#         self.genero=genero
#         self.edad=edad
#         print("Se ha creado una persona nueva con el nombre de ", self. nombre)

#     def __str__(self):
#         return "{} {} {}".format(self.nombre, self.genero, self.edad)


# class ListaPersonas:

#     personas=[]

#     def __init__(self):

#         listaDePersonas=open(r"E:\Descargas\ESTUDIO\PROGRAMACION\MODULOS\ficheroExterno", "ab+") 
#         listaDePersonas.seek(0)

#         try:
#             self.personas=pickle.load(listaDePersonas)
#             print("Se cargaron {} personas del fichero externo".format(len(self.personas)))

#         except:
#             print("El fichero esta vacío")

#         finally:
#             listaDePersonas.close()
#             del(listaDePersonas)


#     def agregarPersonas(self, p):
#         self.personas.append(p)

#     def mostrarPersonas(self):
#         for p in self.personas:
#             print(p)


# miLista=ListaPersonas()

#En esta parte lo que hicimos fue darle memoria automática al archivador. Dentro de la clase 
#ListaPersonas creamos su propio constructor __init__ para que, en cuanto arranquemos el programa, 
#se vaya directo a buscar el archivo físico en la carpeta de la compu. Usamos open con el permiso 
#ab+ para poder leer y escribir, y con seek(0) le decimos que empiece a revisar desde la primera 
#línea.Luego metimos un sistema de seguridad: con try intentamos desempaquetar (load) a las personas 
#que ya estaban guardadas en el disco duro para meterlas a la lista actual; si el archivo está nuevo 
#y no encuentra nada, el except evita que el programa truene y mejor nos avisa que 'el fichero está 
#vacío'. Finalmente, con finally nos aseguramos de cerrar la caja del archivo para que no se 
#corrompa la info. Así, al final, cuando creamos miLista, el programa ya sabe solito si tiene gente 
#guardada o si empieza de cero.


#EJEMPLO 4

# import pickle

# class Persona:

#     def __init__(self,nombre, genero, edad):
#         self.nombre=nombre
#         self.genero=genero
#         self.edad=edad
#         print("Se ha creado una persona nueva con el nombre de ", self. nombre)

#     def __str__(self):
#         return "{} {} {}".format(self.nombre, self.genero, self.edad)


# class ListaPersonas:

#     personas=[]

#     def __init__(self):

#         listaDePersonas=open(r"E:\Descargas\ESTUDIO\PROGRAMACION\MODULOS\ficheroExterno", "ab+") 
#         listaDePersonas.seek(0)

#         try:
#             self.personas=pickle.load(listaDePersonas)
#             print("Se cargaron {} personas del fichero externo".format(len(self.personas)))

#         except:
#             print("El fichero esta vacío")

#         finally:
#             listaDePersonas.close()
#             del(listaDePersonas)


#     def agregarPersonas(self, p):
#         self.personas.append(p)
#         self.guardarPersonasEnFicheroExterno()
#     def mostrarPersonas(self):
#         for p in self.personas:
#             print(p)

#     def guardarPersonasEnFicheroExterno(self):
#         listaDePersonas=open(r"E:\Descargas\ESTUDIO\PROGRAMACION\MODULOS\ficheroExterno", "wb")
#         pickle.dump(self.personas, listaDePersonas)
#         listaDePersonas.close()
#         del(listaDePersonas)

# miLista=ListaPersonas()
# persona=Persona("Sandra", "Femenino", 29)
# miLista.agregarPersonas(persona)

#Lo que hicimos aquí fue crear el botón de auto-guardado definitivo. Creamos un nuevo método llamado 
#guardarPersonasEnFicheroExterno que se encarga de abrir nuestro archivo en modo wb para escribir 
#desde cero la lista actualizada. Dentro usamos pickle.dump para empaquetar y congelar toda nuestra 
#lista de personas directamente en el disco duro. Lo mejor es que conectamos este método dentro de 
#agregarPersonas, así que ahora, en cuanto creamos a Sandra y la metemos al archivador, el programa 
#automáticamente la guarda en la memoria permanente. Ya no tenemos que preocuparnos por darle a 
#'guardar', el código lo hace solo cada vez que registramos a alguien nuevo.

#EJEMPLO 5

# import pickle

# class Persona:

#     def __init__(self, nombre, genero, edad):
#         self.nombre = nombre
#         self.genero = genero
#         self.edad = edad
#         print("Se ha creado una persona nueva con el nombre de ", self.nombre)

#     def __str__(self):
#         return "{} {} {}".format(self.nombre, self.genero, self.edad)


# class ListaPersonas:

#     personas = []

#     def __init__(self):
#         # Abrimos el archivo en modo lectura/escritura binaria
#         listaDePersonas = open(r"E:\Descargas\ESTUDIO\PROGRAMACION\MODULOS\ficheroExterno", "ab+") 
#         listaDePersonas.seek(0)

#         try:
#             self.personas = pickle.load(listaDePersonas)
#             print("Se cargaron {} personas del fichero externo".format(len(self.personas)))
#         except:
#             print("El fichero esta vacío")
#         finally:
#             listaDePersonas.close()
#             del(listaDePersonas)

#     def agregarPersonas(self, p):
#         self.personas.append(p)
#         self.guardarPersonasEnFicheroExterno()

#     def mostrarPersonas(self):
#         for p in self.personas:
#             print(p)

#     def guardarPersonasEnFicheroExterno(self):
#         listaDePersonas = open(r"E:\Descargas\ESTUDIO\PROGRAMACION\MODULOS\ficheroExterno", "wb")
#         pickle.dump(self.personas, listaDePersonas)
#         listaDePersonas.close()
#         del(listaDePersonas)

#     def mostrarInfoFicheroExterno(self):
#         print("La información del fichero externo es la siguiente:")
#         for p in self.personas:
#             print(p) 

# # --- PRUEBA DE LA BASE DE DATOS ---

# miLista = ListaPersonas()

# # Aquí puedes ir cambiando los datos para registrar a más personas:
# persona = Persona("Sandra", "Femenino", 29)
# miLista.agregarPersonas(persona)

# miLista.mostrarInfoFicheroExterno()

#Con esta última parte terminamos de armar nuestro sistema de Base de Datos. Creamos el método 
#mostrarInfoFicheroExterno, que es como pedirle al archivador que nos dé un reporte completo y 
#ordenado de toda la información que tiene guardada en el disco duro. Lo mejor es que este sistema 
#es acumulativo: cada vez que cambiamos los datos en las últimas líneas (por ejemplo, ponemos a 
#'Juan', 'Masculino', '40') y corremos el código, el programa crea la nueva persona, la empaqueta y 
#la suma a la lista que ya existía. Así, poco a poco, vamos llenando nuestro archivo físico con una 
#lista de contactos real que no se borra nunca.

#NOTA: Para ir alimentando la base de datos, solo tienes que cambiar los datos de la última parte 
#del código:

#persona = Persona("Nombre Nuevo", "Género", Edad)
#miLista.agregarPersonas(persona)
#Cada vez que le des al "Play", se agregará una nueva ficha de datos (contactos).

#PARTE 2

# ==========================================================
# PROYECTO SINERGIA ZENKAI: LOGÍSTICA DE INMERSIÓN 4K
# ==========================================================

# 1. Definimos la Clase de Cacería (ADN del Juego)
import pickle

class CaceriaGamer:
    def __init__(self, juego, frase_jap, frase_ing, particula):
        self.juego = juego
        self.frase_jap = frase_jap
        self.frase_ing = frase_ing
        self.particula = particula
        print(f"🧬 ADN extraído de {self.juego}: '{self.frase_jap}'")

    def __str__(self):
        # Formato Rango SSS para la terminal
        return f"🎮 [{self.juego}] JAP: {self.frase_jap} | ENG: {self.frase_ing} | Partícula: {self.particula}"

# 2. Definimos el Archivador Permanente (Soberanía del Disco 2TB)
class RegistroBunker:
    lista_caceria = []

    def __init__(self):
        # Usamos la ruta absoluta de MODULOS
        ruta_archivo = r"E:\Descargas\ESTUDIO\PROGRAMACION\MODULOS\bitacora_gamer"
        
        # ab+ permite leer y agregar sin borrar el pasado (Persistencia)
        fichero_externo = open(ruta_archivo, "ab+")
        fichero_externo.seek(0)

        try:
            self.lista_caceria = pickle.load(fichero_externo)
            print(f"✅ Búnker conectado: {len(self.lista_caceria)} registros recuperados.")
        except:
            print("🌑 Registro nuevo. El búnker está listo para la primera cacería.")
        finally:
            fichero_externo.close()
            del(fichero_externo)

    def guardar_progreso(self, c):
        self.lista_caceria.append(c)
        self.volcar_a_disco()

    def volcar_a_disco(self):
        ruta_archivo = r"E:\Descargas\ESTUDIO\PROGRAMACION\MODULOS\bitacora_gamer"
        fichero = open(ruta_archivo, "wb") # Escritura binaria pura
        pickle.dump(self.lista_caceria, fichero)
        fichero.close()
        del(fichero)

    def mostrar_historial(self):
        print("\n📜 --- REPORTE DE INMERSIÓN GAMER ---")
        for registro in self.lista_caceria:
            print(registro)

# --- EJECUCIÓN DEL PROYECTO ---

# Iniciamos el sistema (busca datos viejos automáticamente)
mi_bitacora = RegistroBunker()

# PARA REGISTRAR NUEVOS DATOS: Solo cambia estas líneas y dale a 'Play'
# nueva_frase = CaceriaGamer("Spider-Man (SR)", "君を助ける (Kimi o tasukeru)", "I will save you", "を (o)")
# mi_bitacora.guardar_progreso(nueva_frase)

# Mostramos todo lo que hay en el disco de 2TB
mi_bitacora.mostrar_historial()
