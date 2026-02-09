# Script de Bautizo - ZenkaiDevMx
# Objetivo: Demostrar lógica condicional y funciones

def validar_nivel(power_level):
    if power_level > 8000:
        print("¡Zenkai activado: Eleva tu Ki")
        print("Rebasaste el límite de poder")
    else:
        print("Entrenando, Desbloquea tu potencial oculto")

# Cambia este valor para probar tu nivel de pelea
mi_poder = 9000 
validar_nivel(mi_poder)
print("Fin del escaneo de sistema.")
