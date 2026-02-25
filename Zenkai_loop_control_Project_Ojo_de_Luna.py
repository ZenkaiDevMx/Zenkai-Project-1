#VIDEO 18
#BUCLES 5
#CONTINUE, PASS, ELSE

#PARTE 1

#.Continue: salta la siguiente vuelta

#.Pass: Solo se usa en casos especificios, 
# igual como un señalador o separador por si 
# vas a usar esa parte del código para después.

#.Else: Solo se activa si el bucle fue True.

#EJEMPLO 1

# for letra in "Pyhton":

#     if letra=="h":
#        continue

#     print("Viendo la letra: " + letra)

#Aquí en cualquier vuelta de bucle, 
# ira validando hasta que encuentre la letra h 
# y se active el continue, cuando la encuentre ignorara 
# la siguiente linea de código en este caso print 
# y salta a la siguiente vuelta de bucle.

#EJEMPLO 2

# nombre="Pildoras Informaticas"

# contador=0

# for i in nombre:

#     if i ==" ":
#        continue
#     contador+=1

# print(contador)

#Aquí creamos un código para que nos imprima cuantas letras exactas 
# hay en píldoras informáticas, para eso, en cada vuelta de validación de bucle for 
# ira contando y pones una condición con el if, si encuentra un carácter en blanco 
# se activa el continue y lo ignora y salta la siguiente linea de código de contador 
# y siga contando las letras y ya imprimiría exactamente que tiene 20.

#NOTA: contador=contador=1 es igual a contador+=1 para abreviar.

#EJEMPLO 3

# while True:
#     pass

#Mantiene el programa ocupado en un bloque infinito, 
# hasta que el usuario rompa el programa con el comando ctrl+c

#EJEMPLO 4

# class MiClase:
#      pass #Para implementar mas tarde

#Lo dejamos como en espera para usar después, 
# y puede correr el código sin afectar esta parte.

#EJEMPLO 5

# email=input("Introduce tu email, por favor:")

# for i in email:

#     if i=="@":

#        arroba=True

#        break;

# else:

#      arroba=False

# print(arroba)

#Este código hace que cuando le introduces por teclado el email, 
# si no tiene @, cuando en el bucle for en la instrucción if este 
# haciendo sus vueltas de validación y no encuentra @ se saltara 
# hasta el else dará False imprimirá False, si introducimos un correo con @, 
# en las vueltas de validación del bucle for instrucción if dira que la arroba vale True, 
# hará un break y se saldrá del bucle for y tambien ignorara el else porque esta dentro del bucle for, 
# y se saltara el @ vale False y imprimirá @ = True.

#NOTA: La instrucción else dentro del bucle funciona diferente que dentro de una condicional, 
# solo se ejecuta cuando el bucle este vacío, en otras palabras cuando ya haya hecho todas sus vueltas de validación, 
# en este caso como hay un break, saldría al bucle for y nunca tocaria el else (amenos que lo pongas sin @).

#PARTE 2

# --- PROYECTO ZENKAI OJO DE LUNA: ESCÁNER DE CALIDAD ---
frames = ["Nítido", "Borroso", "Nítido", "Nítido", "Borroso"]

print("--- Iniciando análisis de frames de GTO (1998) ---")

for f in frames:
    if f == "Borroso":
        print("Frame borroso detectado. Saltando proceso de  escalado...")
        continue
    print(f"Procesando frame {f}... [STATUS:RENDERIZADO 4K]")

else:
    print("--- ESCANEO FINALIZADO: Todos los frames válidos fueron procesados. ---")

#Vamos a simular que escaneamos 5 frames de GTO. Si un frame es "borroso", usamos continue para saltarlo. 
# Si logramos pasar todos los frames, el else confirmará la salud del video.