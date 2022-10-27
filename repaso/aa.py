import xml.etree.ElementTree as ET
file=open("./repaso/aa.xml")
tree=ET.parse(file)
root=tree.getroot()

# MODIFING TAG TEXT AND ATTR 
for each in root.iter("rank"):
    # each.text=str(int(each.text)+1)
    each.set("audit","false") #agregando un atributo

#REMOVING TAG
for x in root.iter("country"):
    if int(x.find("rank").text)> 50:
        root.remove(x)

dataToAdd= '''
    <country name="Panama2">
        <rank updated="yes">69</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
'''
elemento= ET.fromstring(dataToAdd)
root.append(elemento)


for x in root.iter('country'):
    print(x.tag)
    year= x.find("year")
    print(year.text)
    if int(year.text) < 2013:
        x.find("rank").text = "Obsolete"

tree.write("./repaso/aa.xml")

file.close()

