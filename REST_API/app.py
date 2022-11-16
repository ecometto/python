from flask import Flask, render_template, jsonify, request, redirect
import json
import requests
import operator
from functions import getData, saveData

app = Flask(__name__)




# routes ---------- 
@app.route('/', methods=['GET', 'POST', 'DELETE'])
def index():
    data= requests.get('http://127.0.0.1:3000/backend/data')
    data=data.json()
    return render_template('index.html', data=data)




#  BACKEND ------------------------------ 
@app.route('/backend/data', methods=['GET'])
def data():
    with open('REST_API/paises.json')as f:
        data= json.load(f)
        return jsonify(data)
    
    
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        nombre= request.form['nombre']
        capital= request.form['capital']
        with open('REST_API/paises.json')as f:
            data= json.load(f)
        
        newcountry={"nombre": nombre, "capital":capital}
        data.append(newcountry)
        
        ordenados = sorted(data, key=lambda pais : pais['nombre'])
        print(ordenados)
        with open('REST_API/paises.json', 'w')as f:
            json.dump(ordenados, f)
        
        return redirect('/')



@app.route('/delete/<nombre>', methods=['DELETE'])
def dele(nombre):
    data= getData()
    for cada in data:
        # print(cada['nombre'] , "-", nombre)
        if cada['nombre'] == nombre:
            print("encontrado............")
            data.remove(cada)
        
    saveData(data)
            
    return redirect('/')


    



# running server 
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000, debug=True)
 