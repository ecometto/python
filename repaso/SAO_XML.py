from xml.dom.minidom import Document
import xml.etree.cElementTree as ET

file = open("./repaso/SAO.xml")

data=ET.parse(file)
root=data.getroot()

#para visualizar la primera linea de tag HIJOS
for cada in root:
    print(cada.tag)

print("-----------")
#con el dato anterior podemos acceder a cada uno:

todos=Document.getElementsByTagName('activity')

print(todos)