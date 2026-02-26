#VIDEO 19
#GENERADORES 1
#PARTE 1

#.GENERADORES

#.¿Que són?
#.Funcionamiento
#¿Qué utilidad tienen?
#¿Cuál es su sintaxis?

#GENERADORES ¿QUE SON?

#.Estructuras que extraen valores de una función 
# y se almacenan en objetos iterables (que se pueden recorrer), 
# en bucles while, for, iteradores, next.

#.Estos valores se almacenan de uno en uno.

#.Cada vez que un generador almacena un valor, 
# esta permanece en un estado pausado hasta que 
# se solicita el siguiente. Esta característica 
# conocida como "suspensión de estado" (standby).

#FUNCIONAMIENTO 

#Ejemplo si tiene que hacer una lista de números pares. 

#FUNCION "TRADICIONAL"

#Def generalNumero():
   # return números

  #  generaNumero()
   # (2 4 6 8 10)

#GENERADOR

#Def generalNumeros():
    #yield números

# 2----Objeto generador iterable

# generaNumeros()

#Intruccion yield: construye un objeto iterable 
# con el primer valor de esa lista de números pares, 
# la mayor diferencia, nos devuelve los valores en uno en uno 
# dentro de un objeto generador iterable.

#GENERADORES ¿QUE UTILIDAD TIENE?

#.Son mas eficientes que las funciones tradicionales 
# (menor tiempo, menos espacio, fácil para encontrar un elemento concreto de una lista)

#.Muy útiles con listas de valores infinitos

#.Bajo determinados escenarios, era muy útil que un generador 
# devuelva los valores de uno en uno.

#GENERADORES. SINTAXIS

#def generaNumeros():
   # yield números

#Nota: en lugar de return lleva yield pero también puede llevar un return



#EJEMPLO 1 (normal)

# def generaPares(limite): 

#     num=1

#     miLista=[]

#     while num<limite:

#         miLista.append(num*2)

#         num=num+1

#     return miLista

# print(generaPares(10))

#Aquí utilizamos la variable generaPares y usamos el argumento limite, 
# creo otra variable num=1 y una lista donde se van a guardar los números pares 
# que este completamente vacia [], luego uso un bucle while diciéndole mientras la variable 
# num sea menor que el limite de esta funcion de la variable generaPares debe hacer a milista 
# debe agregar el método append el valor de la variable num por 2, luego el valor de la variable 
# num se incrementa en +1 con el return va devolver lo que se haya guardado en mi lista y al final 
# imprimirá el resultado de generapares poniendo el limite hasta 10 pares.


#EJEMPLO 2 (Generador)

# def generaPares(limite):

#     num=1

#     while num<limite:

#         yield(num*2)

#         num=num+1

# devuelvePares=generaPares(10)

# for i in devuelvePares:

#     print(i)

#Aquí utilizamos la variable generaPares y usamos el argumento limite, 
# creo otra variable num=1, luego uso un bucle while diciéndole mientras 
# la variable num sea menor que el limite, utilizamos la instrucción yield 
# y nos devuelva este num por 2, luego el valor de la variable num se incrementa en +1, 
# crea una variable objeto donde se va almacenar llamado devuelvePares donde se va devolver 
# la función en generaPares delimitándolo a un máximo de 10 pares, al final pones un buble for 
# y introducimos el objeto interable llamado devuelvePares y va imprimir todo.

#EJEMPLO 3 (Generador)

# def generaPares(limite):

#     num=1

#     while num<limite:

#         yield(num*2)

#         num=num+1

# devuelvePares=generaPares(10)

# print(next(devuelvePares))

# print("Aquí podría ir mas código....")

# print(next(devuelvePares))

# print("Aquí podría ir mas código....")

# print(next(devuelvePares))

#aquí solo le estamos diciendo que imprima el primer valor que tiene almacenado en su interior 
# desde la variable generapares usando el método next, después puede ir mas código, y solo se 
# puso de ejemplo dos mas líneas y imprimirá los primeros 3 números pares, el control de flujo 
# pasa constantemente por la variable objeto generador devuelvePares a la linea de código imprimir 
# donde hubiera mas código y después cuando continua y se encuentra la instrucción next devuelve 
# otra vez a la variable objeto generador y vuelve otra vez al siguiente imprimir y asi hasta que termine, 
# si hubiera 300 líneas de código se leería primero antes esos y después se devolvería la información a la 
# variable objeto generador, entre cada vez que devuelve y devuelve entra en un estado llamado suspensión para ahorrar recursos.

#NOTA: Se puede también hacer del modo tradicional, pero no se ahorra mucho recursos así, sino eficiencia y tiempo al no tener que 
# asignarle todos los valores y solo decirle específicamente que quiere además de poder encontrarlos mas fácilmente.

#PARTE 2

# --- PROJECT ZENKAI OJO DE LUNA: SINERGIA TOTAL ---

#THE AKIHABARA RENDER ENGINE

# Objetivo: Generador de curva de calidad para GTO (1998).

# LOGICA DE INVASIÓN:
# - Inglés (Walter): Auxiliar 'does' para validar frames (Does it pass?).
# - Japonés (Serorinne): 'Kore' y 'No' para identificar objetos (Kore wa frame desu).
# - Duke (Math): Identificar funciones Crecientes y Decrecientes en la calidad.
# - Python: Uso de 'yield' para optimizar la RAM (Generador).


def render_gto_frames(total_frames):
    frame_id = 1
    calidad = 10  # Iniciamos con calidad base
    
    while frame_id <= total_frames:
        # Lógica de Duke: Función Creciente/Decreciente
        # Si el frame es par, la calidad sube (Creciente). Si es impar, baja (Decreciente).
        if frame_id % 2 == 0:
            calidad += 5
            estado = "CRECIENTE (Improving)"
        else:
            calidad -= 2
            estado = "DECRECIENTE (Dropping)"
            
        # Loot de Inglés y Japonés en los logs
        yield f"[FRAME {frame_id}] Kore wa GTO no frame desu. Quality: {calidad} | Status: {estado}"
        
        frame_id += 1

# --- EJECUCIÓN TÁCTICA ---
# Solo procesamos 5 para no saturar, pero el generador podría procesar 100,000
procesador = render_gto_frames(5)

print("--- STARTING AKIHABARA ENGINE ---")
print(next(procesador)) # Frame 1: Does it work? Yes!
print(next(procesador)) # Frame 2: Kore wa quality desu!
print(next(procesador)) # Frame 3: Standby mode...
print("--- PAUSE PARA AHORRAR KI (RAM) ---")
print(next(procesador))
print(next(procesador))
print("--- MISSION COMPLETE: OJO DE LUNA STATUS: RANGO S ---")

