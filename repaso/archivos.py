# #vaciar archivo
# with open("./repaso.pruebas1.txt", "w") as f:
#     f.write("")
    

# #agregar información a archivo
# with open("./repaso.pruebas1.txt", "a") as f:
#     for fila in range(1,10):
#         f.write(f"Fila numero {fila}...\n")
        

#leyendo archivo
with open("./repaso.pruebas1.txt", "r") as f:
    data=f.read()
    f.seek(0,0)
    arrayLines=f.readlines()

print(data)

##cortando ultimas 3 filas
# qlinesArray=int(len(arrayLines))
# toCut=int(input("ingrese numero de filas a cortar"))
# ultimaInclusive=qlinesArray-toCut

##dos opciones parar resolver:
## opcion 1:
# del arrayLines[ultimaInclusive:qlinesArray]

##opcion 2:
# eliminados=0
# for linea in reversed(arrayLines):
#     if eliminados < toCut:
#         arrayLines.remove(linea)
#         eliminados +=1 

#print(arrayLines)
        