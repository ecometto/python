from flask import Flask, render_template, json, redirect
import requests


app = Flask(__name__)

# functions ---------------------- 
# obteniendo datos
def getDataFromOrigin(url):
    data= requests.get(url)
    data=data.json()
    saveData(data)

def saveData(data):
    with open('REST_API_FETCH/DDBB.json', 'w') as f:
        json.dump(data, f)

def getData():
    with open('REST_API_FETCH/DDBB.json') as f:
        data = json.load(f)
        return data 
    

# BACKEND --------------- 
getDataFromOrigin('https://fakestoreapi.com/products')

#providing json data
@app.route('/API/data', methods=['GET', 'POST'])
def api():
    data = getData()
    return data

@app.route('/delete/<id>', methods=['GET', 'POST'])
def delete(id):
    data=getData()
    for cada in data:
        print(cada['id'])
        if str(cada['id']) == str(id):
            print("--------------------encontrado", cada['id'])

    return redirect('/')


# FRONTEND
#rendering data
@app.route('/')
def index():
    data=getData()
    return render_template('index.html', datos=data)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 