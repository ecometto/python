
def presentar(argumento, otro):
	print("hola", argumento, "....\nTu tienes", otro, "agnos")

presentar("papa", 36)


def participantes(profesor, ayudante):
	print("el profesor es: {} y el ayudante es:  {} ".format(profesor,ayudante))


participantes("Sr. Logan", "Sra Mc.Galigan")

nombre = "ceci"
edad = 18

print ("tu nombre es: {} y tu edad {}".format(nombre,edad))

print("hola{}, como estas con tus {} a;os?".format(nombre,edad))

# otra funcion -----------------
def calculadora(num1, num2):
    resultado1 = 0
    operacion = int(input("ingrese: 1-Suma, 2-Resta, 3-Multiplicacion, 4-Division: "))
    if operacion == 1:
        resultado1 = num1 + num2
    elif operacion == 2:
        resultado1 = num1 - num2
    elif operacion == 3:
        resultado1 = num1 * num2
    elif operacion == 4:
        resultado1 = num1 / num2
    print("el resultado es: ", resultado1)
    return resultado1

calculadora(8, 4)