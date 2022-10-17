#primitives Variables

stringType="this is a text"
intType=16
floatType=12.36
booleanType=True

print("type text: " ,stringType)
print("int text: " ,intType)
print("float text: " ,floatType)
print("boolean text: " ,booleanType)
print( f"También se puede imprimir con corchetes con la letra 'f' adelante. \nEjemplo: {booleanType} or {stringType}")

print("----------------------------------------------------")
#IF SENTENCE (CONDITIONAL)
# string = input("Ingrese un texto a evaluar \n")
# if len(string) > 0:
#     print(f"El texto ingresado tiene {len(string)} caracteres. Está correcto")
# else:
#     print("debe ingresar al menos un caracter")

print("----------------------------------------------------")
#LOOPS ----------------
#FOR LOOP (THERE ARE SEVERAL EXAMPLES IN "FOR LOOPS")
for i in (1,2,3,4,5,6):
    print(i)

for i in range(0,4):
    print(f"Numero: {i}")

lista = ["juan", "pedro", "miguel", "rodrigo", "ana", "maria"]
for name in lista:
    print("el primer nombre es: ", name )

for letter in "this is a string":
    print(f"Letra: {letter}")

dictNotas={"edy": 95, "romulo": 40, "Ceci":90, "Lila": 83}
for alumno in dictNotas:
    print(f"Alumno {alumno}: {dictNotas[alumno]}")
    
for notas in dictNotas.values():
    print(notas)
    