
# CONSIGNA:
# leer el archivo y obtener para cada objeto activity de la lista mainActivityList dentro del objeto activityPlan el valor del tag activityType.

import xml.etree.ElementTree as ET

file = open("./repaso/SAO.XML")
root=ET.parse(file).getroot()

for item in root: #veo y obtengo posición de maniActivityList dentro de raiz 
    print(item.tag) #(para este caso es posición 2)


activity= root[2].findall("activity") #obtengo la lista de actividades
for i in activity:
    for n in range(len(i)):
        if i[n].tag== "activityType":
            print(i[n].text)