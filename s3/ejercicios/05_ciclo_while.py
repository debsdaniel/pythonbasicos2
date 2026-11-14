contador = 4

while contador <= 5:
    print(f"Paso número {contador}")

    contador = contador + 1


print("================================")

meta = 500
ahorrado = 0

while ahorrado < meta:

    aporte = float(input("¿Cuánto desea ahorrar?: "))

    if aporte <= 0:
        print("El aporte debe ser mayor que cero.")
        continue

    ahorrado += aporte

    print(f"Total ahorrado: C$ {ahorrado:.2f}")

print("¡Felicidades! Has alcanzado tu meta.")