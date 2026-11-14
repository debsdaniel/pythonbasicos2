pin_correcto = "1234"
intentos = 0

while intentos < 3:
    pin = input("Ingrese su PIN: ")

    if pin == pin_correcto:
        print("Acceso autorizado.")
        break

    intentos += 1
    #intentos = intentos + 1

    print("PIN incorrecto.")

    if intentos < 3:
        print(f"Intentos restantes: {3 - intentos}")

    if intentos == 3:
        continuar = input("Continuar? (s/n): ").lower()
        if continuar == "s":
            intentos = 0

if intentos == 3:
    print("Usuario bloqueado.")