import re

cadena1dig="SB1_ROI_SB1-SCE-1_20240605T100918.inp"
cadena2dig="SB1_ROI_SB1-SCE-34_20240605T100918.inp"
cadenas = [cadena1dig, cadena2dig]

print("\n\n","*"*30)

print("CON LA REGEX ANTERIOR")
for cada in cadenas:
    res = re.search(r"SB1_ROI_[a-zA-Z0-9-]{10}_[0-9]{8}T[0-9]{6}.inp",cada)
    if res != None:
         print(f"* Se encontró la cadena {cada}")
    else:
        print(f"* ERROR. NO SE ENCONTRÓ LA CADENA {cada}")
        
print("\nCON LA NUEVA REGEX ")
for cada in cadenas:
    res = re.search(r"SB1_ROI_[a-zA-Z0-9-]{9,10}_[0-9]{8}T[0-9]{6}.inp",cada)
    if res != None:
         print(f"* Se encontró la cadena {cada}")
    else:
        print(f"* ERROR. NO SE ENCONTRÓ LA CADENA {cada}")

print("\n")

#exercise1: validar mail:
#NO debe empezar con numero. Debe tener al menos 2 letras o numeros. Luego debe contener un @. Luego un dominio, luego un tipo de dominio (2 o 3 letras) y por último un pais (optativo).
#ejemplos validos: algo@gmail.com - otracosa222@gmail.ar

mail = "valido123@gmail.com.ar"
patternMail = r"([a-z]+)@([a-z]+.[a-z]{2,3}\.[a-z]*)" #lo que va entre paréntesis son grupos de captura.
result = re.search(patternMail,mail)
if result != None:
    print("The string " ,result.group(), "' was found.")
    print("UserName: " ,result.group(1), "'.")
    print("Domain: " ,result.group(2), "'.\n")
else:
    print("The string was not found.\n")


#exercise2
#Filter only 1 phone numbers with the prefix 011, and show just the number (without prefix)
found = False
prefix = "011"
numbers=["0351-15313585","011-5832245","012-5244521","011-5141153"]
patternPrefix = rf"({prefix})-(\d+)" #lo que va entre paréntesis son "grupos de captura". Con resultado.group(1) obtengo el primer grupo
for number in numbers:
    find = re.search(patternPrefix, number)
    if find:
        found = True      
        break  
  
if found:
    print(f"Number found with prefix {find.group(1)}. This number is: {find.group(2)}.\n")
else:
    print(f"Zero numbers with the prefix {prefix} were found.\n")

#para encontrar todos los numeros que coincidan con el prefijo : 
#ATENCION. En el método findall, si se incluyen grupos de captura, dicho método devolverá un array de tuplas con los grupos indicados.
numbersToString = " / ".join(numbers)
many = re.findall(r"011-(\d+)|012-(\d+)", numbersToString)

if many:
    for i in many:
        if i[0]:
            print("con 011: ", i[0])
        else:
            print("con 012: ", i[1])




'''
abc…	Letters
123…	Digits
\d	    Any Digit
\D	    Any Non-digit character
.	    Any Character
\.	    Period
[abc]	Only a, b, or c
[^abc]	Not a, b, nor c
[a-z]	Characters a to z
[0-9]	Numbers 0 to 9
\w	Any Alphanumeric character
\W	Any Non-alphanumeric character
{m}	m Repetitions
{m,n}	m to n Repetitions
*	Zero or more repetitions
+	One or more repetitions
?	Optional character
\s	Any Whitespace
\S	Any Non-whitespace character
^…$	Starts and ends
(…)	Capture Group
(a(bc))	Capture Sub-group
(.*)	Capture all
'''