# los DICCIONARIOS van entre llaves. Se completan "pares" para formar Clave-valor

midiccionario = {"Alemania":"berlin", "españa":"madrid", "francia":"paris"}

#permite agregar elemento con el siguiente formato
midiccionario ["italia"] = "lisboa"


print (midiccionario["Alemania"])
print(midiccionario["francia"])
print (midiccionario)

# para modificar (sobreescribir) el valor, se procede de la siguiente manera

midiccionario ["italia"] = "roma"

print (midiccionario)

# para ELIMINAR un elemento se usa DEL
del midiccionario ["españa"]

print (midiccionario)

# para otros tipos de datos se usa de la siguiente forma
midiccionario1 = {"messi":1, "maradona":2, "otros": "no existen"}

print (midiccionario1)

# para asignarle uma TUPLA  a cada una de las claves del DICCIONARIO entonces
mitupla = ("argentina", "brasil", "uruguay")
midiccionario2 = {mitupla[0]:"BsAs", mitupla[1]:"brasilia", mitupla[2]:"muntevideo"}

print (midiccionario2)

# para asignarle una TUPLA con varios valores a uno de los elementos del DICCIONARIO
midiccionario3 = {"hola":1, "hola2":2, "hola3":3, "holatodos":[1,2,3,4,5,6]}
print (midiccionario3)
print (midiccionario3 ["holatodos"])





