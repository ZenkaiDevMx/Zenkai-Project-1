#DIA 5 Python

#PARTE 1 

#CONDICIONALES

def evaluación(nota):
    valoracion="aprobado"
    if nota<5:
        valoracion="suspenso"
    return valoracion

print(evaluación(4))

#Si la condición if en este caso de nota es true se va ejecutar la única linea de código que hay en el ejemplo en este caso valoracion=suspenso y continuar la linea de código a return e imprimir la evaluación cumpliendo el parámetro en este caso 4, y si no se cumple, simplemente la saltaría y seguiría en return en donde va devolver la valoración y imprimir la evaluación.

#Ejemplo 2

#print("Programa de evaluación de notas de alumnos")

#nota_alumno=input()

#def evaluacion(nota):
    #valoracion="aprobado"
    #if nota<5:
        #valoracion="suspenso"
    #return valoracion

#print(evaluacion(nota_alumno))

#Ejecutar la nota por teclado para hacer eso se necesita la función input es cuando el flujo de ejecución llegue a ella y se quedara a la espera hasta que pongamos un valor, entra en nuestro programa y se almacenara en la variable y después el programa funcionara, se crea una variable nota_alumno.

#Como funciona este programa, hay que ver muy bien la ruta de ejecución, se ejecuta la primera linea se imprima el mensaje (programa de... etc), se ejecuta la segunda y el programa queda a la espera de insertar un dato por teclado (input), cuando se introduce ese dato, se va almacenar por ejemplo el numero 7 en la variable (nota_alumno) y después seguiría ejecutando y hará la función de la condicional if, y cualquier cosa que se ponga, se va almacenar en este caso en nota, si corremos asi el código, nos marcara error, porque todo lo que esta con la función input lo traduce como texto aunque pongas numero.


#Ejemplo 3

print("Programa de evaluación de notas de alumnos")

nota_alumno=input()

def evaluacion(nota):
    valoracion="aprobado"
    if nota<5:
        valoracion="suspenso"
    return valoracion

print(evaluacion(int(nota_alumno)))

#La función int, convertirá en entero mientras sea posible, todo lo que pongas dentro de los parámetros (), y ya la variable (nota_alumno) se convertirá en entero y se almacena en nota y ya se podrá correr el programa correctamente, poniendo el 7 y decir que estas aprobado.

#SEGUNDA PARTE

# RETO ZENKAI: EVALUACIÓN DE HARDWARE

print("\n--- Verificación de Presupuesto GPU ---")
precio_gpu = input("¿Cuánto cuesta la GPU en USD?: ")

def check_budget(price):
    # Usamos la lógica de Steve (Hardware Unboxed)
    if int(price) < 400:
        return "¡Oferta Zenkai! Cómprala antes de que se agote."
    else:
        return "Precio alto. Mejor esperar al CyberPower y ahorrar."

print(check_budget(precio_gpu))

#Ejemplo 4

print("Programa de evaluación de notas de alumnos")

nota_alumno=input()

def evaluacion(nota):
    valoracion="aprobado"
    if nota<5:
        valoracion="suspenso"
        calificacion=7
    return valoracion

print(evaluacion(int(nota_alumno)))





#El ámbito o estructura del código, solo podras accesar a una variable solo en el mismo ámbito que fue declarada, en el ejemplo si agregamos la variable calificación, solo podremos acceder en el ámbito especifico y si se cumple la condicional if.
