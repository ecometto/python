'''
/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */
 
 for n in range(1,101):
    if n % 3 == 0 and n % 5 == 0:
        print("fizzBuzz")        
    elif n % 3 == 0:
        print("fizz")
    elif n % 5 == 0:
        print("Buzz")
    else: print(n)
 '''   
    
    
    
'''
/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */

myString = "Hola a todos, soy el León"
vowels = {
"a":"4",
"e":"3",
"i":"1",
"o":"0",
"ó":"0",
"u":"(_)"
}

#recorriendo y haciendo un nuevo string
newString = ""
for letter in myString:
    if letter in vowels:
        newString += vowels[letter]
    else:
        newString += letter

print(newString)

#con metodo replace directamente
for key, value in vowels.items():
    myString = myString.replace(key, value)
print(myString)
'''



'''
/*
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 */
 
str1 = "hola mundo"
str2 = "ohal umnd"

def anagrama(s1,s2):
    anagrama = True
    dictS1 = {}
    dictS2 = {}
    #descarte por cantidad de letras
    if len(s1) != len(s2):
        anagrama = False
    # contar letras de S1 y agregar a un diccionario
    for letra in s1:
        if letra in dictS1.keys():
            dictS1[letra]= dictS1[letra] + 1
        else:
            dictS1[letra] = 1
    
    # contar letras de S2 y agregar a un diccionario
    for letra in s2:
        if letra in dictS2.keys():
            dictS2[letra]= dictS2[letra] + 1
        else:
            dictS2[letra] = 1
            
    for claveS1, valorS1 in dictS1.items():
        if claveS1 not in dictS2.keys() or dictS1[claveS1] != dictS2[claveS1]:
            anagrama = False  

    return anagrama
         
print(anagrama(str1, str2))
 
 '''
 



'''
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
 
def fibo (n):
    fibo = 0
    fiboAnterior = 1
    fiboAnteAnterior = 0
    
    for n in range (0 , n):
        if n < 2:
            fibo = n
        if n > 1:
            fibo = fiboAnterior + fiboAnteAnterior 
            fiboAnteAnterior = fiboAnterior
            fiboAnterior = fibo
            
        print("fibo ",fibo)
        
        
fibo(10)

'''


'''
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
def primos(num):
    numeros = []
    for n in range(0,num+1):
        if n < 2:
            print("El numero ", n , "es primo.")
        else:
            primo = True
            for cada in numeros:
                resto = n % cada
                if resto == 0:
                    primo = False
                    break
                      
            if primo == False:
                numeros.append(n) 
                print(f"El numero {n} no es primo.")
            else:
                numeros.append(n) 
                print(f"** SI. El numero {n} SI es primo.")       
                    
primos(20)
'''