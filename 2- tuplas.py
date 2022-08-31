# las TUPLAS van entre paréntesis, o sin paréntisis. Para tuplas de 1 solo elemento, se debe colocar la "coma" antes de cerrar el paréntesis
mitupla = ("yo", "otro", 155)

print (mitupla	[:])

# LIST - convierte tupla en lista
milista = list(mitupla)
print(milista)

# TUPLE - convierte lista en tupla
nuevalista = ["hola", "jajajaj", 115]
nuevatupla = tuple (nuevalista)
print (nuevatupla)

# IN - busca dentro de la tupla (o de una lista) y devuelve true o false
print("hola" in nuevatupla)

# COUNT -  cuenta la cantidad de veces que aparece el elementos
print (nuevatupla.count("hola"))


# LEN - devuelve "cantidad" de elementos en una tupla
print(len(nuevatupla))