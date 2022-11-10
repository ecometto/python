import json
import requests


def downloadingData():
    ruta="./flaskJSON/countries.json"
    url="https://restcountries.com/v2/all"
    data=requests.get(url)
    data=data.json()

    with open(ruta, 'w') as file:
        json.dump(data, file)
        
        
#geting data from json file
def getData():
    ruta="./flaskJSON/countries.json"
    with open(ruta) as file:
        users= json.load(file)
        return users


def validar(country, DDBB ):
    for cada in DDBB:
        # print(cada['name'])
        if country in cada['name']:
            return f"existe {cada['name']}. Su capital es {cada['capital']} - Región: {cada['region']}"
        
res=validar("Argentina", getData())
print(res)