from io import *
'''
# definir el nombre que se utilizara internamente (en memoria) para trabajar con el archivo
# en caso que el archivo no exista, con la siguiente linea se "crea"

miArchivo = open("archivo.txt", "w")        #el segundo argumento "W" indica "escritura"
frase = "estupendo dia para estudiar Python. \nHoy es jueves por suerte"
miArchivo.write(frase)
miArchivo.close() # esta linea cierra el archivo "en memoria" de python
'''

'''
elmismoArchivo = open("archivo.txt", "r")        #el segundo argumento "r" indica "lectura" ("a" indica leer y permitir adicionar texto)
#texto = elmismoArchivo.read()
textoLista = elmismoArchivo.readlines()
elmismoArchivo.close()
#print(texto)
print(textoLista)
print(textoLista[0])
'''

'''
#para agregar texto al final
miArchivo = open("archivo.txt","a")              #el segundo argumento "a" indica "anadir"
miArchivo.write("\nOtra nueva prueba para realizar")
miArchivo.close()
'''
'''
miArchivo = open("archivo.txt","r")
texto = miArchivo.read()
print(texto)
'''

'''
miArchivo = open("archivo.txt","r+") #lectura y escritura
texto = miArchivo.read()
miArchivo.seek(0)               # SEEK ES EL PUNTERO, La POSICION DONDE SE UBICARA EL CURSOR
texto1 = miArchivo.read(15)     # define hasta donde leera
miArchivo.seek(0)
miArchivo.seek(len(miArchivo.readline()))   #lo posiciona luego de finalizar la lectura del primer parrafo (readLINE)
segundoParrafo = miArchivo.read()
print("----------------------")
print(texto)
print("----------------------")
print(texto1)
print("----------------------")
print(segundoParrafo)
print("----------------------")
miArchivo.seek(0)
miArchivo.write("Este sera el primer parafo \n")
miArchivo.seek(0)

listatexto= miArchivo.readlines()
#del(listatexto[4,5])
print(listatexto)

miArchivo.close()'''

#CORTARLE PARRAFOS AL ARCHIVO
''' archivo = open("archivo.txt","r+")
print(archivo.read())
print("-------------")
archivo.seek(0)
lineas = archivo.readlines()
lineasutiles = [lineas[2], lineas[3]]
print("-------------")
print(lineasutiles)

archivo.seek(0)
archivo.truncate()
archivo.seek(0)
archivo.writelines(lineasutiles)
archivo.seek(0)
print(archivo.read())

archivo.close '''


''' # PERMITE LEER y/o EXTRAE POR PARRAFO EN PARTICULAR
archivo = open("archivo.txt","r+")
print(archivo.read())
archivo.seek(0)
lineas = archivo.readlines()
utiles = (0,3)
listaNueva = []
for i in range(0,len(lineas)):
    if i in utiles:
        listaNueva.append(lineas[i])
print(listaNueva)
archivo.seek(0)
archivo.truncate()
archivo.writelines(listaNueva)
archivo.seek(0)
print(archivo.read())

archivo.close()'''

# # ESCRIBIR UNAS LINEAS AL PRINCIPIO SIN SOBREESCRIBIR TEXTO

# archivo = open("archivo.txt", "+r")
# textoAAgregar = "este sera el primer parrafo.\n"
# textoActual = archivo.read()
# print(textoActual)
# archivo.seek(0)
# archivo.write(textoAAgregar + textoActual) 
# archivo.write("")
# archivo.seek(0)
# print(archivo.read())
# archivo.close()

archivo = open("archivo.txt,r")


