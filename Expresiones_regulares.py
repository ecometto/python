# EXPRESIONES PARA REALIZAR BUSQUEDAS
import re
texto = "bienvenidos al curso de python. esta es nuestra primera clase de python"

#search busca y muestra la primer posicion del primero que encuentra y devuelve desde donde hasta donde
texto_a_buscar = "bien"
busqueda = re.search(texto_a_buscar, texto)
if not busqueda is None:
    print("el texto fue encontrado en la posicion", busqueda.start(), " y termina en la posicion: ", busqueda.end())
    print("lo que seria lo mismo que decir que el texto fue encontrado en: ", busqueda.span())
else:
    print("no existe")

print("*" * 20)

#busca todos los resultados y los muestra.
texto_buscado1 = "python"
busqueda1 = re.findall(texto_buscado1, texto)
print("se ha encontrado la palabra ", texto_buscado1, " y se ha encontrado ", len(busqueda1), " veces.")
print("*"*20)

#crea una lista separando las palabras en el criterio indicado (puede ser un espacio, una letra o lo que sea),
# al cual reemplaza con una coma. El 3er. criterio limita la cantidad de elementos del resultado (puede obviarse).
busqueda2 = re.split("e",texto, 4)

# sub reemplaza o "sustituye"  el argumento por lo indicado
busqueda3 = re.sub(" ","-",texto)


texto2 = "hola123. Esto es un curdo con numeros 78532"

#METACARACTERES
#Algunos "filtros".
# "\A" lo encuentra solo si esta en la primer posicion.
# "\d" encuentra el primer caracter numerico

print(busqueda2)
print("*"*20)

print(busqueda3)
print("*"*20)
