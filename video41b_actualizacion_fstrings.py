#PILDORAS INFORMATICAS
#PYTHON
#VIDEO 41b
#ACTUALIZACION: USO DE F-STRINGS

#PARTE 1

#EJEMPLO 1

# import pickle

# class Persona:

#     def __init__(self, nombre, genero, edad):
#         self.nombre = nombre
#         self.genero = genero
#         self.edad = edad
#         # Actualizado a f-string: Más limpio y directo
#         print(f"Se ha creado una persona nueva con el nombre de {self.nombre}")

#     def __str__(self):
        
#         return f"{self.nombre} {self.genero} {self.edad}"

# class ListaPersonas:

#     personas = []

#     def __init__(self):
        
#         ruta = r"E:\Descargas\ESTUDIO\PROGRAMACION\MODULOS\ficheroExterno"
#         listaDePersonas = open(ruta, "ab+") 
#         listaDePersonas.seek(0)

#         try:
#             self.personas = pickle.load(listaDePersonas)
#             # Actualizado a f-string: Metemos la lógica de len() directo en las llaves
#             print(f"Se cargaron {len(self.personas)} personas del fichero externo")
#         except:
#             print("El fichero está vacío")
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


# miLista = ListaPersonas()

# # Creamos a Sandra (o a cualquier "misionero de datos" que quieras)
# persona = Persona("Sandra", "Femenino", 29)
# miLista.agregarPersonas(persona)

# miLista.mostrarInfoFicheroExterno()

#En esta actualización del sistema, sustituimos el antiguo método .format() por las f-strings (f"..."), 
# que son el estándar moderno de Python para el manejo de cadenas. Al escribir el prefijo f antes de las comillas, 
# permitimos que las variables de la clase, como {self.nombre} o {self.edad}, se inserten directamente dentro del texto 
# sin necesidad de dejar espacios vacíos ni usar funciones externas al final de la línea. Esto hace que el método __str__ 
# y los mensajes de confirmación sean mucho más fáciles de leer y procesar para el sistema. Es una mejora de limpieza de 
# código que optimiza la visualización de los datos cuando pedimos un reporte del fichero externo, asegurando que la 
# información que se extrae del empaquetado de pickle se presente de forma directa y moderna en la terminal.




#PROYECTO SINERGIA ZENKAI: BITÁCORA GAMER 4K (REFACTOR f-string)

import pickle

# 1. Definimos la Clase de Cacería (ADN del Juego con f-strings)
class CaceriaGamer:
    def __init__(self, juego, frase_jap, frase_ing, particula):
        self.juego = juego
        self.frase_jap = frase_jap
        self.frase_ing = frase_ing
        self.particula = particula
        # Refactor f-string: Mensaje de nacimiento más directo
        print(f"🧬 ADN extraído de {self.juego}: '{self.frase_jap}'")

    def __str__(self):
        # Refactor f-string: Limpieza absoluta en el reporte de la terminal
        return f"🎮 [{self.juego}] JAP: {self.frase_jap} | ENG: {self.frase_ing} | Partícula: {self.particula}"

# 2. Definimos el Archivador Permanente (Soberanía del Disco 2TB)
class RegistroBunker:
    lista_caceria = []

    def __init__(self):
        ruta_archivo = r"E:\Descargas\ESTUDIO\PROGRAMACION\MODULOS\bitacora_gamer"
        fichero_externo = open(ruta_archivo, "ab+")
        fichero_externo.seek(0)

        try:
            self.lista_caceria = pickle.load(fichero_externo)
            # Refactor f-string: Conteo de registros en tiempo real
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
        fichero = open(ruta_archivo, "wb")
        pickle.dump(self.lista_caceria, fichero)
        fichero.close()
        del(fichero)

    def mostrar_historial(self):
        print("\n --- REPORTE DE INMERSIÓN GAMER (REFACTOR f-string) ---")
        for registro in self.lista_caceria:
            print(registro)

# --- EJECUCIÓN DEL PROYECTO ACTUALIZADO ---

mi_bitacora = RegistroBunker()

# PARA REGISTRAR NUEVOS DATOS 
# nueva_frase = CaceriaGamer("おはよう (Ohayou)", "Good morning", "は (wa)")
# mi_bitacora.guardar_progreso(nueva_frase)

mi_bitacora.mostrar_historial()