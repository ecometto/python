#EJERCICIOS DICCIONARIOS:
#1- crear funcion para contar de una lista dada, la cantidad de veces que se repiten las palabras dentro de la lista. Mostrar resultado a traves de un diccionario.

def contarRepetidos(lista):
    palabras=dict()
    for palabra in lista:
        if palabra not in palabras:
            palabras[palabra] = 1
        else:
            palabras[palabra] +=1
    return palabras

colores=["rojo", "verde", "rojo", "negro", "azul", "verde", "amarillo", "marron", "marron", "rojo"]
print(sorted(contarRepetidos(colores)))
#(el ordenamiento por defecto es POR CLAVE. y muestra solo la clave)

#ordenando por CLAVE y mostrando ambos (clave y valor) se agrega .items()
print("--------")
print(sorted(contarRepetidos(colores).items(), reverse=True))

# si se quiere pordenar POR VALOR mostrando ambos, entonces se debe importar MODULO OPERATOR.
import operator
print("--------")
print(sorted(contarRepetidos(colores).items(), reverse=True, key=operator.itemgetter(1)))


#2- crear funcion para contar la repeticion de letras dentro de un strig solicitado al usuario. Mostrar resultado a traves de un diccionario.
def contarLetras():
    # string = input("ingrese el string a evaluar: ").lower()
    string = "alguna cadena de pruebaiii"
    dictResultado = dict()
    for ch in string:
        if ch == " ":
            continue
        if ch not in dictResultado:
            dictResultado[ch] = 1
        else:
            dictResultado[ch] += 1
    return dictResultado

print("--------")
ordenado2=sorted(contarLetras().items(), reverse=True , key=operator.itemgetter(1))

for i in ordenado2:
    print(i)


# #3 - leer un archivo .txt y crear una fucnion para contar todas las palabras que tiene, indicando la cuantas veces se repiten las mismas.
archivo="./repaso/file1.txt"
file= open(archivo,"r", encoding="utf8")
myT = file.read() # texto completo STR
file.seek(0)
myTLines = file.readlines() #texto en lista
file.close()

lines3=[]
lines2=myT.split('\n')
for each in lines2:
    if each != "":
        lines3.append(each)
cuenta=0
for n in lines3:
    cuenta+=len(n.split())
    # print(len(n))
print(cuenta)

i=1
total=0
for line in myTLines:
#    print(line.split())
#    print(len(line.split()))
   total+=len(line.split())
print(total)


def contarPalabras(text):
    return len(text.split())

print("--------")
print(contarPalabras(myT))


print("--------")
# # using regex findall()
import re
texto="esto es uN texto de Prueba"
data=re.findall("\w+",texto)
print(data)
print(len(data))
print(type(data))



# #buscando espacios en blanco con REGEX . Se debe importar el modulo RE
# import re
# text = 'Python, the be1st programming language'

# # using regex findall()
# result = len(re.findall(r'\w+', text))

# print("There are " + str(result) + " words.")