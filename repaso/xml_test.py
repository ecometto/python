import xml.etree.ElementTree as ET

XMLPath='./repaso/xml.xml'



with open(XMLPath) as file:
    tree=ET.parse(file)
    root=tree.getroot()

    print("-----------ANTES-------------")
    for cada in root.iter("country"):
        print(f"Pais: {cada.tag} {cada.attrib['name']} - Fundacion: {cada[1].text}")
        
        for cada in root.iter('country'):
            year=int(cada[1].text)
            if  year > 2011:
                cada[1].set('status', 'NEW')
                print(cada[1].attrib['status'])

    tree.write('./repaso/xml.xml')


def deleteEnd():
    QDelete= int(input("cantidad a eliminar: "))
    ultimo = (len(root) - QDelete)
    for cada in range (len(root)-1,0,-1):    
        if cada >= ultimo:
            root.remove(root[cada])

# deleteEnd() 
# print("-----------DESPUES-------------")
# for cada in root.iter("country"):
#     print(f"Pais: {cada.attrib['name']} - Fundacion: {cada[1].text}")

# with open(XMLPath, 'w') as file:
#     tree=ET.parse(file)
#     root=tree.getroot()
#     for cada in root.iter('country'):
#         year=int(cada[1].text)
#         if  year > 2011:
#             cada[1].set('status', 'actual')
#             print(cada[1].attrib['status'])
#             cada[1].attrib['status'] = "obsoleto" 
#             print(f"el pais {cada.attrib['name']} es mayor a 2011. Fecha: {cada[1].text}")
#     print(tree)
    # tree.write(file)    


        
        

# # MODIFING TAG TEXT AND ATTR 
# for each in root.iter("rank"):
#     # each.text=str(int(each.text)+1)
#     each.set("audit","false") #agregando un atributo

# #REMOVING TAG
# # for x in root.iter("country"):
# #     if int(x.find("rank").text)> 50:
# #         root.remove(x)

# dataToAdd= '''
#     <country name="Panama2">
#         <rank updated="yes">69</rank>
#         <year>2011</year>
#         <gdppc>13600</gdppc>
#         <neighbor name="Costa Rica" direction="W"/>
#         <neighbor name="Colombia" direction="E"/>
#     </country>
# '''
# elemento= ET.fromstring(dataToAdd)
# root.append(elemento)


# for x in root.iter('country'):
#     print(x.tag)
#     year= x.find("year")
#     print(year.text)
#     if int(year.text) < 2013:
#         x.find("rank").text = "Obsolete"

# # paises=root.findall("country")
# # for pais in paises:
# #     print( pais[1].text)

# for x in root.iter("country"):
#     print(x[0].text)

# tree.write("./repaso/aa.xml")



