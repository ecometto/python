import json


    
def newPerson(listObject):
    name=input("ingrese su nombre ")
    age=int(input("ingrese su edad "))
    city=input("ingrese la ciudad ")
    new= {'name': name, 'age': age, 'city': city}
    listObject.append(new)
    save(data)
    print(data)
    print("cargado exitosamente")

def save(data):
    with open("JsonFile.json","w") as f:
        json.dump(data, f)


def new(data):
    continuar="1"
    while continuar=="1":
        newPerson(data)
        continuar=input("desea continuar: 1-Si  /  0-NO")

def filterAge(data, age):
    filtered= filter(lambda x:x['age']>age, data)
    return filtered

def listar(data):
    '''Funcion para filtrar '''
    for cada in data:
        print(f"Nombre: {cada['name']}, Edad: {cada['age']}, Ciudad: {cada['city']}")
        # print(cada)
# ------------- comienzo ---------------
try:
    file=open("JsonFile.json")
    data= json.load(file)
except Exception as e:
    print("error al cargar archivo. Asegurese que existe y que tenga formato JSON")

finally:
    file.close()    

#menu:
print("MENU\n")
opcion=input("1-Nuevo registro \n2-Filtrar por edad \n3-Listar \n0-SALIR ")

while opcion != "0":
    if opcion == "1":
        new(data)
    elif opcion=="2":
        edad= int(input("ingrese la edad"))
        filtered=filterAge(data, edad)
        for cada in filtered:
            print(f"{cada['name']} - {cada['age']}")
    elif opcion == "3":
        listar(data)           
    
    opcion=input("1-Nuevo registro \n2-Filtrar por edad \n3-Listar \n0-SALIR ")
    

        
# * en filtrado, inclur el input en la funcion 
# file=open("JsonFile.json")
# data= json.load(file)
# print(data)














# try:
#     archivo = open('JsonFile.json', 'r')
#     data = json.load(archivo)
#     archivo.close()

#     for d in range(0, len(data)):
#         print(data[d]['name'])
#         if d > 2:
#             data.remove(data[d])
        
#     archivo = open('JsonFile.json','w')
#     Json=json.dumps(data)
#     archivo.write(Json)
#     archivo.close()


#     archivo = open('JsonFile.json', 'r')
#     data = json.load(archivo)
#     archivo.close()
#     for d in data:
#         print(d)
# except:
#     print('hubo errores durante la carga. asegurese que el archivo no esté vacio')





# # # try:
# # jsonFile = open('JsonFile.json','r') 

# # # LOAD: PARA "DESERIALIZAR" UN ARCHIVO
# # data = json.load(jsonFile)

# # jsonFile.close()

# # dato = { "name":"jhony", "age":50, "city":"Manhattan"}

# # data.append(dato)

# # for d in data:
# #     print(d)

# # # DUMP: PARA "SERIALIZAR" UN ARCHIVO
# # with open('JsonFile.json', 'w') as f:
# #     txt = json.dumps(data)
# #     f.write(txt)
        
