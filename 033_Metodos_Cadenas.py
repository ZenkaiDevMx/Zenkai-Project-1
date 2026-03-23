# PILDORAS INFORMATICAS
# PYTHON
# VIDEO 33
# METODOS DE CADENAS
# PARTE 1

#.Uso de métodos de cadenas (String)

#🐍 ESTRATEGIA BETA: MÉTODOS DE CADENAS (V33)

#Las cadenas en Python son inmutables (no cambian), pero estos métodos te devuelven una versión "mejorada". 

#.upper() y .lower(): Para normalizar datos (muy útil para que Héctor y HECTOR sean lo mismo en tu base de datos).

#.capitalize(): Pone la primera en mayúscula. Elegancia pura.

#.count(): Cuenta cuántas veces aparece un carácter. (Imagina contar cuántas veces dice "error" un log).

#.find(): Te da la posición (índice) de un texto. Si no lo halla, devuelve -1.

#.isdigit(): ¡Vital! Te dice si la cadena es un número. Ideal para validar entradas del usuario.

#.isalum(): Revisa si es alfanumérico.

#.isalpha(): Revisa si solo son letras (incluyendo espacios).

#.split(): El rey de la segmentación. Corta una frase en una lista de palabras.

#.strip(): Borra los espacios basura al inicio y al final.

#.replace(): Cambia una palabra por otra (ej. cambiar "bug" por "feature"). 

#.find(): Busca la primera aparición de un texto de izquierda a derecha.

#.rfind() (la "r" es de Right): Busca la última aparición de un texto, empezando de derecha a izquierda.



         #String

#🐍 ACORDEÓN DE COMBATE: MÉTODOS DE CADENAS (S7)

#Método	            Acción Técnica 🛠️	                    Visión de Senior (Uso Real) 🧙‍♂️

# .upper()	Todo a MAYÚSCULAS.	        Resaltar alertas o gritar en logs.
# .lower()	Todo a minúsculas.	        Normalizar: que "Héctor" y "HECTOR" sean iguales.
# .capitalize()	Primera letra en Mayúscula.	Formatear nombres de usuario para que se vean bien.
# .strip()	Borra espacios al inicio y fin.	Limpiar: quitar espacios basura que mete el usuario.
# .replace
# ("a", "b")      Cambia "a" por "b".	        Corregir errores masivos o censurar palabras.
# .split(" ")	Rompe la cadena en una Lista.	Extraer: separar nombres de apellidos o datos CSV.
# .find("x")	Busca posición (Izq -> Der).	Saber si una palabra existe en un texto largo.
# .rfind("x")	Busca posición (DER -> Izq).	Rutas: hallar la última diagonal en un archivo/URL.
# .isdigit()	¿Es un número? (True/False).	Validar: evitar que el programa truene si no hay números.
# .count("x")	Cuenta cuántas "x" hay.	        Analizar frecuencia de palabras o errores.
                                                 
# .isalpha()	¿Son solo letras? (True/False).	 Validar que un nombre no tenga números (ej: H3ctor).
# .isalnum()	¿Es alfanumérico? (True/False).  Validar contraseñas o IDs de usuario.



#EJEMPLO #1

# nombreUsuario=input("introduce tu nombre de Usuario: ")

# print("El nombre es: ", nombreUsuario.upper())

#Si queremos poner el nombreUsuario a mayúsculas cuando tipeamos 
# en teclado minúsculas juan usando el método de cadena upper.



#EJEMPLO #2

# edad=input("introduce la edad:")

# while(edad.isdigit()==False):

#     print("Porfavor, introduce un valor numérico")
 
#     edad=input("Introduce la edad: ")

# if (int(edad)<18):
  
#    print("No puede pasar")

# else:
#      print("Puedes pasar")

# print(edad.isdigit())

#Por el input pasamos todo a texto, usamos un bucle while y el método de cadena isdigit para decir si es un digito o no lo es, 
# y se quedara en ese bucle hasta que le pongamos un numero, despues y usamos la funcion int para la edad pasar a numero entero 
# el texto pasado por input y poder compararlo, después que pueda validarlo se activara el if o el else según sea.   

#PARTE 2

# --- 🛡️ PROYECTO ZENKAI SINERGIA: VALIDADOR DE ACCESO S7 ---

# 1. El Dato de entrada (Inglés del Bloque Alfa)
frase_seguridad = "  everything_is_up_and_running  "

# 2. Tu misión: Limpiar los espacios y ponerlo todo en MAYÚSCULAS 
# Para que el sistema lo reconozca como un COMANDO DE ALERTA.
acceso_validado = frase_seguridad.strip().upper()

# 3. Resultado en el Monitor 4K
print(f"ESTADO DEL SISTEMA: {acceso_validado}")
