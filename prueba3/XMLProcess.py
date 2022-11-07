import xml.etree.ElementTree as ET

def readFile():
    with open('./prueba3/SAO.XML') as f:
        tree= ET.parse(f)
        root=tree.getroot()

    DDBB= []
    lista = root.iter("activity")

    for item in lista:
        reference= item[0].text
        startTime= item[5][0].text
        endTime = item[5][1].text
        dato=(reference, startTime, endTime)
        DDBB.append(dato)
    
    return DDBB


    
    