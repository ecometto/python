# EXPRESIONES PARA REALIZAR BUSQUEDAS
from datetime import datetime
import re

def separar():
    print("-" * 20)

texto = "bienvenidos al curso de python. esta es nuestra primera clase de python"

#SEARCH
#search busca y muestra la primer posicion del primero que encuentra y devuelve desde donde hasta donde
texto_a_buscar = "bien"
busqueda = re.search(texto_a_buscar, texto)
if not busqueda is None: #también se puede validar así: 'if re.search(textoBuscado, texto) != None:' 
    print(busqueda)
    print(f"SEARCH: el texto '{busqueda.group()}' fue encontrado en la posicion", busqueda.span()[0], " y termina en la posicion: ", busqueda.span()[1])
else:
    print("no existe")

separar()

#FINDALL
#findall busca todos los resultados y los muestra.
texto_buscado1 = "python"
busqueda1 = re.findall(texto_buscado1, texto)
print("FINDALL: se ha encontrado la palabra ", texto_buscado1, " y se ha encontrado ", len(busqueda1), " veces.")
separar()


#SPLIT
now = datetime.now()
nowStr=datetime.strftime(now, "%Y-%m-%d %H:%M:%S")
#Split crea una lista separando las palabras en el criterio indicado (puede ser un espacio, una letra o lo que sea),
# al cual reemplaza con una coma. El 3er. criterio limita la cantidad de elementos del resultado (puede obviarse).
busqueda2 = re.split(" ", nowStr)
print(f"fecha: {busqueda2[0]} - hora: {busqueda2[1]}")
separar()


# sub reemplaza o "sustituye"  el argumento por lo indicado
texto2 = "SUB: hola123. Esto es una prueba de SUB que sustituye caracteres/cadenas"
busqueda3 = re.sub(" ","-",texto2)
print(busqueda3)
separar()

# --------------------------------------------- 

listanombres= ["Juan castro", "jose perez", "raul Martinez", "ricardo peres", "javier martinez", "ricardo rajonte"]

empiezaJ=[]
for nombre in listanombres:
    if re.findall("^j", nombre): #el simbolo ^indica que empiezan con ese texto
        empiezaJ.append(nombre)
if len(empiezaJ)>0:
    print("los nombresque empiezan con 'j' son: ", empiezaJ)

terminaMmartinez=[]
for nombre in listanombres:
    if re.findall("[Mm]artinez$", nombre): #el simbolo entre corchetes indica que puede ser cualquiera de esos valores
        terminaMmartinez.append(nombre)
if len(terminaMmartinez)>0:
    print("los nombresque termina 'Mm'artinez son: ", terminaMmartinez)

entreAyM=[]
for nombre in listanombres:
    if re.findall("^[aA-mM]", nombre): #el simbolo entre corchetes indica el rango que pueden empezar la palabras (incluye mayuscula y minuscula)
        entreAyM.append(nombre)
if len(entreAyM)>0:
    print("los nombres entre A y M' son: ", entreAyM)

separar()



Varmail = "hkjhgka00000fjvhaudfvhfdauvhafduvjf@dahvkdfhv@gfghdfhgdfg.com.ar"
if re.search("@", Varmail):
   print ("contiene arroba")

for nombre in listanombres:
    if re.search("[Pp]ere[sz]", nombre): #la expresion match busca al principio de una variable o lista, la funcion search busca en cualquier lugar
        print("el/los apellidados Perez/s son: ", nombre)



mailusuario=input("ingrese un mail")
contarArrobas=mailusuario.count("@")

if contarArrobas >1:
    print("error. La cantidad de arrobas no puede ser distinta de 1. Ud ha ingresado ", contarArrobas)
    print("la cantidad de puntos es", mailusuario.count(".") )
else:
    print("mail ingresado correctamente")
    print("la cantidad de puntos es", mailusuario.count("."))
print (mailusuario.find("@"))
print(mailusuario.find("@"), len(mailusuario))
print("error")