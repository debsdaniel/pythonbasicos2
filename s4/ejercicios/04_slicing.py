#Sintaxis:  lista[inicio:fin]

productos = ["Arroz", "Frijoles", "Leche", "Aceite", "Azúcar", "Café"]
print(productos)
# Tomar los elementos del 1 al 3
print(productos[1:4])

#Primero tres elementos
print(productos[:3])

#Obtener elemetno desde una posicion hasta el final
print(productos[2:])

#Obtener dos últimos elemento
print(productos[-2:])

#Obtener uno de cada dos elemetnos
print(productos[::2])

#Invertir el orden de una lit
print(productos[::-1])

### Agregar Elementos
###### Uso de metodo append()
print("************ Agregar Elementos ***********")
productos = ["Arroz", "Frijoles", "Leche"]
print(productos)
productos.append("Aceite")
print(productos)

### Agregar Varios Elementos
##### extend

productos.extend(["Azúcar", "Café","Agua"])
print(productos)

prod2 = ["Galletas", "Chocolates"]

productos.extend(prod2)
print(productos)

### Insertar en una posición específica
#### insert
print("************ Insertar Elementos ***********")
productos = ["Arroz", "Frijoles", "Leche"]
print(productos)
productos.insert(1,"Aceite")
print(productos)

####Eliminar Valores
##### remove()

productos.remove("Aceite")
print(productos)

print("************ Eliminar Aceite ***********")
productos.insert(1,"Aceite")
productos.append("Aceite")
print(productos)
productos.remove("Aceite")
print(productos)

print("************ Borrar Por Posición ***********")
#### Pop
productos = ["Arroz", "Frijoles", "Leche"]
print(productos)

eliminado = productos.pop(1)
print("Producto Eliminado: ", eliminado)
print("Lista Actual: ", productos)

productos.pop()
print(productos)

print("Ordenar Lista")
precios = [350,232,129,80,300]
print(precios)
precios.sort()
print(precios)
precios.sort(reverse=True)
print(precios)

print("******** sorted *******")
precios = [350,232,129,80,300]
precios_ordenados = sorted(precios)
print(precios)
print(precios_ordenados)