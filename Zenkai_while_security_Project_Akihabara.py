#DIA 13 VIDEO 17
#BUCLE 4 WHILE

#Bucle While
#.Sintaxis

#While condición:

      #cuerpo del bucle

#PARTE 1

#Nota: Su condición es ser idéntico como condicional #if, while es un bucle indeterminado, hay que tener #cuidado de no hacer bucles whiles que siempre sean #verdaderos.

#EJEMPLO 1

# i=1

# while i <=10:
#     print("Ejecución " + str(i))
#     i=i+1

# print("Terminó la ejecución")

#Si no le agregamos la instrucción (contador) de que la variable i valga +1 
# en cada vuelta de validación del bluce while, se quedara como un bucle infinito 
# y nunca imprimirá "termino la ejecución", pero asi como esta, imprimirá 10 veces, 
# como es el tope donde cumple la intruccion i<=10.

#EJEMPLO 2

# edad=int(input("Introduce tu edad por favor: "))

# while edad<0:
#     print("Has introducido una edad negativa. Vuelve a intentarlo")
#     edad=int(input("introduce tu edad por favor: "))

# print("Gracias por colaborar. Puedes pasar")
# print("Edad del aspirante " + str(edad))

#En este ejemplo no sabemos cuantas veces se va ejecutar el bucle while, 
# porque depende del usuario, si ponemos una edad correcta, imprimirá el mensaje correcto, 
# pero si no, incluso poniendo edades negativas, imprimirá hasta el infinito.

#EJEMPLO 3

# edad=int(input("Introduce tu edad por favor: "))

# while edad<5 or edad>100:
#     print("Has introducido una edad incorrecta. Vuelve a intentarlo")
#     edad=int(input("introduce tu edad por favor: "))

# print("Gracias por colaborar. Puedes pasar")
# print("Edad del aspirante " + str(edad))

#Aquí mientras se cumpla la condición de que la edad sea menor que 5 o edad mayor a 100 
# te imprimirá la edad incorrecta y si lo haces dentro de ese intervalo marcara gracias por colaborar, 
# si pones edades negativas también te marcara incorrecta porque es menor que 5 y se activa la condición.

#EJEMPLO 4

# import math

# print ("Programa de cálculo de raíz cuadrada")
# numero=int(input("Introduce un número por favor: "))

# intentos=0

# while numero<0:
#     print("No se puede hallar la raíz de un número negativo")

#     if intentos==2:
#         print("Has consumido demasiados intentos. El programa a finalizado")
#         break;

#     numero=int(input("Introduce un numero por favor: "))
#     if numero<0:
#          intentos=intentos+1

# if intentos<2:
#     solucion=math.sqrt(numero)
#     print ("La raíz cuadrada de " + str(numero) + " es " + str(solucion))



#En este ejemplo, vemos como hacer que jamás entre en un bucle infinito while, 
# sino restringirlo, las primeras líneas de código nos dan la bienvenida 
# y nos pide que introduzcamos en teclado, delimitamos que los intentos esta en cero, 
# y arranca el bucle while con la instrucción la variable numero es <0, 
# si se cumple esto nos imprime no se puede hallar la raíz y se activa 
# la intruccion if delimitando la variable intento a 2 veces mas, mas la primera, 
# hace que nuestro programa nos de 3 intentos máximos antes de romperse y bloquear 
# nuestro acceso gracias a la instrucción break, el contador se va aumentar 1 cada vez 
# que intente validar y marcar error como habíamos dicho con un máximo de 3 veces, ahora si, 
# si cumplimos la condición en true, se active el bloque de la instrucción if pero fuera del cuerpo 
# de la instrucción while, haciendo que tengamos 2 intentos para que nos de la raíz cuadrada, 
# usamos la clase math con la abreviatura de raíz cuadrada que es sqrt, lo que hacemos que 
# se guarde en la variable solución la raíz cuadrada del numero introducido en la segunda linea 
# del código o dentro del bucle while si ponemos un numero entero positivo imprimirá su raíz cuadrada.

#Nota: Concepto de Importación: Importar clases, además importante, la primera linea de código debe decir 
# import math, que le estamos diciendo que vamos importar esa clase especifica (math) para usar todas sus 
# operaciones aritméticas.

#PARTE 2

# - - - PROYECTO ZENKAI OJO DE LUNA: FILTRO NEURONAL ---
import math

print("--- Iniciando Denoising en GTO (1998) ---")
ruido_db =50 #  Nivel de ruido incial
intentos_filtro = 0

while ruido_db >10:
    print(f"Ruido actual: {ruido_db}dB.Aplicando limpieza...")
    intentos_filtro +=1

    if intentos_filtro == 3:
        print("ALERTA: El ruido es persistente. Abortando para evitar distorsion.")
        break
    
    ruido_db -= 15 #El filtro reduce el ruido en cada vuelta

if ruido_db <=10:
    print(f"Exito. Ruido final: {ruido_db}dB. Frame listo para 4K.")