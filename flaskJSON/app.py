from flask import Flask, render_template, session, redirect, request

import json

#geting data from json file
ruta="flaskJSON/users.json"
with open(ruta) as file:
    users= json.load(file)['data']

def validar(user, password, DDBB):
    for cada in DDBB:
        print(cada['nombre'])
        if user in cada['nombre'] and password in cada['pass']:
            print("encontrado")
            return user
            
usuario= validar("otadmin","123",users)
print(usuario)

app=Flask(__name__)
app.secret_key="secreta"



# ------------- rutas ------------------
@app.before_request
def validarUser():
    if "user" not in session:
        print("no loged")
    if "user" not in session and request.endpoint != 'login' and '/static/' not in request.path:
        return redirect('/login')


@app.route('/', methods=['GET', 'POST'])
def index():
    nombre = ""
    if "user" in session:
        nombre = session['user']
    return render_template('index.html', title="principal", user=nombre)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.clear()
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['user']="Edgardo"
        return redirect('/')
    
    
    return render_template('login.html')



if __name__ == "__main__":
    app.run(port=3000, debug=True)