###############DECORADORES ############## ("decoran" o mejoran una funcion)
def decoradora(funcionParametro):  #ejecutada al final
    '''esta funcion "decoradora" lo que hace es realizar un agregado a las funciones.
    la forma de llamarla es agregando un "@" antes de la funcion que queremos realizar el agregado'''
    
    def funcionResultado(*args):
        print("\nAqui empieza la funcion 'decoradora':\n", "*"*10, "\n Se ejecutará una funcion: ")
        funcionParametro(*args)
        print("funcion ejecutada con exito\n", "*" * 5, "\nAqui termina la funcion 'decoradora'\n")

    return funcionResultado


# EJEMPLO (se incluye decoradora y a continuación se define la funcion a "complementar")
@decoradora
def calculoHipotenusa():
    '''Esta funcion calcula la hipoptenusa de un triangulo rectangulo.
    Lo realiza a traves del ingreso de 2 parametros (cada uno de los catetos)'''

    cat1 = int(input("ingrese valor para el cateto1: "))
    cat2 = int(input("ingrese valor para el cateto2: "))
    hipotenusa = (cat1**2 + cat2**2)**0.5
    print("el valor de la hipotenusa es:", hipotenusa)

calculoHipotenusa()


def funcionPar(num):
    if num %2 == 0:
        return num


# ****************** FILTER Y MAP ********************* 
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