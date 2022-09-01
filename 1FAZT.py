#para correr archivo ALT + F5
#imprimiendo en consola

#LISTAS = ARRAY JS
#DICCIONARIOS = OBJETOS JS
# CON LA FUNCION 'DIR' PODEMOS VER TODOS LOS METODOS ASOCIADOS AL TIPO DE DATO. (EJEMPLO: print(dir(myStr)))

# COMENTARIO MULTIPLE USANDO TRIPLE "COMILLA SIMPLE O DOBLE" (''' ó """)
""" UN RENGLON QUE NO SE IMPRIMIRÁ..
OTRO RENGLON..
"""

'''
myStr = "HOLA polola"
print(dir(myStr))

print(myStr.capitalize())
print(myStr.replace("HOLA", "ADIOS").upper())
print('la cantidad de letras "o" es: ' ,myStr.count('o'))

mylist = myStr.split(' ')
print(f'formato lista {mylist}')

print(myStr.find('l'))
print(myStr.index('l'))
if type(myStr) == str:
    print ('si lo es')
else:
    print ('no lo es')

print('la cantidad de letras de mystr es: ', len(myStr))
'''



print('----------------')

#NUMEROS
# numero = int(input('ingrese un numero: '))
# multiplo = int(input('ingrese un multiplicador'))
# print(f'el producto entre {numero} y {multiplo} es {numero * multiplo}')

# exponente = int(input('ingrese un exponente'))
# print(f'el numero {numero} elevado a {exponente} es: {numero ** exponente}')


# print('----------------')
# def suma(a,b):
#     c = a+b
#     return c 
# print("la suma es: " ,suma(5,8))

# print('****')
# def compara(a=32,b=2):
#     if a < b:
#         return " b es mayor que a"
#     else:
#         return "a es mayor que b"
# print(compara())

# print('****')
# def listarPares(desde, hasta):
#     for i in range(desde,hasta):
#         if i%2 == 0:
#             print(i)
# listarPares(0,5)

# def ingreso():
#     edad = int(input('ingrese su edad: '))
#     if edad>18:
#         print('puedes pasar')
#     else:
#         print('no puedes entrar)')
# ingreso()

# print('****')
# for i in range (0,3):
#     print(i)

    
# i=0
# letras = list(('a', 'b', 'c', 'd', 'e', 'f'))
# while i<len(letras):
#     print(letras[i])
#     i=i+1

# if('x' in letras): print('contiene')
# else: print('no contiene')

# letras.append('g')
# print(letras)

# letras.extend(('h', 'i', 'j'))
# print(letras)

# letras.insert(0, "#")
# print(letras)


# ultimo = letras.pop()
# print(f'eliminado {ultimo}')


# if '#' in letras: letras.remove('#')
# print(letras)

# letras.sort(reverse=True)
# print(letras)
# letras[2] = "ZZ"
# print(letras)


# meses = {'1':'enero','2':'febrero'}

# print(dir(meses))
# meses['3'] = 'marzo'

# print(meses.items())

# frutas = []
# print ('las frutas son', frutas)
# frutas.append('banana')
# frutas.append('naranja')
# frutas.append('manzana')
# frutas.append('pera')

# print(frutas)

# def validarCompra():
#     fruta = input('ingrese una fruta (para salir ingrese espacio vacio): ')
    
#     while fruta != ' ': 
#         if fruta.lower() in frutas:
#             print('there is ENAUGHT', fruta)
#         else:
#             print('you HAVE TO BUY ', fruta)
#             confirmar = input('desea agregarla? (ingrese yes or not) ')
#             if confirmar.lower() == 'yes':
#                 frutas.append(fruta.lower())
#                 input('fruta ingresada correctamente !!! ENTER para continuar')

#         fruta = input('ingrese una fruta (para salir ingrese espacio vacio): ')
#     for f in frutas:
         
#          print(f.split())
# validarCompra()

# FUNCIONES LAMBDA.. (es como las funciones flechas.. se definen los parametros y retorna directo la operación sin llamar a return)
# suma = lambda num1, num2: num1 + num2

# def sumar ():
#     a = int(input('ingrse el primer numero '))
#     b = int(input('ingrse el segundo numero '))
#     return suma(a,b)

# print('la suma es ', sumar())

# MODULOS -------- 
# import datetime
# ahora = datetime.datetime.now()
# print('este año es ' ,ahora.year)

# import prueba.modulos as modulos
# print(modulos.suma(3,8))