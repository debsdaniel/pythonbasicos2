#edad=25
#print(edad < 18)
#Si la compra es mayor a C$100 aplicar descuento

monto = float(input("Ingrese el monto de su compra: "))
limite = 1000
porcentaje = 10
descuento = 0

if monto >= limite:
    descuento = monto * porcentaje / 100

total = monto - descuento

print(total)


