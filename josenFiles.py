import json

try:
    archivo = open('JsonFile.json', 'r')
    data = json.load(archivo)
    archivo.close()

    for d in range(0, len(data)):
        print(data[d]['name'])
        if d > 2:
            data.remove(data[d])
        
    archivo = open('JsonFile.json','w')
    Json=json.dumps(data)
    archivo.write(Json)
    archivo.close()


    archivo = open('JsonFile.json', 'r')
    data = json.load(archivo)
    archivo.close()
    for d in data:
        print(d)
except:
    print('hubo errores durante la carga. asegurese que el archivo no esté vacio')





# # try:
# jsonFile = open('JsonFile.json','r') 

# # LOAD: PARA "DESERIALIZAR" UN ARCHIVO
# data = json.load(jsonFile)

# jsonFile.close()

# dato = { "name":"jhony", "age":50, "city":"Manhattan"}

# data.append(dato)

# for d in data:
#     print(d)

# # DUMP: PARA "SERIALIZAR" UN ARCHIVO
# with open('JsonFile.json', 'w') as f:
#     txt = json.dumps(data)
#     f.write(txt)
        
