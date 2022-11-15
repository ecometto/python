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
        res = DDBBProcess.verifyingEncriptedUser(user, password)
        print(res)
        if res != None:
            session['user']= res[1]
            session['type']= res[3]
            return redirect('/')

        mensaje= flash("Error en los datos ingresados.")
        return render_template('login.html', mensaje=mensaje)
    
    return render_template('login.html')


@app.route('/')
def index():
    if 'type' in session:        
        data=getData(session['type'])
        if session['type'] != "admin":
            flash("Ud tiene permisos de usuario con tiene privilegios limitados")
            flash("<a href='/login'>Loguearse como admin</a>")

    return render_template('index.html', data=data, user=session['user'], type=session['type'])


@app.route('/close', methods=['POST'])
def close():
    session.clear()
    return redirect('/login')


@app.route('/users', methods=['GET', 'POST'])
def users():
    users = DDBBProcess.readUsers()
    
    if request.method == "POST":
        name=request.form['name']
        passw=request.form['pass']
        type=request.form['type']
        res= DDBBProcess.addUser(name, passw, type)
        if res == 1:
            flash("usuario registrado correctamente")
        if res == 0:
            flash ("Error: Usuario duplicado")
        
        users = DDBBProcess.readUsers()
        return render_template('users.html', titulo="UserAdmin", users=users)


    if request.method == "GET":
        id = request.args.get('eliminar')
        DDBBProcess.deleteUser(id)
        users = DDBBProcess.readUsers()            
        return render_template('users.html', titulo="UserAdmin", users=users)

    return render_template('users.html', titulo="UserAdmin", users=users)



if __name__ == '__main__':
    app.run(port=8000, debug=True)
 