#PILDORAS INFORMATICAS
#PYTHON
#VIDEO 21
#EXCEPCIONES 1
#PARTE 1

#EXCEPCIONES

#.¿Que es una excepción?
#.Como manejar excepciones

#.Las excepciones son errores que ocurren durante la ejecución del programa. La sintaxis del código es correcta pero durante la ejecución ha ocurrido "algo inesperado".

#.Este tipo de errores de ejecución se pueden controlar para que la ejecución del programa continúe. Es lo que se conoce como manejo o control de excepciones.

#NOTA: si el programa es corto como los del curso pues no hubiera mucho problema, pero si el código es largo ahí si hubiera un problema cuando te sale un error inesperado no uno común (identacion, falta de coma etc).

#EJEMPLO 1

# def suma(num1, num2):
# 	return num1+num2

# def resta(num1, num2):
# 	return num1-num2

# def multiplica(num1, num2):
# 	return num1*num2

# def divide(num1,num2):		
# 	return num1/num2
	

# op1=(int(input("Introduce el primer numero: ")))

# op2=(int(input("Introduce el segundo numero: ")))		
	
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


# print("Operación ejecutada. Continuación de ejecución del programa ")

#Es un programa que tiene 4 funciones, la primera función suma, la segunda resta, la tercera multiplica y la ultima divide, 
# luego le pedimos al usuario que introduzca por teclado dos valores de tipo entero que se almacenaran en las variables op1 y op2 
# después de introducir esos dos valores le pedimos al usuario que introduzca también por teclado una operación a realizar con los valores 
# que introdujo anteriormente, puede sumar, restar, multiplicar y dividir dependiendo del texto que introduzca cuando le pedimos la operación, 
# si pone resta, restara los dos valores que introdujo anteriormente y lo va hacer porque después hay unos condicionales que evalúan a introducido 
# el usuario en la operación a realizar, vamos a imprimir lo que devuelva la función resta después de pasarle los dos parámetros introducidos por teclado, 
# también contemplamos que a lo mejor el usuario pone un mensaje que no esta contemplado y imprimirá operación no contemplada y cuando todo esto termina 
# imprime operación ejecutada, continuación de ejecución del programa y imaginamos que sigue muchas líneas de código mas.

#NOTA: si provocamos en este código un error de darle al primer numero 8 y al segundo numero 0 y poner una división, marcara dos errores, pero lo que hay 
# que notar es que al tener ese error, la ultima linea de código de imprimir nunca se ejecuta, y si hubiera miles líneas de código no se ejecutaría ninguna, 
# porque el error interrumpe el flujo del código.

#Se arregla el ejemplo anterior con esto:

#Captura o control de excepción: Le estamos diciendo intenta realizar esta instrucción y si no puedes que el resto del programa se ejecute, asi le estamos 
# damos prioridad a las que si queremos se ejecuten.

#Pila de llamada: Se le llama a las líneas de código donde se marco el error y nos da información valiosa para detectar el error, en este caso en la linea 29 
# en op1 y op2 y la segunda en la linea 11 con la función divide y fijarse muy bien en la descripción del error en este caso ZeroDivisionError.

#EJEMPLO 2

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

# op1=(int(input("Introduce el primer numero: ")))

# op2=(int(input("Introduce el segundo numero: ")))		
	
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


# print("Operación ejecutada. Continuación de ejecución del programa ")

#Aquí siguiendo para arreglar el ejemplo anterior, gracias que detectamos en que líneas estaba el error 
# y el tipo de error en este caso ZeroDivisionError que en otras palabras seria error de dividir cero, 
# aplicamos una especie de bypass, poniendo antes de la instrucción que es propensa de cometer el error 
# que en este caso es la de return num1/num2 la tenemos que poner dentro de un bloque try except, primero 
# el try después num1/num2 y después la clausula except y el nombre del error ZeroDivisionError y dentro 
# de la clausula except lo que quieres que el programa quieras, imprimir no se puede dividir entre 0 y 
# hacer que devuelva con return operación errónea, en otras palabras le decimos a la función divide 
# que intente realizar esta intruccion y en caso que no lo consiga ejecuta lo que estará en el except 
# ( es parecido a como funciona un if/else) y asi podemos salvar nuestro programa para que no se caiga 
# o rompa y siga su flujo hay que aclarar si la excepción que estas capturando no es que el programa comete, 
# caera igualmente, en este caso si le dimos exactamente en el error, haciendo que imprimirá la ultima linea 
# o si hubiera miles mas también se ejecutarían.


#PARTE 2

#PROYECTO ZENKAI: "THE RELIABLE BÚNKER ANALYZER"

# DIA 17 - PROYECTO DE SINERGIA TOTAL
# UNIÓN DE BLOQUES: ALFA, AKIHABARA, BETA Y GAMMA
# ARCHIVO: Zenkai_Excepciones_Sinergia.py

def zenkai_calculator(val1, val2):
    # INGLÉS (PACHO L22): Usamos "Really" para enfatizar la necesidad de chequeo
    print("\n[SYSTEM CHECK]: I REALLY need to verify this hardware data...")
    
    try:
        # BLOQUE BETA (PYTHON V21): Intentamos la operación propensa a error
        # DUKE MATH (MÓDULO 3): La división representa la relación lógica entre variables
        result = val1 / val2
        
        # INGLÉS: Si tiene éxito, usamos "Very" como intensificador de éxito
        print(f"-> SUCCESS: The result is {result}. It works VERY well!")
        
    except ZeroDivisionError:
        # AKIHABARA (KIRA L1-6): Si hay un error, usamos la negación "Dewa Arimasen"
        # "Ureshi" significa feliz/bueno. "Dewa arimasen" significa "No es".
        print("-> ALERT: ZeroDivisionError detected!")
        print("-> JAPO LOG: Sugoi ureshi DEWA ARIMASEN (Esto NO es muy bueno/feliz).")
        
        # Devolvemos un status controlado para que el programa siga vivo
        result = "Bypass Activated: Operation Denied"

    return result

# --- EJECUCIÓN DEL BÚNKERE ---

# Escenario A: Datos correctos (Poder del Ryzen 7)
print("TEST 1: High Performance Mode")
zenkai_calculator(9000, 10) # 9000 de Ki entre 10 núcleos

# Escenario B: Error inesperado (Simulando un apagón sin No-Break)
print("\nTEST 2: System Crash Simulation")
final_loot = zenkai_calculator(7700, 0) # Ryzen 7700 entre 0

print(f"\n[FINAL STATUS]: {final_loot}")
print("Mission Complete: The bunker is still online thanks to exceptions.")
