

# # funcion básica 
# def participantes(profesor, ayudante):
# 	print("el profesor es: {} y el ayudante es:  {} ".format(profesor,ayudante))

# participantes("Sr. Logan", "Sra Mc.Galigan")


# # concatenar variables con string 
# nombre = "ceci"
# edad = 18
# print ("tu nombre es: {} y tu edad {}".format(nombre,edad))
# print(f"hola{nombre}, como estas con tus {edad} años?")


# # funcion basica de calculadora  -"importando modulos"
# import modulos as m

# operaciones = dir(m)
# print (operaciones) # para ver las operaciones y metodos propios que contiene ese modulo

# def calculadora():
#     resultado = 0
#     operacion = int(input("ingrese numero de operacion (1=suma, 2=resta, 3=multiplicacion, 4=division ):"))
#     num1 = int(input("ingrese el primer numero "))
#     num2 = int(input("ingrese el segundio numero "))
#     if operacion == 1:
#         resultado =  m.sumar(num1, num2)
#     elif operacion == 2:
#         resultado = m.restar(num1, num2)
#     elif operacion == 3:
#         resultado = m.multiplicar(num1, num2)
#     elif operacion == 4:
#         resultado = m.dividir(num1, num2)
        
#     print("El resultado es: ", resultado)
    
# calculadora()


# transformar numero a texto con funcion y diccionario (objeto) 
numeros = {
    "1" : "uno",
    "2" : "dos",
    "3" : "tres",
    "4" : "cuatro",
    "5" : "cinco",
    "6" : "seis",
    "7" : "siete",
    "8" : "ocho",
    "9" : "nueve"
}

def transformarNumero ():
    # num = input("ingrese un numero del 0 al 9 - ")
    # for n in num:
        # textoNum += numeros[n] + ' ' 
    # print ("El numero ingresado, en letras es: " + textoNum)
    
    #print("el numero ingresado es ", numeros[num])
    for numero in numeros.items():
        print(numero[0] , " - " , numero[1])
    print("------------------------------")
    for cada in numeros.keys():
        print(cada , " - " , numeros[cada])    
    
transformarNumero ()