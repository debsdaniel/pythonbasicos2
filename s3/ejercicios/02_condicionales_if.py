# Si la compra es mayor  1500 el descuento 15%
# si la compra es mayor 800 el descuento 10%
# si la compra es mayor a 300 descuento 5%
# si la compra es menor a 300 descuento es 0%

compra = float(input("Ingrese el monto de su compra: "))
descuento = 0
porcentaje=0

if compra >= 1500:
    descuento = 0.15
    mensaje = "Descuento del 15%"
elif compra >= 800:
    descuento = 0.10
    mensaje = "Descuento del 10%"
elif compra >= 300:
    descuento = 0.05
    mensaje = "Descuento del 5%"
else:
    descuento = 0
    mensaje = "No hay descuento"

total_descuento = compra * descuento
total_pagar = compra - total_descuento

print("\n===== SUPERMERCADO =====")
print(mensaje)
print(f"Compra: C$ {compra:.2f}")
print(f"Descuento: C$ {total_descuento:.2f}")
print(f"Total a pagar: C$ {total_pagar:.2f}")