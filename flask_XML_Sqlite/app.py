from flask import Flask, render_template, session, redirect, request, flash
import sqlite3

# importing files 
import XMLProcess as XML
import DDBBProcess 

app = Flask(__name__)
app.secret_key="clave secreta"

def getData(type):
    # extracting data from the File 
    data= XML.readFile()

    # Clearing DataBase and storaging new data 
    DDBBProcess.clearDDBB()
    DDBBProcess.uploadData(data)

    #reading database
    if type == "admin":
        datos = DDBBProcess.readData()
        return datos
    else:
        datos = DDBBProcess.readPartialData()
        return datos


@app.before_request
def validar():
    ruta = request.endpoint
    if 'user' not in session and ruta != 'login' and '/static/' not in request.path:
        return redirect('/login')
    

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        user=request.form['user']
        password=request.form['password']
        res = DDBBProcess.verifyingUser(user, password)
        session['user']= res[1]
        session['type']= res[3]
        if res != None:
            return redirect('/')

    return render_template('login.html')


@app.route('/')
def index():
    if 'type' in session:
        
        data=getData(session['type'])
        if session['type'] != "admin":
            flash("Ud tiene permisos de usuario con tiene privilegios limitados")
            flash("<a href='/login'>Loguearse como admin</a>")

    return render_template('index.html', data=data, user=session['user'])


@app.route('/close', methods=['POST'])
def close():
    session.clear()
    return redirect('/login')



if __name__ == '__main__':
    app.run(port=8000, debug=True)
 