from re import search
import ejercicios1 as e1

e1.separar()
# Ejercicio 1
# La función max() del ejercicio 1 (primera parte) y la función max_de_tres() del ejercicio 2 (primera parte), solo van a funcionar para 2 o 3 números. Supongamos que tenemos mas de 3 números o no sabemos cuantos números son. Escribir una función max_in_list() que tome una lista de números y devuelva el mas grande.
def maxInList(*args):
    max = 0
    for arg in args:
        if arg > max:
            max = arg
    return max

print(maxInList(9,8,3,55,14,25,71))


e1.separar()
# Ejercicio 2
# Escribir una función mas_larga() que tome una lista de palabras y devuelva la mas larga.
def mas_larga(WordList):
    lenWord = 0
    larga = ""
    for word in WordList:
        if len(word) > lenWord:
            lenWord = len(word)
            larga = word
    return larga
print(mas_larga(["laprimera", "lasegunditass", "tercera"]))

e1.separar()
# Ejercicio 3
# Escribir una función filtrar_palabras() que tome una lista de palabras y un entero n, y devuelva las palabras que tengan mas de n caracteres.
def filtrar_palabras(list, nChar):
    filtrada=[]
    for item in list:
        if len(item) > nChar:
            filtrada.append(item)
    return filtrada

palabras=["salud","depende","enorme","rojo","saltando","type", "animosidad", "dos"]
print(filtrar_palabras(palabras, 6))

e1.separar()
# Ejercicio 4
# Escribir un programa que le diga al usuario que ingrese una cadena. El programa tiene que evaluar la cadena y decir cuantas letras mayúsculas tiene.
def qUpper():
    count=0
    # myString=input("ingrese una cadena")
    myString="Lista Cadena con Mayusculas"
    for i in myString:
        if search("[A-Z]", i):
            print("mayuscula encontrada")
            count+=1
    return count
print(f"cantidad de mayusculas: {qUpper()}")
            

e1.separar()
# Ejercicio 5
# Construir un pequeño programa que convierta números binarios en enteros.
def convertToDecimal(bin):
    count=1 ;    
    numero=0
    for i in reversed(bin):
        if i == "1":
            numero += 2**(count-1)
        count+=1
    return numero

print(convertToDecimal("1010"))


e1.separar()
# Ejercicio 6
# Escribir un pequeño programa donde:
# - Se ingresa el año en curso.
# - Se ingresa el nombre y el año de nacimiento de tres personas.
# - Se calcula cuántos años cumplirán durante el año en curso.
# - Se imprime en pantalla.

def calcYears():
    personas=[]
    actualYear=int(input("ingrese año actual: "))
    for i in range (0,2):
        name=input(f"ingrese nombre de persona {i+1}: ")
        birthDate=input(f"ingrese fecha nacimiento de persona {i+1} (dd/mm/yyyy): ")
        yearDate=int(birthDate[-4:])
        personas.append([name,birthDate, yearDate])

    for persona in personas:
        age= actualYear - persona[2]
        print(f"La persona {persona[0]} tiene o cumple {age} años")

#print(calcYears())


e1.separar()
# Ejercicio 7
# Definir una tupla con 10 edades de personas.
# Imprimir la cantidad de personas con edades superiores a 20.
# Puedes variar el ejercicio para que sea el usuario quien ingrese las edades.
def verifAge(tuple, age):
    count=0
    for item in tuple:
        if item > age:
            count += 1
    return count
edades=(30,11,55,42,80,93,77,68,35,22,46,76,32,31)
print("mayores: ", verifAge(edades,90))


e1.separar()
# Ejercicio 8
# Definir una lista con un conjunto de nombres, imprimir la cantidad de comienzan con la letra a.
# También se puede hacer elegir al usuario la letra a buscar.  (Un poco mas emocionante)
def cantCapitalLetter(list):
    count=0
    for persona in list:
        if search("^[aA]", persona):
            count +=1
    return count

personas=["Analia", "Carlos", "alberto", "Miguel", "Zulema", "Eva", "Donatella", "Ariana"]
print("cantidad que comienzan: ",cantCapitalLetter(personas))


e1.separar()
# Ejercicio 9
# Crear una función contar_vocales(), que reciba una palabra y cuente cuantas letras "a" tiene, cuantas letras "e" tiene y así hasta completar todas las vocales.
# Se puede hacer que el usuario sea quien elija la palabra.

def contar_vocales(dictVowels):
    palabra= input("ingrese la palabra/frase a evaluar: ")
    for vowel in dictVowels.keys():
        count=0
        for cada in palabra:
            if search(vowel,cada):
                count +=1
        dictVowels[vowel]=count        

diccVocales={"a":0, "e":0, "i":0, "o":0, "u":0 }
contar_vocales(diccVocales)

    

e1.separar()
# Ejercicio 10
# Escriba una función es_bisiesto() que determine si un año determinado es un año
# bisiesto.Un año bisiesto es divisible por 4, pero no por 100. También es divisible por 400
def  es_bisiesto():
    # year=int(input("ingrese el año a verificar si es bisiesto: "))
    year=2022
    if year % 4 == 0:
        return "Bisiesto"
    else:
        return "no bisiesto"

print(es_bisiesto())