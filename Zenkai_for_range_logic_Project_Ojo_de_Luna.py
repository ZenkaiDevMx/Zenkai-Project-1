#DIA 12 BUCLE FOR 3 RANGE -F STRING
#PARTE 1

#EJEMPLO 1:

# for i in range(5):
#     print(f"Valor de la variable {i}")

#Al usar la función "f" al principio en el print, 
# nos ayuda a unir texto con variables en este caso {i} 
# en otras palabras se imprime 5 veces por numero entero range 
# el nombre de la variable y al final al poner la i entre corchetes 
# se pone 0,1,2,3,4 respectivamente. 

#Nota: Si no ponemos la f, imprimirá literal la letra i.

#EJEMPLO 2:

# for i in range(5,50,3):
#     print(f"Valor de la variable {i}")

#Ahora le estamos diciendo que empiece a contar desde el 5, 
# llegue hasta el 49 (es el tope) y lo hago en 3 en 3 va llegar al 47 
# porque el 50 ya no se podría.

#EJEMPLO 3:

# valido=False

# email=input("Introduce tu email: ")

# for i in range(len(email)):
#     if email[i]=="@":
#        valido=True

# if valido:
#     print("Email correcto")

# else:
#     print("Email incorrecto")


#Cuanto introduces por teclado por ejemplo Juan, el bloque for se activa y la función len en range te dice que va entrar 4 veces(0,1,3,4)  a dar vueltas de validación el bucle for en if checando si hay una @,  en este caso no detectara y saltara la líneas siguiente y se ira directo al else y imprimirá Email incorrecto, por consiguiente si pongo por ejemplo juan@pildoras ya me dará email correcto.

#Nota: función len: siempre te va arrojar el numero de caracteres(Juan = 4).

#PARTE 2

# --- PROYECTO ZENKAI OJO DE LUNA: ESCÁNER DE RUIDO V1.0 ---
#Simulamos una línea de píxeles de Zyuranger (1992)
# El "#" representa el ruido que queremos eliminar

pixeles = "11001100#110011" 

print(f"--- Iniciando escaneo de {len(pixeles)} bits de imagen")

for i in range(len(pixeles)):
    if pixeles[i]=="#":
        print(f"ALERTA: Ruido detectado en la posicion {i}.")
        print("Activando IA de restauración... [STATUS: PROCESSING]")

print("--- Escaneo de Sinergia: COMPLETADO ---")