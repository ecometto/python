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