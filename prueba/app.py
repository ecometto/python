from flask import Flask, render_template, url_for, request, flash, session, redirect
import sqlite3

app=Flask(__name__)

def conectar():
    con=sqlite3.connect("./prueba/personas.sqlite")
    # cursor=con.cursor()
    # cursor.execute(" create table if not exists personas (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre varchar(50), edad int, mail varchar(50))")
    return con

app.secret_key="ecometto key"

# ------------------------------------------- 
# definiendo rutas 


@app.route('/login', methods=['POST'])
def login():
      if request.method == "POST":
        print("llega post")

@app.route('/', methods=['POST'])
def index():
    
    if 'user' in session:
        con=conectar()
        sql="select * from personas"
        cursor=con.cursor()
        cursor.execute(sql)
        data=cursor.fetchall()
        print(data)
        con.close
        return render_template("index.html", titulo="principal", data=data)
    else:
        return redirect(url_for("login"))
    

@app.route("/form", methods=['POST', 'GET'])
def form():
    if request.method == 'POST':
        nombre=request.form['nombre']
        edad= request.form['edad']
        mail= request.form['mail']
        con=conectar()
        sql=f"insert into personas values(null,'{nombre}',{edad},'{mail}')"
        cursor=con.cursor()
        cursor.execute(sql)
        con.commit()
        con.close
        flash("persona ingresada correctamente")
    return render_template("formulario.html", titulo="formulario")



# --------------------------------------- 
#ejecutando el servidor
if __name__ == "__main__":
    app.run(port=5000, debug=True)
