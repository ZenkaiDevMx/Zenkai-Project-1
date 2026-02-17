#CONDICIONALES PARTE 4
#OPERADORES AND, OR, IN
#PARTE 1

#EJEMPLO 1


#El programa va evaluar la distancia mayor a 40km, 
# numero de hermanos mayor a 2 y el salario familiar menor o igual a 20k, 
# aplicamos el operador and que fuerza desde if, que debe cumplir todas las instrucciones, 
# si una no se cumple, saltara y se ira directo al else y imprimirá No tienes derecho a beca.

#EJEMPLO 2

# print("Programa de becas Año 2026")
# distancia_escuela=int(input("Introduce la distancia a la escuela en km"))

# numero_hermanos=int(input("Introduce el n° de hermanos en el centro"))
# print(numero_hermanos)

# salario_familiar=int(input("Introduce salario anual bruto"))
# print(salario_familiar)

# if distancia_escuela>40 and numero_hermanos>2 or salario_familiar<20000:
#     print("Tienes derecho a beca")
# else:
#      print("No tienes derecho a beca")


#En este ejemplo, le damos prioridad al salario familiar sobre las demás condiciones 
# y hacemos esto usando el operador or, para que aunque cumpla las condiciones de distancia 
# y numero de hermanos si el salario familiar es bajo, se acepte como buena 
# y pueda imprimir tienes derecho a beca.

#EJEMPLO 3

# print("Asignaturasoptativas Año 2026")
# print("Asignaturas optativas:Informática grafica - Pruebas de software - Usabilidad y accesibilidad")
# asignatura=input("Escribe la asignatura escogida:")

# if asignatura in ("Informatica grafica","Pruebas de software", "Usabilidad y accesibilidad"):

#    print("Asignatura elegida " + asignatura)
# else:
#      print("La asignatura escogida no esta contemplada")


#En este ejemplo va comparar lo que hay almacenada en la variable asignatura, 
# con los elementos que están en el operador in con los valores de tipo string (texto con comillas), 
# y si es verdad imprimirá Asignatura elegida y se concatenara con la variable asignatura, 
# no se tiene que usar la función str para pasar la variable asignatura a string porque ya lo es 
# y si no es verdad se activara else y imprimirá La asignatura escogida no esta contemplada. 

#Nota: Python es case senstitive (distingue entre mayúsculas y minúsculas).

#EJEMPLO 4

# print("Asignaturas optativas Año 2026")
# print("Asignaturas optativas:Informática grafica - Pruebas de software - Usabilidad y accesibilidad")
# opcion=input("Escribe la asignatura escogida:")

# asignatura=opcion.lower()

# if asignatura in ("informática grafica", "pruebas de software", "usabilidad y accesibilidad"):

#      print(f"Asignatura elegida {asignatura}")


# else:
     
#      print("La asignatura escogida no esta contemplada")



#En este ejemplo, tomamos el valor sucio de la variable opcion, 
# lo limpiamos transformándolo a minúsculas con la función .lower(), 
# y el resultado final lo guardamos en la nueva variable asignatura. 
# Así aseguramos que la comparación sea perfecta sin importar cómo escriba el usuario."

#Nota: 

#Funcion lower() = Transforma cualquier valor a minúscula

#Funcion upper() = Transforma cualquier valor a mayúscula

#F-String (Literal de Cadena Formateado)
# Permite meter cualquier variable (números, listas, textos) 
# dentro de una frase sin tener que estar convirtiendo con str() 
# o poniendo mil signos de +.

#PARTE 2 

# --- PROYECTO ZENKAI: Bunker Access Control ---
# Combinando: Video 13 (in, or, and) + Inglés (Whose) + .lower()

print("\n--- GAWAIN SECURITY SYSTEM ---")

# Usando la frase 'Whose' de la mañana
user_input = input("Whose access is this? (Enter your name): ")
user_name = user_input.lower()

authorized_users = ("hector", "zero", "pacho8a")

# Simulando datos de entrada
age = int(input("Enter your age: "))
distance = int(input("How many km are you from the bunker? "))

# APLICANDO LÓGICA DE JUAN DÍAZ (VÍDEO 13)
if user_name in authorized_users or (age >= 18 and distance < 10):
    print(f"Access Granted. Welcome back, {user_name}!")
    print("Those 32GB of RAM are ready for you.") # Frase de inglés de hoy
else:
    print("Access Denied. This isn't your computer.") # Negación de hoy

#"En este proyecto usamos un programa de seguridad llamado Gawain, aplicando las frases de inglés del bloque alfa. Usamos la función input para guardar el nombre en user_input y luego lo normalizamos con la función .lower() en la variable user_name para que todo esté en minúsculas. Los usuarios permitidos se guardan en authorized_users.
#La Lógica del Acceso:
#Si la variable user_name encuentra el nombre en la lista usando la función in, o bien...
#Si se cumplen los parámetros de edad (>= 18) y distancia (< 10) que están agrupados en paréntesis para que funcionen como un solo bloque (Jerarquía de Operadores).
#Si cualquiera de esas se cumple, se imprime el acceso con una F-string. Si no, el else niega la entrada."