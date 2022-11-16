import json

def getData():
        with open('REST_API/paises.json')as f:
            data= json.load(f)
            return data
            
def saveData(data):
    with open('REST_API/paises.json', 'w')as f:
            json.dump(data, f)