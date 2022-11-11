import json
import requests
import re


#obteniendo datos de API y almacendando en archivo JSON
def downloadingData():
    ruta="./flaskJSON/countries.json"
    url="https://restcountries.com/v2/all"
    data=requests.get(url)
    data=data.json()

    with open(ruta, 'w') as file:
        json.dump(data, file)
        
        
#geting data"""FROM JSON FILE"""
def getData():
    ruta="./flaskJSON/countries.json"
    with open(ruta) as file:
        users= json.load(file)
        return users


# def searchCountry(country):
#     data=getData()
#     for cada in data:
#        res= re.search(country, cada['name'], re.IGNORECASE)
#        if res:
#            print(res)
# searchCountry("argentina")

# datos=getData()
# def pares(country):
#         if "Argentina" in country['name']:
#             return country['name']
    
# new= map(pares, datos)
# for cada in new:
#     # print(list(cada))
#     print(cada)

# Return double of n
def addition(n):
    if "Ar" in n['name']:
        return n
    else:
        return ""
  
# We double all numbers using map()
numbers = getData()
result = filter(addition, numbers)
# print(list(result))
for cada in result:
    print(cada['name'])

#validando usuario
def validarUser(user, passw):
    file="./flaskJSON/users.json"
    with open(file) as f:
        users= json.load(f)
        for cada in users['users']:
            patronUser =f"\\b{user}\\b"
            patronPass =f"\\b{passw}\\b"
            if re.match( patronUser , cada['nombre']) and re.match(patronPass, cada['pass']):
                return (cada)