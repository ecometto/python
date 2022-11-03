import xml.etree.ElementTree as ET
import re
from datetime import datetime

file = open("./repaso/SAO.XML")
lectura=file.read()
file.seek(0)
tree= ET.parse(file)
root=tree.getroot()
# print(lectura)

def main():
    for cada in root.iter("activity"):
        refID=cada[0].text
        actType=cada[3].text
        #Obteniendo fecha/hora y calculando diferencia
        startTime=re.sub("T"," ",cada[5][0].text)
        sTime=datetime.strptime(startTime,"%Y-%m-%d %H:%M:%S.%f")
        # print(sTime)
        endTime=re.sub("T"," ",cada[5][1].text)
        eTime=datetime.strptime(endTime,"%Y-%m-%d %H:%M:%S.%f")
        # print(eTime)
        difTime = (eTime - sTime)
        # print(f"dif: {difTime}")
        print(f"Referencia: {refID}: Duración: {difTime}. \n tipo: {actType}\n")
    
main()


    
    
    
# # funcion inicial incluyendo datos de demora y redID. Con Regex (sin incluir fecha)
# for cada in root.iter("activity"):
#     refID=cada[0].text
#     actType=cada[3].text
#     startTime=re.search("((\d+:)+\d{2}.\d{6})",cada[5][0].text)[0]
#     sTime=datetime.strptime(startTime,"%H:%M:%S.%f")
#     # print(sTime)
#     endTime=re.search("((\d+:)+\d{2}.\d{6})",cada[5][1].text)[0]
#     eTime=datetime.strptime(endTime,"%H:%M:%S.%f")
#     # print(eTime)
#     difTime = eTime - sTime
#     # print(difTime)
#     print(f"La referencia: {refID}, Tuvo una demora de {difTime}. \n - Tipo: {actType}\n")


# ---------------------------------------------------------------- 
# # FUNCION OPTIMIZADA con "ITER":
# for cada in root.iter("activity"):
#      print(f"{cada[0].tag}: {cada[0].text} - ActivityType: {cada[3].text}")

