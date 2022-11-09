from flask import Flask, render_template, session, redirect, request
import sqlite3

# importing files 
import XMLProcess as XML
import DDBBProcess 

app = Flask(__name__)
app.secret_key="clave secreta"

def getData():
    # extracting data from the File 
    data= XML.readFile()

    # Clearing DataBase and storaging new data 
    DDBBProcess.clearDDBB()
    DDBBProcess.uploadData(data)


    #reading database
    con=sqlite3.connect("./prueba3/DDBB.sqlite")
    cursor=con.cursor()
    sql="select * from data"
    cursor.execute(sql)
    datos = cursor.fetchall()
    con.close
    return datos


@app.before_request
def validar():
    ruta = request.endpoint
    if 'user' not in session and ruta != 'login':
        print(request.endpoint)
        return redirect('/login')
    print(request.endpoint)
    

@app.route('/')
def index():
    print(request.endpoint)
    data=getData()
    return render_template('index.html', data=data)
    # if 'user' in session:
    #     data=getData()
    #     return render_template('index.html', data=data)
    # else:
    #     return redirect('/login')


@app.route('/close', methods=['POST'])
def close():
    session.clear()
    return redirect('/login')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        user=request.form['user']
        password=request.form['password']
        res = DDBBProcess.verifyingUser(user, password)
        session['user']= user
        if res != None:
            return render_template('index.html')

    return render_template('login.html')


if __name__ == '__main__':
    app.run(port=8000, debug=True)
 