from flask import Flask, render_template, url_for, request
import sqlite3

app=Flask(__name__)

def conectar():
    con=sqlite3.connect("personas.sqlite")
    # cursor=con.cursor()
    # cursor.execute(" create table if not exists personas (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre varchar(50), edad int, mail varchar(50))")
    return con



# ------------------------------------------- 
# definiendo rutas 
@app.route("/")
def index():
    con=conectar()
    sql="select * from personas"
    cursor=con.cursor()
    cursor.execute(sql)
    data=cursor.fetchall()
    print(data)
    con.close
    return render_template("index.html", titulo="principal", data=data)
    

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
    return render_template("formulario.html", titulo="formulario")



# --------------------------------------- 
#ejecutando el servidor
if __name__ == "__main__":
    app.run(port=3000, debug=True)
