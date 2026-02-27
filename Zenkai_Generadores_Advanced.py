#DIA 16 VIDEO 20
#GENERADORES 2
#PARTE 1

#GENERADORES

#.Nueva instrucciones Yield from

#Utilidad: Simplificar el código de los generadores en el caso de utilizar bucles anidados (como en un bucle for dentro de otro)

#SINTAXIS

#Def miGenerador():
  # Yield elementos

#FUNCIONAMIENTO

#EL bucle for principal accede a los elementos del generador mientras que el bucle for anidado que es parte del bucle for principial estuviera accediendo a los subelementos que a su vez es parte de unos de los elementos que nos devuelve el generador.


#EJEMPLO 1

# def devuelve_ciudades(*ciudades):
#     for elemento in ciudades:
#         yield elemento

# ciudades_devueltas=devuelve_ciudades("Madrid", "Barcelona", "Bilbao", "Valencia")

# print(next(ciudades_devueltas))

# print(next(ciudades_devueltas))



#Le estamos diciendo al programa que la función con * quede guardado 
# en la variable devuelve_ciudades y pasa por un bucle for y el generador elemento,
#  por medio de la variable ciudades_devueltas que hacemos igual a devuelve_ciudad le 
# damos 4 nombres de ciudad y al final por una función next dos veces, le estamos diciendo 
# que haga dos vueltas de validación y de regreso de código y en cada vuelta y regreso conserve energía 
# y vuelva a repetir el proceso, para al final mostrar dos ciudades nada mas.


#NOTA: al ponerle un * delante del argumento de una función, le estamos diciendo que va recibir un 
# numero indeterminado de elementos además que esos argumentos los va recibir en forma de tupla.

#EJEMPLO 2 (bucle for anidado)

# def devuelve_ciudades(*ciudades):
#     for elemento in ciudades:
#         for subElemento in elemento:
#             yield subElemento

# ciudades_devueltas=devuelve_ciudades("Madrid", "Barcelona", "Bilbao", "Valencia")

# print(next(ciudades_devueltas))

# print(next(ciudades_devueltas))


#Ahora le estamos diciendo que dentro de las dos palabras de ciudades 
# que devuelve ahora acceda a sus subelementos que en este caso son las letras, 
# pero solo devolverá las dos primeras letras de la primera palabra o sea M y a, 
# ya que solo devuelve los dos primeros subelementos del primer elemento.

#EJEMPLO 3

# def devuelve_ciudades(*ciudades):
#     for elemento in ciudades:
#              yield from elemento

# ciudades_devueltas=devuelve_ciudades("Madrid", "Barcelona", "Bilbao", "Valencia")

# print(next(ciudades_devueltas))

# print(next(ciudades_devueltas))

#Aquí le quitamos el bucle for anidado y mejor usamos la instrucciones yield from 
# para simplificar código y mejorar la eficiencia, haciendo que por defecto que digamos 
# que acceda a los 2 primeros subelementos del primer elemento en este caso M y a.

"""
PARTE 2

PROYECTO ZENKAI OJO DE LUNA: SINERGIA TOTAL V2 (VIERNES DE VICTORIA)
-----------------------------------------------------------
- Inglés (Pacho): Adverbios '-ly' para describir el proceso.
- Japonés (Kira): Q&A binario (Hai/Iie) para validación de hardware.
- Duke (Math): Lógica de Funciones Crecientes vs Inversas.
- Python: 'yield from' para extraer sub-metadatos de frames.
"""

def analyze_gto_metadata(episode_data):
    # 'yield from' accede directamente a los subelementos (frames) del episodio
    yield from episode_data

def render_engine():
    # Datos de entrada: Frames de GTO (subelementos de la ciudad Akihabara de datos)
    frames_gto = ["Frame_01_Low", "Frame_02_Mid", "Frame_03_High"]
    
    # 1. INGLÉS (Adverbios): The AI works PERFECTLY.
    print("--- STARTING SYSTEM: The AI processes accurately ---")
    
    # 2. JAPONÉS (Q&A): Anata wa enjinia desu ka? Hai!
    print("Q: あなた は エンジニア です か。 (Are you an engineer?)")
    print("A: はい、 わたし は エンジニア です。 (Yes, I am.)")

    # 3. PYTHON (Yield from): Extrayendo datos sin bucles anidados
    scanner = analyze_gto_metadata(frames_gto)
    
    # 4. DUKE (Lógica de Funciones):
    # Si la calidad sube de Low a High, es CRECIENTE.
    # Si queremos volver al original, aplicamos la INVERSA (f^-1).
    
    f1 = next(scanner)
    print(f"Loot 1: {f1} | Status: Constant Ki.")
    
    f2 = next(scanner)
    print(f"Loot 2: {f2} | Status: Increasing Quality (Duke Logic).")
    
    f3 = next(scanner)
    print(f"Loot 3: {f3} | Status: Perfectly Rendered (Pacho Logic).")
    
    print("\n--- MISSION COMPLETE: Inversa applied to return to original state ---")

# --- EJECUCIÓN ---
render_engine()
