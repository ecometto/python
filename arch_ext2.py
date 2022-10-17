import io

#IMPORTANTE.. Cuando lee o escribe, el cursor queda al final.. y desde ahí realiza la accion siguiente.
# open type "w" is for writing (overWrite) or create  the file if it does not exist.
 # open type "a" is for "append" content at the end of the file. (not red)
 # open type "r" is for read (only read) the. 
 # open type r+ allows read and write info. But be carefull it write from the begining of the file (not at the end)
 #readlines para leer por línea (parrafo) y lo guarda como array

archivoEnMemoria = io.open("archivo1.txt","r+")

array = archivoEnMemoria.readlines()
print(array)
array.insert(4, "quinto este texto nuevo en \n")
text = "".join(array)

archivoEnMemoria.close()

archivoEnMemoria = io.open("archivo1.txt","w")

# archivoEnMemoria.seek(0)
archivoEnMemoria.write(text)

# print(len(archivoEnMemoria.read()))
# archivoEnMemoria.seek(0)


# fraseAIncluir = "nueva3\n"
# archivoEnMemoria.write(fraseAIncluir)

# text = archivoEnMemoria.readlines()
# print(text[0])
# print(len(text))



archivoEnMemoria.close()