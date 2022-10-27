# String
print("Este es un curso de Python." + "\nBienvenidos")

#listas
smartphones=["huawei", "samsung", "motorola", "iphone", "xiaomi"]
print(smartphones)

# se puede acceder con indice negativo (los indices van de 0 a n)
print("los smartphones elegidos son: ", smartphones[1], smartphones[-1])

del smartphones[2]
print(smartphones)

smartphones.remove("huawei")

print(smartphones)

#para eliminar y guardar lo eliminado, se usa POP, guardando en una variable
nombres = ["maria", "jose", "juan", "miguel", "raul", "roberto"]
nombreseliminados = [nombres.pop(0), nombres.pop(1)]
nombres.append("jazmin")
nombres.insert(-1,"norberto")
print (nombres)
print ("el color eliminado fue: ", nombreseliminados)

#sort para ordenar en forma definitiva la list
nombres.sort(reverse = True)
print(nombres)

#si solo quiero imprimir ordenado, sin modificar osiciones, se usa sorted
print(sorted(nombres))

print("la cantidad de elementos en 'nombres' es de: ", len(nombres))

# para generar una tupla en lista y viceversa e usa "tuple" o "list"
tuplanombres = tuple(nombres)
print(tuplanombres)

#para verificar si existe en lista o tupla
if "raul" in tuplanombres:
	print("existe en la lista")
else:
	print("no existe en la lista")

#DICCIONARIOS las comas separan los items. Los "dos puntos" separan entre si
#para los diccionarios tambien aplican len, pop, del (cuidado que puede eliminar todo)

midiccionario = {"cateoria": "teclado",	"nombre": "tec KMV genios 54t",	"precio": 100}

midiccionario1 = {
	"Alemania": "Berlin",
	"Argentina": "Buenos Aires",
	"Uruguay": "Montevideo",
	"Francia":"Paris",
	"Brasl":"Brasilia"
}

consulta = midiccionario["nombre"], "tiene un precio de", midiccionario["precio"]
print("el teclado", consulta)

print("la capital de Argentina es:", midiccionario1["Argentina"])

consultadicc = dict(midiccionario1)
print(consultadicc)
print(midiccionario1)

midiccionario["precio"] = "199"
print(midiccionario)

for x in midiccionario:
	print(x)

print("*************")

for x in midiccionario:
	print(midiccionario[x])
# otra opcion para el renglon aterior seria con .values
print("*************")

for x in midiccionario.values():
	print(x)
print("*************")

for x,y in midiccionario1.items():
	print("La capital de:",x,":"), print(" ", y)

#Si queremos ordenar por la clave o por el valor 

import operator 
resultadoOrd = sorted(midiccionario1.items(), key=operator.itemgetter(0))
resultadoOrd1 = sorted(midiccionario1.items(), key=operator.itemgetter(1))
print(resultadoOrd)
print(resultadoOrd1)

print(sorted(midiccionario1))
print(sorted(midiccionario1.values()))


#for key in sorted(midiccionario1):
#   print (":" % (key, midiccionario1[key]))
'''y no por la clave, basta con usar el argumento key de sorted:

import operator

valores = {5: 20000, 3: 90000, 4: 15000} 
valores_ord = dict(sorted(valores.items(), key=operator.itemgetter(1)))
print(valores_ord)  # {4: 15000, 5: 20000, 3: 90000}
'''

