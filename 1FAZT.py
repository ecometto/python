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


print('----------------')
def suma(a,b):
    c = a+b
    return c 
print("la suma es: " ,suma(5,8))

print('****')
def compara(a,b):
    if a < b:
        return " b es mayor que a"
    else:
        return "a es mayor que b"
print(compara(4,8))

print('****')
def listarPares(desde, hasta):
    for i in range(desde,hasta):
        if i%2 == 0:
            print(i)
listarPares(0,10)


print('****')
for i in range (0,5):
    print(i)

    
i=0
letras = list(('a', 'b', 'c', 'd', 'e', 'f'))
while i<len(letras):
    print(letras[i])
    i=i+1

if('x' in letras): print('contiene')
else: print('no contiene')

letras.append('g')
print(letras)

letras.extend(('h', 'i', 'j'))
print(letras)

letras.insert(0, "#")
print(letras)

ultimo = letras.pop()
# letras.pop(0)
if '#' in letras: letras.remove('#')
print(letras)
print(ultimo)