# - - - ENTRENAMIENTO DE NIVEL DE PELEA - - -
print("---INICIANDO CARGA DE KI---")

#Vamos a contar de 500 en 500 hasta 3000
for ki in range(0,3500,500):
    #La F-string une el texto con la variable ki
    print(f"Nivel de ki actual: {ki}...")

    if ki >=3000:
        print("¡ADVERTENCIA: El Scouter está por explotar!")

print("--- Entrenamiento Terminado, Shogun ---")