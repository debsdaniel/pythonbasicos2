productos1 = ["Arroz", "Frijoles", "Leche", "Aceite", "Azúcar"]
#print(productos1)
productos2 = []
#print(productos2)

precios = [45, 35, 20, 78]

print(productos1[0])
print(productos1[1])
print(productos1[3])
print(productos1[4])
print("******************")
print(productos1[-1])
print(productos1[-2])
print("******************Cambiar Valor***********")

print(productos1)
productos1[0] = "Frijoles Rojo"
#print(productos1[0])
print(productos1)

print("******************Tamaño de Lista***********")
print(len(productos1))
print("******************Sobre Indice ***********")
print(productos1[-4])
print(productos1[-5])
#print(productos1[-6])

print("******************Validar  Indice ***********")
cnt = len(productos1)
for i in range(0,50):
    if i >= 0 and i < cnt:
        print(productos1[i])
    else:
        print(f"Índice {i} no existe en la lista")