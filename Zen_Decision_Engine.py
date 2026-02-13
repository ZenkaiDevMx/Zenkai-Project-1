# DIA 6

#PARTE 1 CONDICIONALES IF, ELSE, ELIF, EJEMPLOS

#Ejemplo 1

# print("verificación de acceso")
# edad_usuario=int(input("Introduce tu edad, por favor"))

# if edad_usuario<18:
#    print("no puedes pasar")
# else:
#    print("Puedes pasar")
# print("El programa ha finalizado")

#Es un pequeño programa que te diga si puedes pasar si eres mayor de edad y si eres menor de edad no puedes pasar, 
# # primero va imprimir verificar el acceso, luego la variable edad_usuario y usar la función int para pasar a entero 
# y usar input para guardar por teclado en la variable edad_usuario, después de preguntar la edad, usamos la condicional if 
# y la variable edad_usario con el menor que que 18 y imprimir no puedes pasar, si la condición de if es cierta el else lo ignora 
# y después imprimi la ultima linea en este caso el programa ha finalizado.


#Ejemplo 2


#print("verificación de acceso")
#edad_usuario=int(input("Introduce tu edad, por favor"))

#if edad_usuario<18:
   #print("no puedes pasar")
#if edad_usuario>100:
   #print("Edad incorrecta")
#else:
   #print("Puedes pasar")
#print("El programa ha finalizado")

#En este segundo ejemplo, calibramos la lógica poniendo que tener mas de 100 de vida va imprimir edad incorrecta, agregando un segundo if, funcionara correctamente para edades mayores de 18 pero si ponemos una edad menor como 14 , el programa funciona sin crashear, pero entrega dos resultados contradictorios porque el else solo está vinculado al segundo if, en otras palabras imprimiria ambos, este es un error de lógica,  para crear una sola cadena de decisión y evitar este 'glitch', usaremos el elif en el siguiente ejemplo."

#Ejemplo 3


##edad_usuario=int(input("Introduce tu edad, por favor"))

#if edad_usuario<18:
   #print("no puedes pasar")
#elif edad_usuario>100:
   #print("Edad incorrecta")
#else:
   #print("Puedes pasar")
#print("El programa ha finalizado")

#En este tercer ejemplo, corregimos el error lógico, 
# simplemente usando la instrucción elif, 
# que es mucho mas rápida y segura para cuando hay mas de 2 condiciones 
# y ya funciona el programa correctamente.

#Ejemplo 4


# print("verificación de acceso")
# nota_alumno=int(input("Introduce tu nota, por favor"))

# if nota_alumno<5:
#     print("Insuficiente")

# elif nota_alumno<6:
#      print("Suficiente")

# elif nota_alumno<7:
#      print("Bien")

# elif nota_alumno<9:
#      print("Notable")

# else:
#      print("Sobresaliente")

#En el cuarto ejemplo, seguimos usando la instrucción elif, 
# pero ahora hacemos un programa que nos diga que nos diga el nivel de nuestra nota, 
# según el numero de las notas que pongamos, usamos un if varios elif y un else, 
# todo esta estructura funciona como un único bloque y 
# el else se ejecuta si no entra en ninguna de las opciones anteriores, 
# si pongo un 4, validara el primer if (insuficiente) y ingnorara las demás 
# y como no hay mas el programa terminaría.

# ---------------------------------------------------------
# PARTE 2: PROYECTO PERSONAL: ANALIZADOR DE VALOR (RTX 5060 Ti)
# ---------------------------------------------------------

print("\n--- BIENVENIDO AL GAWAIN GPU ANALYZER ---")

# Datos basados en el reporte de Linus de hoy:
# 5060 Ti 8GB = $380 | 5060 Ti 16GB = $430
precio_usuario = int(input("Introduce el precio que encontraste para la GPU ($): "))

def analizar_valor(precio):
    if precio <= 380:
        return "¡RANGO S! Es el precio base. Compra recomendada."
    elif precio <= 430:
        # Aquí están los $50 bucks de diferencia que viste con Linus
        return "RANGO A: Es la versión de 16GB. Solo vale la pena por la VRAM extra."
    elif precio < 500:
        return "RANGO B: Está algo cara, pero aceptable si urge."
    else:
        # La lógica de "Expensive" que escuchaste en el video
        return "¡ERROR DE VALOR! Demasiado caro (Expensive). Mejor esperar al CyberPower."

print(f"Resultado del análisis: {analizar_valor(precio_usuario)}")
