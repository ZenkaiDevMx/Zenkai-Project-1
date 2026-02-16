#DIA 7
#CONDICIONALES PARTE 3 (AND, OR, IN)
#PARTE 1 EJEMPLOS

#EJEMPLO 1

#CODIGO 1

# edad=7

# if 0<edad<100:
#      print("Edad es correcta")
# else:
#      print("Edad incorrecta")

#Si delimitamos 0 es menor que la variable edad (7) y es cierto, pasa a la siguiente instrucción (7 < 100). Como ambas se cumplen, marca 'Edad correcta.

#CODIGO 2

# edad=-7

# if 0<edad<100:
#      print("Edad es correcta")
# else:
#      print("Edad incorrecta")

#Por el contrario, con -7, Python evalúa de izquierda a derecha,
# ve que la primera condición es falsa (0 < -7), ignora el resto de la instrucción 
# y salta directo al else. Esto ahorra procesamiento.


#EJEMPLO 2

#CODIGO 1
 
# salario_presidente=int(input("Introduce salario presidente"))
# print ("Salario presidente:"+str(salario_presidente))

# salario_director=int(input("Introduce salario director"))
# print ("Salario director:"+str(salario_director))

# salario_jefe_area=int(input("Introduce Salario Jefe Area"))
# print ("Salario Jefe Area:"+str(salario_jefe_area))

# salario_administrativo=int(input("Introduce salario administrativo"))
# print ("Salario administrativo:"+str(salario_administrativo))

# if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
#   print("Todo funciona correctamente")
# else:
#   print("Algo falla en esta empresa")

#Aquí estamos diciendo que la variable salario presidente, 
# siempre debe ser el que gane mas e ir bajando de sueldo pasando por el director, 
# jefe de área y administrativo el salario mas bajo, y si todo va correcto, debe imprimir, 
# todo funciona correctamente, para este ejemplo pondremos que salario de presidente es 4000, 
# director 3000, jefe área 2000 y salario administrativo 1000.

#CODIGO 2
 
# salario_presidente=int(input("Introduce salario presidente"))
# print ("Salario presidente:"+str(salario_presidente))

# salario_director=int(input("Introduce salario director"))
# print ("Salario director:"+str(salario_director))

# salario_jefe_area=int(input("Introduce Salario Jefe Area"))
# print ("Salario Jefe Area:"+str(salario_jefe_area))

# salario_administrativo=int(input("Introduce salario administrativo"))
# print ("Salario administrativo:"+str(salario_administrativo))

# if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
#   print("Todo funciona correctamente")
# else:
#   print("Algo falla en esta empresa")

#Para este ejemplo pondremos que salario de presidente es 4000, director 3000, jefe área 3400 y administrativo 2000, como va ver un fallo en jefe área que gana mas que director debe imprimir algo falla en esta empresa, no importa si falla el primero o el segundo etc, siempre se va leer el código de izquierda a derecha y si falla va ignorar la siguientes instrucciones, las saltara e ira por else y imprimirá algo falla en esta impresa.

#PARTE 2 

# ZENKAI PROJECT: Hardware Validator
# Combinando Condicionales de Rango + Inglés Técnico de hoy

print("--- Welcome to Gawain System Check ---")

ram = int(input("How many gigabytes of RAM are in this PC? "))

if 0 < ram < 8:
    print("This is a Basic PC. Not enough for Data Science.")
elif 8 <= ram < 32:
    print("That is a Good PC. You can start your journey.")
elif 32 <= ram < 128:
    print(f"Those {ram} gigabytes are amazing! This is a Shogun PC.")
else:
    print("Something is wrong. Check your hardware.")

#Aplicando la clase del video 12 de juan, con lo que se vio de ingles, 
#evaluamos la ram, Si está entre 0 < RAM < 8: Imprime "This is a Basic PC".
#Si está entre 8 <= RAM < 32: Imprime "That is a Good PC".
#Si está entre 32 <= RAM < 128: Imprime "Those thirty-two gigabytes (or more) are for a Shogun. This is a Beast!".
#y si no es asi salta al Else y Imprime "Something is wrong with this hardware".
#Todo esto va evaluar desde 0 a 128.