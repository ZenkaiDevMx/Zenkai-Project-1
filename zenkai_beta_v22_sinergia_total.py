#PILDORAS INFORMATICAS
#PYTHON
#VIDEO 22
#EXCEPCIONES 2
#PARTE 1

#EJEMPLO 1

# def suma(num1, num2):
# 	return num1+num2

# def resta(num1, num2):
# 	return num1-num2

# def multiplica(num1, num2):
# 	return num1*num2

# def divide(num1,num2):		
	
#     try:
# 	    return num1/num2
	
#     except ZeroDivisionError:
#         print("No se puede dividir  entre 0")
#         return "Operación errónea"


# while True:
#     try:
#         op1=(int(input("Introduce el primer numero: ")))

#         op2=(int(input("Introduce el segundo     numero: ")))		

#         break

#     except ValueError:
#         print("Los valores introducidos no son correctos inténtalo de nuevo")	
# operacion=input("Introduce la operación a realizar (suma,resta,multiplica,divide): ")

# if operacion=="suma":
# 	print(suma(op1,op2))

# elif operacion=="resta":
# 	print(resta(op1,op2))

# elif operacion=="multiplica":
# 	print(multiplica(op1,op2))

# elif operacion=="divide":
# 	print(divide(op1,op2))

# else:
# 	print ("Operación no contemplada")

#Ahora si cuando nos pida un numero, ponemos algo que no sea numero por ejemplo letras, 
# va tirar error y en este caso es el tipo de ValueError, ahora tenemos que ir a la linea 
# que nos marca el error donde esta el op1 y op2, falla porque nos pide un entero entonces 
# vamos a cubrirlo con un try y un except especificando el tipo de error ValueError y especificamos 
# que imprima Los valores introducidos no son correctos, para que los posibles errores no lleguen a 
# los condicionales, una de las posibles soluciones sea poner el op1 y op2 en un bucle infinito while True 
# y poner un break para salir antes del except para seguir el flujo de código, si ponemos valores erróneos 
# leera el except y imprimirá Los valores introducidos no son correctos inténtalo de nuevo, si dame un valor 
# correcto y uno incorrecto se quedara como un bucle infinito y solo saldrá cuando pongamos los dos valores correcto.


#EJEMPLO 2

# def divide():

#      try:
#          op1=(float(input("Introduce el primer número:")))

#          op2=(float(input("Introduce el segundo número: ")))

#          print("La división es:" +str(op1/op2))
#      except ValueError:
#             print("El valor introducido es erróneo")

#      except ZeroDivisionError:	
#            print("No se puede dividir entre 0!")


#      print("Cálculo finalizado")

# divide()


#Aquí usamos una función divide, que va ser todo, nos va pedir la introducción de los dos valores numéricos, 
# va hacer el calculo, imprimirá el calculo y dará un mensaje final de calculo finalizado, usaremos el float 
# en lugar del string para poder trabajar con decimales y al final imprimirá el resultado del calculo uniéndolo 
# con la función str la división op1/op2 y imprimara el calculo finalizado, ahora el bloque de op1 hasta el print 
# calculo finalizado es  susceptible a un cumulo de error para remediar esto lo cubrimos con un try al principio del 
# bloque y antes del final varios except con diferentes tipos de error para prevenirnos que se nos cuelgue el programa, 
# en este caso pondremos de tipo ValueError y ZeroDivisionError.

#EJEMPLO 3

# def divide():

#      try:
#          op1=(float(input("Introduce el primer número:")))

#          op2=(float(input("Introduce el segundo número: ")))

#          print("La división es:" +str(op1/op2))
     
     
#      except: 
          
#         print("Ha ocurrido un error")

     
#      print("Cálculo finalizado")

# divide()


#Podriamos poner solo un except general sin especificar el tipo de excepción dentro del except, 
# es poco recomendable porque no detalla que tipo de error especifico es, pero almenos el programa no se cuelga.

#EJEMPLO 4

# def divide():

#      try:
#          op1=(float(input("Introduce el primer número:")))

#          op2=(float(input("Introduce el segundo número: ")))

#          print("La división es:" +str(op1/op2))
#      except ValueError:
#             print("El valor introducido es erróneo")

#      except ZeroDivisionError:	
#            print("No se puede dividir entre 0!")


#      finally:      

#            print("Cálculo finalizado")

# divide()

#Si tu quieres que un codigo se ejecute siempre se puede usar introducir ese código 
# dentro de una clausula finally, lo que hace, es que lo que pongas dentro siempre 
# se va ejecutar tanto si se captura una excepción como si no ocurre, si todo va bien 
# el except no se ejecuta y el finally si y va mal no se ejecutara el try, se ejecutara 
# el except correspondiente y después el finally se va ejecutar si o si, es muy útil en 
# base de datos si queremos algo no importa que pase se va ejecutar.

#EJEMPLO 5

# def divide():

#      try:
#          op1=(float(input("Introduce el primer número:")))

#          op2=(float(input("Introduce el segundo número: ")))

#          print("La división es:" +str(op1/op2))
     
#      finally:      

#         print("Cálculo finalizado")

# divide()


#Aquí el finally es clave, porque el bloque try va intentar ejecutarlo 
# y si al introducir los datos te marca cualquier error, el programa no va caer, 
# porque igual va imprimir lo que este dentro del finally.

#PARTE 2

# PROYECTO: SINERGIA ZENKAI (ALFA + AKIHABARA + GAMMA -> BETA)
# OBJETIVO: PROCESAR EL KI DE LOS IDIOMAS Y LA MATEMÁTICA CON ESCUDO DE EXCEPCIONES

def procesador_zenkai_maestro():
    # --- BLOQUE GAMMA: LÓGICA DE DERIVADAS (Duke Math) ---
    # La derivada de f(x) = x^n es n*x^(n-1). 
    # Usaremos esto para calcular la "Aceleración del Aprendizaje".
    
    print("--- INICIANDO ESCANEO DE SISTEMAS ZENKAI ---")
    
    try:
        # --- BLOQUE ALFA (English - L23): LOOK, SEE, WATCH ---
        # Simulamos que Héctor "mira" (Look) los datos de entrada.
        print("\n[ALFA English Mode]")
        print("Look at the monitor! We need to see if the Ki level is correct.")
        nivel_ki = float(input("Enter your current Ki level (e.g., 5.0): "))
        
        # --- BLOQUE AKIHABARA (Japonés - L1-7): Partícula も ---
        # Si el Ki es alto, el Inglés es bueno y el Japonés "También" (も) lo es.
        print("\n[AKIHABARA Japanese Mode]")
        print("Eigo wa sugoi desu. Nihongo mo sugoi desu ka?") # ¿El japonés también es increíble?
        confirmacion_mo = input("¿El Japonés también es increíble? (si/no): ").lower()
        
        if confirmacion_mo == "si":
            particula_mo = "も (MO) ACTIVADA"
        else:
            particula_mo = "は (WA) ESTÁNDAR"

        # --- CÁLCULO DE DERIVADA (Sinergia de Datos) ---
        # Calculamos la tasa de cambio del éxito: f(x) = Ki^2 -> f'(x) = 2*Ki
        tasa_exito = 2 * nivel_ki
        
        print(f"\n--- RESULTADO DEL ESCANEO ---")
        print(f"Status: {particula_mo}")
        print(f"Tasa de Cambio (Derivada del Éxito): {tasa_exito}x faster than the 99%.")

    # --- BLOQUE BETA: EXCEPCIONES II (Píldoras V22) ---
    # Aquí aplicamos los múltiples "except" y el "finally" de Juan Díaz.
    
    except ValueError:
        # Si Héctor mete "paja" o texto donde va el nivel de Ki.
        print("\n❌ ERROR DE TIPO (ValueError):")
        print("Héctor, 'Look' closely! El Ki debe ser un número decimal.")
        
    except ZeroDivisionError:
        # En caso de una operación matemática ilegal (División entre 0).
        print("\n❌ ERROR MATEMÁTICO (ZeroDivisionError):")
        print("No puedes dividir tu fe entre cero. Papa Dios es infinito.")
        
    except Exception as e:
        # El escudo genérico (No recomendado pero útil para "Ki Maligno" desconocido).
        print(f"\n⚠️ ATAQUE DESCONOCIDO: {e}")

    finally:
        # EL PASO FINAL: Lo que pase siempre, como la disciplina de Héctor.
        print("\n[FINALLY PROTOCOL]")
        print("Logs guardados en el SSD Patriot Gen 4.")
        print("Ryzen 7 7700X enfriándose para la instalación del clima.")
        print("¡Misión cumplida, Shogun!")

# Ejecución del sistema
procesador_zenkai_maestro()
