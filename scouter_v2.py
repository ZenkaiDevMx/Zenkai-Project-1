# - - - SCOUTER SAIYAYIN OPTIMIZADO - - -
enemigos = ["Saibaiman 1", "Saibaiman 2", "Saibaman 3", "Saibaman 4", "Nappa", "Vegeta"]
print(f"Scouter detecta {len(enemigos)} objetivos. Iniciando escaneo de largo alcance (Salto 2)...")

#range(inicio, fin, salto)
for i in range(0, len(enemigos), 3):
    print(f"Posición {i}: {enemigos[i]} ANALIZADO.")

print("Escaneo parcial terminado,Shogun.")

