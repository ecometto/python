###############DECORADORES ############## ("decoran" o mejoran una funcion)
def decoradora(funcionParametro):  #ejecutada al final
    '''esta funcion "decoradora" lo que hace es realizar un agregado a las funciones.
    la forma de llamarla es agregando un "@" antes de la funcion que queremos realizar el agregado'''
    
    def funcionResultado(*args):
        print("*"*10, "\n Se ejecutará una funcion: ")
        funcionParametro(*args)
        print("funcion ejecutada con exito", "*" * 5)

    return funcionResultado




def funcionPar(num):
    if num %2 == 0:
        return num

listanumeros=[2,3,5,8,6,9,4,7,52,1,3,5,4,7]
print(list(filter(funcionPar,listanumeros))) #usa la funcion para filtrar lista "listanumeros"

print(list(filter(lambda num: num%2 == 0 , range(0,20)))) # esta es otra forma usando funcion lambda

print("******************************")

class Empleado():       #se crea una clase "empleado" para hacer una lista "listaempleados" con los datos indicados en la Clase.
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo=cargo
        self.salario = salario

    def __str__(self):      #este constructor devuelve una cadena de texto. Hay que indicar las variables con Llaves y format.(self.nnn)
        return "El empleado{} que ocupa el cargo de {}, cobra un salario de {}." .format(self.nombre, self.cargo, self.salario)

listaempleados = [Empleado("juan", "director", 25000), Empleado("roberto","director",27000),
                  Empleado("ana", "administracion",2100), Empleado("juanita","porteria",1800)]

salariosAltos=filter(lambda x: x.salario>2200, listaempleados) # a la funcion lambda se le pasan 2 parametros. La funcion con el criterio, y la lista
for n in salariosAltos:
    print(n)
print("******************************")

######################## MAP #####################################
def comisiones(x):
    if x.salario < 2200:
        x.salario = x.salario * 1.1
    return x

listacomisiones = map(comisiones, listaempleados) #"map" aplica una funcion (lambda) a una lista (listaempleados).
for x in listacomisiones:
    print(x)

######################## EXPRESIONES REGULARES (find, findall, search, match) #####################################
print("******************************")
import re

texto = "vamos a aprender Python. Python es un programa de programacion orienteado a objetos"
textoBuscado = "Python"
textoEncontrado = re.search(textoBuscado, texto)

#la busqueda discrimina mayusculas y minusculas.. ver lineas 55 en adelante para salvar este tema
if re.search(textoBuscado, texto) != None:          #si encuentra el texto devuelve un objeto. Si no lo encentra devuelve "None"
    print("texto encontrado en la posicion", textoEncontrado.start(), "y finaliza en la posicion: ", textoEncontrado.end())
    print("la extension del texto es: ", textoEncontrado.span())
else:
    print("texto no encontrado")

print("la cantidad de palabras es: ", len(re.findall(textoBuscado, texto)))
#findall devuelve una lista con la palabra buscada, tantas veces como aparezca.)

listanombres= ["Juan castro", "jose perez", "raul Martinez", "ricardo peres", "jose martinez", "ricardo rajonte"]

for nombre in listanombres:
    if re.findall("^j", nombre): #el simbolo ^indica que empiezan con ese texto
        print("el/los nombresque empiezan con 'j' son: ", nombre)

for nombre in listanombres:
    if re.findall("ez$", nombre): #el simbolo $ al final indica que busca los valores que terminen con ese texto
        print("el/los nombres terminados en 'ez' son: ", nombre)

for nombre in listanombres:
    if re.findall("[Mm]artinez$", nombre): #el simbolo entre corchetes indica que puede ser cualquiera de esos valores
        print("el/los nombres que contienen J o j son: ", nombre)

for nombre in listanombres:
    if re.findall("[Pp]ere[sz]", nombre): #el simbolo entre corchetes indica que puede ser cualquiera de esos valores
        print("el/los apellidados Perez/s son: ", nombre)

for nombre in listanombres:
    if re.findall("^[aA-mM]", nombre): #el simbolo entre corchetes indica el rango que pueden empezar la palabras (incluye mayuscula y minuscula)
        print("el/los nombres que empiezan entre a y c son: ", nombre)


# match y Search ############## (devuelven True o False)
print("******************************")

for nombre in listanombres:         #la expresion match busca al principio de una variable o lista, la funcion search busca en cualquier lugar
    if re.match("j", nombre):
        print("exite el nombre que empieza con J")

cont=0
Varmail = "hkjhgka00000fjvhaudfvhfdauvhafduvjf@dahvkdfhv@gfghdfhgdfg.com.ar"

if re.search("@", Varmail):
   print ("contiene arroba")

for nombre in listanombres:
    if re.search("[Pp]ere[sz]", nombre): #la expresion match busca al principio de una variable o lista, la funcion search busca en cualquier lugar
        print("el/los apellidados Perez/s son: ", nombre)

@decoradora
def calculoHipotenusa():
    '''Esta funcion calcula la hipoptenusa de un triangulo rectangulo.
    Lo realiza a traves del ingreso de 2 parametros (cada uno de los catetos)'''

    cat1 = int(input("ingrese valor para la cat1: "))
    cat2 = int(input("ingrese valor para la cat2: "))
    hipotenusa = (cat1**2 + cat2**2)**0.5
    print("el valor de la hipotenusa es:", hipotenusa)

calculoHipotenusa()

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