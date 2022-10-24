import xml.etree.ElementTree as ET

file=open("./repaso/SAO.XML")
root=ET.parse(file).getroot() #para convertir los datos en un elemento TREE

# para convertir el elemento TREE en STRING
# print(ET.tostring(root, encoding="utf-8"))


# ----------------------------------------------
# para conocer cuantos hijos hay en root 
# print(len(root))
#para conocer los HIJOS DIRECTOS del root
# for nivel in root: 
#     print(nivel.tag)

#otra forma de ver las ETIQUETAS HIJO...
# for i in range(len(root)):
#     print(root[0].tag)



# la clase element tiene 4 atributos (tag, atrrib, text, tail)



# --------------------------------------------- 
#para conocer los HIJOS DE HIJOS
# for cada in root.findall("mainActivityList"): 
#     for subTag in cada[0]:
#         print(subTag.tag)


        

# act1=root[2][0]
# for cada in act1:
#     if cada.tag=="referenceId":
#         print("Encontrado", cada.text)

# buscar con FIND (devuelve la primera coincidencia)
# print((root[2].find('activity/status')).text)
# print((root.find('mainActivityList/activity/referenceId')).text)
        
        
# buscar con FINDALL (devuelve una lista con todas las coincidencias)
# listaStatus=root[2].findall('activity')
# for cada in listaStatus:
#     print(f"{cada[0].tag} - {cada[0].text}  / Status: {cada[1].text}")
    
activity= root[2].findall('activity')
for each in activity[0]:
    print(each.tag)

# for cada in activity:
#   for i in cada[0]:
#         print(i.tag)