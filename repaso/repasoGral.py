#funcion para separar resultados
def separar():
    print("\n--------------------------------------------------\n")
separar()

# -------------VARIABLES PRIMITIVAS ------------------
stringType = "hola soy un string en python. Para realizar pruebas"
numberType = 2
booleanType = True

print(f"la variable 'stringType' es de tipo {type(stringType)}. Su contenido es: {stringType}")
palabra=input("ingrese la palabra a buscar: ")

print("Palabra encontrada en : " , stringType.find(palabra))

print(f"Desde '{palabra}' - hasta el final: -- \"{stringType[stringType.find(palabra):len(stringType)]}\"")


print("parcial: " ,stringType[1:10])

print(f"la variable 'numberType' es de tipo {type(numberType)}. Su contenido es: {numberType}")

print(f"la variable 'booleanType' es de tipo {type(booleanType)}. Su contenido es: {booleanType}")


#  ------------- ARRAYS  y TUPLAS ---------------
separar()

arrayX = ['hola', 4 , "soy yo el tercero-segundo", False, ('soy', 'una', 'tupla', 'en', 'array')]
tuplas=(1, "tuplita", 38 , True)

print(arrayX[0:2])
print(tuplas[1:2])

#metodos array
arrayX.insert(1, "new object inserted")
arrayX.append("the last added")
arrayX.extend(["uno", "dos", (1,2,3)])
deletedFromArray=arrayX.pop(3)
posicion = arrayX.index("uno")

print("posición de 'uno': ", posicion)
print(f"deleted from Array - {deletedFromArray}")


# --------- FUNCIONES, LOOPS Y CONDICIONALES ---------------
separar()

print("--- datos de Array ---")    
for i in arrayX:
    print(i)

for i in range (1,len(arrayX)):
    if i == 3:
        continue
    print(f"{i}° - {arrayX[i-1]}".upper())

num =0
while num <= 50:
    num +=1
    if num == 5:
        continue
    if num == 8:
        break 
    print(num)
print("fin de la instrucción while".upper())

def validarEdad(edad):
    if edad <= 18:
        return False
    return True


edad= int(input("ingrese su edad"))
pasa= validarEdad(edad)
while not pasa:
    print(f"lo siento, tienes {edad} años. Eres menor de 18")
    edad= int(input("ingrese su edad"))
    pasa= validarEdad(edad)
    print(pasa)
print("welcome.. ")
    
