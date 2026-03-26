#EJEMPLO 1

# import video34_modulos

# video34_modulos.sumar(7,5)
# video34_modulos.restar(7,5)

#Aquí estamos haciendo funciones operaciones aritmeticas de suma, 
# resta, multiplicación y creando un modulo con la función import de esas funciones

#EJEMPLO 2

# from video34_modulos import sumar

# sumar(7,5)
# restar(9,5)
# multiplicar(5,6)

#Aquí si usamos la función from y import especificando solo la suma, 
# solo la operación con suma lo podrá hacer bien y las demás no.

#EJEMPLO 3

# from video34_modulos import *

# sumar(7,5)
# restar(9,5)
# multiplicar(5,6)

#Aquí al cambiar la operación especifica por el *, le estamos diciendo 
# que engoble todas las operaciones aritméticas y nos podrá hacer la operación.

#NOTA: Aunque es una gran ventaja hacerlo asi, si el código es muy grande y si 
# solo estamos usando una operación en ese bloque, es mejor especificar la operación 
# para optimizar y gastar menos recursos (memoria) en la ejecución.

#EJEMPLO 4

# from video34_modulos import *

# miCoche=Vehiculos("Mazda", "MX5")

# miCoche.estado()

#Aquí reutilizando parte del código de herencia, creamos una instancia de miCoche=Vehiculos y le pasamos al constructor de vehículos una marca y un modelo.

#NOTA: siempre el archivo principal y donde queremos hacer el modulo debe estar en una misma carpeta, para arreglar esto podemos usar un paquete que nos sirve para que no importe donde este.

