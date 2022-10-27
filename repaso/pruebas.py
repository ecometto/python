from datetime import datetime, timedelta

fecha_cad1 = '12:15:49.646660'
fecha_cad2 = '12:15:49.646805'
fecha1 = datetime.strptime(fecha_cad1, '%H:%M:%S.%f')
fecha2 = datetime.strptime(fecha_cad2, '%H:%M:%S.%f')

res= fecha2 - fecha1

print(res)

# imprime: 
# 0:00:00.000145 


# --------------------------------------------- 
import xml.etree.ElementTree as ET
file=open("./repaso/aa.xml")
tree=ET.parse(file)
root= tree.getroot()

        
newCountryData= '''
    <country name="Panama3">
        <rank updated="yes">69</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W" />
        <neighbor name="Colombia" direction="E" />
    </country>
'''
ETData=ET.fromstring(newCountryData)
root.append(ETData)

tree.write("./repaso/aa.xml")
# file.close()

# -------------------------------------------- 
# ACTUALIZANDO 
# file=open("./repaso/aa.xml")
# tree=ET.parse(file)
# root= tree.getroot()

for x in root.iter('country'):
    print(x.tag)
    year= x.find("year")
    print(year.text)
    if int(year.text) < 2013:
        x.find("rank").text = "Obsolete"

tree.write("./repaso/aa.xml")
file.close()