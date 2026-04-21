# PILDORAS INFORMATICAS
# PYTHON
# VIDEO 71
# EXPRESIONES REGULARES 3

#.RANGOS


#EJEMPLO 1


# import re

# lista_nombres=['Ana',
#                 'Pedro',
#                 'María',
#                 'Rosa',
#                 'Sandra',
#                 'Celia']

# for elemento in lista_nombres:
#     if re.findall('[o-t]', elemento):

#        print(elemento)

#Aqui implementamos los rangos mediante el guion (-) dentro de los 
#corchetes [ ]. Al definir el patrón [o-t], le ordenamos al radar que 
#localice cualquier coincidencia que contenga caracteres situados 
#alfabéticamente entre la letra o y la letra t (o, p, q, r, s, t). 
#El sistema recorre la lista y valida los datos si encuentra cualquiera 
#de estas letras en cualquier posición del nombre. Esta técnica es fundamental 
#para la Soberanía de Datos, ya que permite crear filtros masivos de forma 
#abreviada, optimizando el procesamiento de información en el disco duro 
#sin necesidad de listar cada opción manualmente.



#EJEMPLO 2


# import re

# lista_nombres=['Ana',
#                 'Pedro',
#                 'María',
#                 'Rosa',
#                 'Sandra',
#                 'Celia']

# for elemento in lista_nombres:
#     if re.findall('^[O-T]', elemento):

#        print(elemento)

#Aqui combinamos el anclaje inicial (^) con un rango de letras mayúsculas 
#[O-T]. Al definir el patrón ^[O-T], el radar solo valida los datos si el 
#elemento comienza estrictamente con una letra mayúscula situada entre la O 
#y la T (O, P, Q, R, S, T). Esta maniobra es vital para la Soberanía de 
#Datos, ya que permite realizar una clasificación jerárquica instantánea, 
#descartando nombres que no cumplen con el criterio de inicio alfabético. 
#Es la técnica estándar para organizar directorios masivos o filtrar 
#registros por iniciales de forma rápida y eficiente en el disco duro.



#EJEMPLO 3


# import re

# lista_nombres=['Ana',
#                 'Pedro',
#                 'María',
#                 'Rosa',
#                 'Sandra',
#                 'Celia']

# for elemento in lista_nombres:
#     if re.findall('[o-t]$', elemento):

#        print(elemento)

#En este ejercicio combinamos un rango de letras minusculas [o-t] con el 
#anclaje final (). Al definir el patron [o - t], el radar solo valida los 
#datos si el elemento termina estrictamente con una letra situada entre la 
#o y la t. Es una maniobra de precision que permite filtrar registros 
#basandose en su caracter de cierre. En este caso, el sistema detecta a 
#Pedro porque termina en o, que esta dentro del rango, pero descarta a los 
#demas cuyos cierres (como la a) quedan fuera del limite alfabetico 
#marcado. Esta tecnica asegura que el bunker solo procese informacion con 
#terminaciones especificas en el disco duro.


#EJEMPLO 4


# import re

# lista_nombres=['Ma1',
#                 'Se1',
#                 'Ma2',
#                 'Ba1',
#                 'Ma3',
#                 'Va1',
#                 'Va2',
#                 'Ma4']

# for elemento in lista_nombres:
#     if re.findall('Ma[0-3]', elemento):

#        print(elemento)

#Aqui implementamos la combinación de un patrón de texto fijo con un rango 
#numérico [0-3]. Al definir el patrón Ma[0-3], le ordenamos al radar que 
#localice los datos que comience con el prefijo Ma seguido inmediatamente 
#por cualquier dígito entre el 0 y el 3. Esta técnica es fundamental para 
#la Soberanía de Datos, ya que permite segmentar registros, lotes o números 
#de serie que comparten una raíz común pero se distinguen por una 
#numeración específica. El sistema descarta tanto los elementos que no 
#empiezan con Ma como aquellos que, empezando con Ma, tienen un número 
#fuera del rango establecido (como Ma4).



#EJEMPLO 5


# import re

# lista_nombres=['Ma1',
#                 'Se1',
#                 'Ma2',
#                 'Ba1',
#                 'Ma3',
#                 'Va1',
#                 'Va2',
#                 'Ma4']

# for elemento in lista_nombres:
#     if re.findall('Ma[^0-3]', elemento):

#        print(elemento)

#Aqui implementamos la negación de rangos mediante el uso del acento 
#circunflejo (^) dentro de los corchetes [ ]. Al colocar el símbolo ^ al 
#inicio del corchete, el radar cambia su lógica: en lugar de buscar los 
#caracteres indicados, los excluye. El patrón Ma[^0-3] le ordena al sistema 
#localizar los datos que empiecen con Ma pero que NO termine con ningún 
#número entre 0 y 3. Esta técnica es vital para la Soberanía de Datos, ya 
#que permite realizar filtrados por excepción, descartando bloques de 
#información conocidos para enfocarse en los registros nuevos o fuera de 
#norma en el disco duro. 



#EJEMPLO 6


# import re

# lista_nombres=['Ma1',
#                 'Se1',
#                 'Ma2',
#                 'Ba1',
#                 'Ma3',
#                 'Va1',
#                 'Va2',
#                 'Ma4',
#                 'MaA',
#                 'Ma5',
#                 'MaB',
#                 'MaC']

# for elemento in lista_nombres:
#     if re.findall('Ma[0-3A-B]', elemento):

#        print(elemento)

#Aqui implementamos los rangos combinados dentro de un mismo par de 
#corchetes [ ]. Al definir el patrón Ma[0-3A-B], le ordenamos al radar que 
#localice los datos que comiencen con Ma seguido de un carácter que cumpla 
#cualquiera de las dos condiciones: ser un número entre 0 y 3, o ser una 
#letra mayúscula entre A y B. Esta técnica es fundamental para la Soberanía 
#de Datos, ya que permite crear filtros complejos y compactos para bases de 
#datos que mezclan nomenclaturas alfanuméricas. El sistema procesa la 
#información en el disco duro y valida registros como Ma2 o MaB, pero 
#descarta Ma5 o MaC por quedar fuera de ambos límites establecidos.


#EJEMPLO 7


# import re

# lista_nombres=['Ma.1',
#                 'Se1',
#                 'Ma2',
#                 'Ba1',
#                 'Ma:3',
#                 'Va1',
#                 'Va2',
#                 'Ma4',
#                 'MaA',
#                 'Ma.5',
#                 'MaB',
#                 'Ma:C']

# for elemento in lista_nombres:
#     if re.findall('Ma[.:]', elemento):

#        print(elemento)

#Aqui implementamos la localización de caracteres especiales mediante 
#clases de caracteres [ ]. Al definir el patrón Ma[.:], le ordenamos al 
#radar que busque los datos que comiencen con Ma seguido inmediatamente por 
#un punto (.) o por dos puntos (:). Es fundamental notar que, dentro de los 
#corchetes, el punto pierde su función de comodín y se comporta como un 
#carácter literal. Esta técnica es vital para la Soberanía de Datos, ya que 
#permite filtrar registros que utilizan signos de puntuación como 
#separadores técnicos en el disco duro, discriminando entre códigos simples 
#y códigos estructurados con simbología específica.



