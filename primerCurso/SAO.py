from time import strptime
import xml.etree.ElementTree as ET
import re
from datetime import datetime

file = open("./repaso/SAO.xml")
read= file.read()
file.seek(0)
tree=ET.parse(file)
root=tree.getroot()


for i in root.iter("activity"):
    StartTime=i[5][0].text
    STfiltered=re.sub("T", " ",  StartTime)
    fs= datetime.strptime(STfiltered, "%Y-%m-%d %H:%M:%S.%f")
    EndTime=i[5][1].text
    ETfiltered=re.sub("T", " ",  StartTime)
    fs= datetime.strptime(STfiltered, "%Y-%m-%d %H:%M:%S.%f")
    
    print(fs)
    print(f"Referencia: {i[0].text} - Type: {i[3].text}")