import xml.etree.ElementTree as ET

XMLPath='./flask_XML_Sqlite/SAO.XML'
def readFile():
    with open(XMLPath) as f:
        tree= ET.parse(f)
        root=tree.getroot()

    DDBB= []
    lista = root.iter("activity")

    for item in lista:
        reference= item[0].text
        activityType= item[3].text
        startTime= item[5][0].text
        endTime = item[5][1].text
        dato=(reference, startTime, endTime, activityType)
        DDBB.append(dato)
    
    return DDBB


    
    