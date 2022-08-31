lista = ["maria", 5,"marta", 8.8]

print (lista[1])
print (lista[0:2])

# inserta al final de la lista
lista.append ("juanjo")
print (lista [:])

# inserta en un lugar determinado de la lista
lista.insert (2, "ruben")
print (lista [:])

# agregar varios elementos a la lista 
lista.extend (["bicho", "loco", "otro"])

print (lista [:])

nombre = input("ingresa un nombre: ")

# indica la ubicación dentro de la lista (1º posición = 0)
print (nombre, " está en el lugar: ", lista.index("juanjo"))

# para buscar si está o no en la lista
print ("pepe" in lista)

# elimina un elemento de la lista
lista.remove ("bicho")
print (lista [:])

# elimina EL ÚLTIMO elemento de la lista
lista.pop ()
print (lista [:])

#unir listas (concatenar listas)

lista1 = ["jota", "nacho"]

lista3 = lista + lista1

print (lista3)

# multiplica las listas
lista4 = ["maria", 5,"marta", 8.8] * 3
print (lista4)

