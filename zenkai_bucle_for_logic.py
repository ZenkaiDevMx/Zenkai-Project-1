#VIDEO 14 PILDORAS INFORMATICAS
#BUCLES DETERMINADOS
#PARTE 1

#La variable puede ser cualquier nombre, 
# pero por convención se usa la letra i, 
# en el bucle for.

#EJEMPLO 1:

# for i in [1,2,3]:
#     print("Hola")


#Este bucle determinado va imprimir 3 veces Hola, 
# porque usa 3 elementos (1,2,3), en la declaración del bucle.

#EJEMPLO 2:

# for i in ["primavera","verano","otoño","invierno"]:
#     print("Hola")


#Este bucle determinado va imprimir 4 veces Hola, 
#porque usa  elementos, en la declaración del bucle,
#no importa si son números o palabras, 
#lo que importa es el numero de elementos.

#EJEMPLO 3:

# for i in ["primavera","verano","otoño","invierno"]:
#     print(i)

#Le estamos diciendo que i es igual a cada uno de los elementos, 
# por lo cual imprimirá cada uno de ellos de izquierda a derecha.

#PARTE 2

# --- PROYECTO ZENKAI DE SINERGIA: HARDWARE + LOGIC + FOR ---

# List of hardware components with their operating temperatures (Celsius)
# La lista contiene tuplas: (Nombre del componente, Temperatura)
hardware_inventory = [("CPU", 65), ("GPU", 82), ("RAM", 45), ("SSD", 35)]

print("Checking system status...")

# Logic: We only want to alert if temperature is GREATER THAN 70 (Duke's Inequality)
# The developer loops through the list (3ra persona - Inglés)

for component, temp in hardware_inventory:
    if temp > 70:
        # The system SHOWS an alert (3ra persona - Inglés)
        print(f"ALERT: {component} is too hot! It is {temp} degrees.")
    else:
        # The system RUNS normally (3ra persona - Inglés)
        print(f"Status: {component} is stable at {temp} degrees.")

print("Analysis complete.")

#En este proyecto, estamos creando el bucle for desde una lista de tuplas, 
# usando piezas de hardware, creando 4 parejas de elementos 
# y le asignamos al for dos variables component y temp, 
# el bucle se va ejercer 4 veces al medir estos valores, 
# si la temperatura supera los 70 grados Celsius, 
# imprimirá is too hot! It is y si no es asi, 
# se saltara la instrucción if y se ira directo al else imprimiendo is stable at, 
# despues que termine de medir las 4 parejas de elementos imprimirá "Analysis complete y finalizara el programa.
