# Lista de actualización para la laptop de mi hermana
# Incluye: Componente (String), Precio aprox (Float) y Prioridad (Int)

componentes_acer = ["SSD NVMe 500GB", "RAM 8GB DDR4", "Pasta Térmica MX-4", "Monitor Externo"]

# 1. Agreguemos el precio de la RAM al final
componentes_acer.append(25.99) 

# 2. Vamos a ver si el SSD está en la lista
print("¿Está el SSD en la lista?:", "SSD NVMe 500GB" in componentes_acer)

# 3. ¿En qué posición quedó el monitor?
print("El monitor está en el índice:", componentes_acer.index("Monitor Externo"))

# 4. Imprimamos todo el inventario
print("Inventario final de rescate:", componentes_acer[:])