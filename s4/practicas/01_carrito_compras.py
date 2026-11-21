carrito = [
    "Arroz",
    "Frijoles",
    "Aceite",
    "Azucar",
    "Cafe"
]

# Agregar un producto al final.
carrito.append("Leche")

# Insertar Sal en la segunda posición.
carrito.insert(1, "Sal")

# Eliminar Aceite.
carrito.remove("Aceite")

# Retirar el último producto.
producto_retirado = carrito.pop()

print("Producto retirado:", producto_retirado)

# Ordenar el carrito.
carrito.sort()

print("\n===== CARRITO DE COMPRAS =====")

print("Todos los productos:", carrito)

print("Primeros tres:", carrito[:3])

print("Últimos dos:", carrito[-2:])

# RETO EXTRA: agregar varios productos utilizando extend().
carrito.extend(["Pan", "Huevos"])

carrito.sort()

print("\n===== CARRITO ACTUALIZADO =====")
print(carrito)