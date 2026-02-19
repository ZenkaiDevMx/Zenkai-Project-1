#DIA 10 PYTHON
#LECCION VIDEO 15
#BUCLES 2
"""
#ZENKAI LOGIC - VIDEO 15 SUMMARY:
#1. Boolean Flags: Initializing as 'False' (Waiting for data).
#2. Range Function: Semi-open intervals [start, end).
#3. Indexing: We always start counting at 0 (Computers count offsets).
"""

#PARTE 1

#EJEMPLO 1

# for i in ["Píldoras","Informaticas",3]:
#     print ("Hola")

#Va imprimir la palabra hola, 
# por defecto 3 veces por cada uno de los elementos.

#EJEMPLO 2

# for i in ["Píldoras","Informaticas",3]:
#     print ("Hola", end="")

#Si queremos que imprima sin salto de linea, usamos el argumento end, 
# lo que hace que finalice la impresion en un espacio que no existe,
# en otras palabras imprime horizontalmente pegado las palabras.

#EJEMPLO 3

# for i in ["Píldoras","Informaticas",3]:
#     print ("Hola", end=" ")

#Es lo mismo que lo anterior pero aquí solo le hacemos un espacio a las comillas 
# para que cuando imprima, también respete ese espacio, y le podemos poner los espacios 
# que queramos y imprima tal cual lo hacemos.

#EJEMPLO 4

# for i in "juan@pildorasinformaticas.es":
#     print ("Hola", end=" ")

#Aquí le decimos que va imprimir Hola tantas veces 
# como letras o caracteres hay en el bloque in.

#EJEMPLO 5

#Nota: True y False en Python va con la primera letra en mayúscula.

# email=False

# for i in "juan@pildorasinformaticas.es":
#     if(i=="@"):
#        email=True

# if email==True:
#     print("Email es correcto")
# else:
#     print("El email no es correcto")

#Aquí le estoy diciendo, que por defecto los email están en espera de información 
# por lo tanto están en False y después de teclear la info si detecta un @ cambie la instrucción a True, 
# terminando de validar imprima es correcto y sino lo detecta se vaya directo al else y imprima el email no es correcto

#EJEMPLO 6


# email=False

# for i in "juan@pildorasinformaticas.es":
#     if(i=="@"):
#        email=True

# if email:
#     print("Email es correcto")
# else:
#     print("El email no es correcto")

#Aquí para simplicar la linea de código podemos poner en el if, 
# solo el nombre de la variable booleana en este caso email y 
# automáticamente Python lo leerá como True.

#Nota: un = asigna y == comparan,
#en otras palabras usamos el operador de un igual para asignar, estamos damos valor a una variable 
# y cuando usamos el operador de 2 iguales estamos comparando una variable con otra o una variable con un valor o dos variables.

#EJEMPLO 7


# email=False
# miEmail=input("Introduce tu dirección de email:")

# for i in miEmail:
#     if(i=="@"):
#        email=True

# if email:
#     print("Email es correcto")
# else:
#     print("El email no es correcto")

#Aquí le estamos diciendo, que va estar en espera antes de la asignación de datos, 
# leera la variable miEmail y te pedirá teclar el correo para validarlo y 
# después de la revisión podrá imprimir según sea el caso en True o False imprimirá un texto o otro.

#EJEMPLO 8


# contador=0
# miEmail=input("Introduce tu dirección de email:")

# for i in miEmail:
#     if(i=="@" or i=="."):
#        contador=contador+1

# if contador==2:
#     print("Email es correcto")
# else:
#     print("El email no es correcto")


#Empezamos que la variable contador, empieza con el valor 0, 
# esperara que se le asigne información, cuando entra la información, 
# la función for se activara y empezara a analizar, si detecta un @ o si detecta un punto, 
# cualquiera de las dos, debe ser exacto para que pueda marcar aprobado en dado caso, 
# si el usuario pone "h..@g.com", el contador dará 4 y fallará.

#EJEMPLO 9

# for i in range(5):
#     print("Hola")

#Aquí ejecutara el tipo range, usaras el bucle for con contadores, 
# esta diciendo que imprima el valor entero exacto que marcas, 
# en este caso 5 veces el Hola.

#EJEMPLO 10

# for i in range(5):
#     print(i)


#El range crea una lista de 5 elementos partiendo desde el 0,1,2,3,4.

#PARTE 2

# PROYECTO ZENKAI INTEGRADO: 
# INGLÉS (LECCIÓN 15) + PYTHON (EJEMPLO 8)

# 1. El programa arranca pidiendo el email para validar al alumno.
contador = 0
email = input("Introduce tu email para practicar DO/DOES: ")

for i in email:
    if i == "@" or i == ".":
        contador = contador + 1

# 2. Si el email es EXACTO (2 validaciones), entramos a la lección de inglés.
if contador == 2:
    print("\n--- Acceso Concedido: Práctica de DO y DOES ---")
    
    # Lista de sujetos para practicar la regla
    sujetos = ["I", "You", "He", "She", "It", "We", "They"]
    
    for persona in sujetos:
        # Lógica de programación aplicada a la gramática:
        if persona == "He" or persona == "She" or persona == "It":
            print(f"Para '{persona}' usamos: DOES (Tercera persona)")
        else:
            print(f"Para '{persona}' usamos: DO")
            
    print("\nREGLA ZENKAI: ¡Escúchalo lento 2 veces primero!")

else:
    print("Email incorrecto. El contador no dio 2. No puedes pasar.")

