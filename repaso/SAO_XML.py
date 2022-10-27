import xml.etree.cElementTree as ET

file=open("./repaso/aa.XML")
data=file.read()
string=ET.fromstring(data)

print(data)
print("-------------")
print(string)

for cada in root:
    print(cada.tag)

