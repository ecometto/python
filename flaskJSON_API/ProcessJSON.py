import json
import requests
import re


#obteniendo datos de API y almacendando en archivo JSON
def downloadingData():
    ruta="./flaskJSON/countries.json"
    # ruta="./flaskJSON/countries.json"
    url="localhost:8000/data"
    data=requests.get(url)
    data=data.json()

    with open(ruta, 'w') as file:
        json.dump(data, file)
        
        
#geting data"""FROM JSON FILE"""
def getData():
    ruta="./flaskJSON_API/countries.json"
    with open(ruta) as file:
        users= json.load(file)
        return users


# def searchCountry(country):

def search(country):
    data = getData()
    res = []
    # result = filter(searchCountry(country), data)
    for cada in data:
        if country.lower() in cada['name'].lower():
            print("finded", cada['name'])
            res.append(cada)
    return res
         
    
# def searchCountry(data, country):
#     if country in data['name']:
#         return data


#validando usuario
def validarUser(user, passw):
    file="./flaskJSON_API/users.json"
    with open(file) as f:
        users= json.load(f)
        for cada in users['users']:
            patronUser =f"\\b{user}\\b"
            patronPass =f"\\b{passw}\\b"
            if re.match( patronUser , cada['nombre']) and re.match(patronPass, cada['pass']):
                return (cada)