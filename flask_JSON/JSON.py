import json

data={}
def validarUser(user, password):
    with open('./flask_JSON/dataBase.json') as f:
        try:
            data=json.load(f)
            if data:
                for cada in data['usuarios']:
                    if user in cada['nombre'] and password in cada['pass']:
                        return 1
                    else:
                        return "error"
        except Exception as err:
            print( "No hay datos en la Base de Datos de usuarios" )
            return 0


res=validarUser('Edgardo', '12')
print(res)


