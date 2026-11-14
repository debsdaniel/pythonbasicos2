edad = int(input("Ingrese su edad: "))

if edad <= 0:
    print("Edad inválida. No se puede realizar la compra.")

else:
    if edad < 12:
        categoria = "Niño"
        precio = 50
    elif edad <= 17:
        categoria = "Joven"
        precio = 80
    elif edad <= 64:
        categoria = "Adulto"
        precio = 120
    else:
        categoria = "Adulto mayor"
        precio = 70

    codigo = input("¿Tiene código promocional? (s/n): ").lower()

    if codigo == "s":
        descuento = precio * 0.10

    else:
        descuento = 0

    total = precio - descuento

    print("\n===== FESTIVAL =====\n")
    print(f"Categoría: {categoria}")
    print(f"Precio original: C$ {precio:.2f}")
    print(f"Descuento: C$ {descuento:.2f}")
    print(f"Total a pagar: C$ {total:.2f}")