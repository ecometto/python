lista = ["maRia", "peDrito", "marta", "Anita"]

print(lista[1])
print(lista[0:2])

# inserta al final de la lista
lista.append("juanjo")
print(f"Agregado el ultimp? {lista}")

# inserta en un lugar determinado de la lista
lista.insert(2, "ruben")
print(lista[:])

# agregar varios elementos a la lista
lista.extend(["bicho", "loco", "otro"])

print(f"agregando varios más con metodo \"extend\": -- {lista}")

nombre = input("ingresa el nombre de la lista a buscar: ")
# pasa todo a minuscula e indica la ubicación dentro de la lista (1º posición = 0)

pos=""
for i in range (0, len(lista)):
    lista[i] = lista[i].lower()
    try:
        pos=lista.index(nombre.lower())
        break
    except:
        continue
if pos == "":
    print("no se encontró el nombre indicado")
else:   
    print(f"se encontro el nombre {nombre} en la posicion {pos + 1}")
    
print(lista)

print("---------------------------")

# para buscar si está o no en la lista (devuelve True o False)
print(f"{'pepe' in lista} - {'maria' in lista}")

# elimina un elemento de la lista
lista.remove("bicho")
print("lista con 'bischo' eliminado ", lista[:])

# elimina EL ÚLTIMO elemento de la lista
eliminado = lista.pop()
print(f"Lista con '{eliminado}' eliminado: {lista [:]}")

# unir listas (concatenar listas)

lista1 = ["jota", "nacho"]

lista3 = lista + lista1

print("lista 3: ", lista3)

# multiplica las listas
lista4 = ["Maria", 5, 10, "Marta", 8.8] * 3
print(lista4)

def toUP(x):
    if not isinstance(x, str):
        return x
    else:
        return x.upper()

nombre4=input("ingrese el nombre a buscar: ")
l4=list(map(toUP, lista4))
pos=l4.index(nombre4.upper())
print(f"el nombre {nombre4.upper()} está en la posición {pos}")
print(l4)

for item in l4:
    if isinstance(item, int) or isinstance(item, float):
        print(item)