def separar():
    print("\n *************************************************\n")

separar()
# 1 - Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. (Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.
def max(a, b):
    if a > b:
        return a
    else:
        return b

maximo=max(101,202)
print(maximo)

separar()
# 2 - Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.
def max_de_tres(a,b,c):
    max=0
    for i in a,b,c:
        if i > max:
            max=i
    return max

maximo3=max_de_tres(1,5,30)
print(maximo3)

separar()
# 3 - Definir una función que calcule la longitud de una lista o una cadena dada. (Es cierto que python tiene la función len() incorporada, pero escribirla por nosotros mismos resulta un muy buen ejercicio.
def lenList(list):
    count = 0
    for i in list:
        count +=1
    return count
    
listaNums=[1,9,5,44,6,32,5,55,12]
print(lenList(listaNums))


separar()
# 4 - Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.
def isVowel(caracter, lista):
    if caracter in lista:
        return True
    else:
        return False
vowels= ("a", "e", "i", "o", "u")
caracteres = [1, "m", "e", "t", "o", "v", 3]
for c in caracteres:
    print(f"charter {c} is a vowel?: { isVowel(c, vowels) }")

separar()
# 5 - Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.
def sum(*args):
    total=0
    for arg in args:
        total+=arg
    return total

def multip(*args):
    total=1
    for arg in args:
        total*=arg
    return total

def sumaMultip(*args):
    suma=0; 
    mult=1
    for arg in args:
        suma+=arg
        mult*=arg
    return (suma, mult)

print(sum(1,2,3,4))
print(multip(1,2,3,4))
print("Suma: " ,sumaMultip(1,2,3,4)[0], ". Multiplicación: ", sumaMultip(1,2,3,4)[1])


separar()
# 6 - Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"

def invertString(string):
    string = f" {string}"
    inverted=string[len(string):0:-1]
    return inverted

myString = "Hello World"
print(invertString(myString))


separar()
# 7 - Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.

def isPalindrome(string):
    ini=0
    end=int(len(string)-1)
    equals=True
    while ini <= end:
        if string[ini] != string[end]:
            equals = False
            print("No son iguales")
            break
        ini= ini+1
        end= end-1
    return(equals)

palabra="radar"
if isPalindrome(palabra):
    print(palabra, " ES PALINDROMO")
else:
    print(palabra, " no es palindromo... sorry")
    

separar()
# 8 - Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado.
def superposicion(lista1, lista2):
    for cada1 in lista1:
        for cada2 in lista2:
            if cada2 == cada1:
                print("encontrado. Valor: ", cada1)
                return True
    return False

l1=[1,3,5,8,7,"hola", "que tal"]            
l2=[9,6,7,"chau", "adios"] 
print(superposicion(l1,l2))


separar()
# 9 - Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".

def generar_n_caracteres(chart, repeat):
    return chart*repeat

print(generar_n_caracteres("/", 10))


separar()
# 10 - Definir un histograma procedimiento() que tome una lista de números enteros e imprima un histograma en la pantalla. Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:
# ****
# *********
# *******
def procedimiento(*args):
    for arg in args:
        print("*" * arg)
procedimiento(1,5,6)

def proced2(list):
    for item in range(0,len(list)):
        print("#" * list[item])
proced2([10,5,16])


separar()
