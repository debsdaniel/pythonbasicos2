factura = {
    "nombre": "Cuaderno",
    "precio": 45.00,
    "cantidad": 12,
    "descuento": True
}

#Producto: Cuaderno
#Precio: 45.00
#Cantidad: 12
#Descuento: No Aplica  
#            Si Aplica

n = factura["nombre"]
p = factura["precio"]
c = factura["cantidad"]
descuento = factura["descuento"]

print(f"Producto: {n}")
print(f"Precio: {p}")
print(f"Cantidad: {c}")
if descuento:
    print("Descuento: Si Aplica")
else:
    print("Descuento: NO Aplica")
