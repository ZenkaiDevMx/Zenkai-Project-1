def multiplicar_poder(base, multiplicador):
    return base * multiplicador 

# Aquí guardamos lo que el "return" nos devolvió en la variable 'resultado'
resultado = multiplicar_poder(8000, 2)

# Como 'resultado' tiene un valor real (16000), podemos seguir operando:
nuevo_nivel = resultado + 500

print("El resultado de la función fue:", resultado)
print("Sumándole un bono de entrenamiento:", nuevo_nivel)
