from re import U, template
import sqlite3
from flask import Flask, request, render_template, redirect, url_for


app=Flask(__name__)

# ------------------------------------------------------- 
# DDBB consulting
def conectar():
    try:
        con=sqlite3.connect("./proyectoFlaskSqlite/DDBB.sqlite") #, check_same_thread=False
        # cursor = con.cursor()
        return con
    except Exception:
        print(Exception)

# ------------------------------------------------------------ 
# ------------------------------------------------------------ 
# INTERACTING WITH DATABASE  
#creating the table (JUST ONCE)
# cursor.execute("create table articulos (id integer primary key autoincrement, nombre varchar(50), marca varchar(50), modelo varchar(50))")

# --------------- FUNCIONES CRUD ----------------- 
# inserint data ---------
def create(nombre, marca, modelo):
    con=conectar()
    cursor=con.cursor()
    cursor.execute(f"insert into articulos values (null, '{nombre}', '{marca}', '{modelo}')")
    con.commit()
    con.close()
# insert("art3", "marca3", "modelo3")

# Getting data -----------
def read():
    # con=conectar()
    con=sqlite3.connect("./proyectoFlaskSqlite\DDBB.sqlite", check_same_thread=False)
    cursor=con.cursor()
    cursor.execute("select * from articulos")
    data = cursor.fetchall()
    return data
    con.close()
# read()

def readId(id):
    con=conectar()
    cursor=con.cursor()
    cursor.execute(f"select * from articulos where id={id}")
    data = cursor.fetchall()
    return data[0]
    con.close()
# read()

# Getting data -----------
def update(id, nombre, marca, modelo):
    con=conectar()
    cursor=con.cursor()
    cursor.execute(f"update articulos set nombre='{nombre}', marca='{marca}', modelo='{modelo}' where id={id}")
    con.commit()
    con.close()
# update(5,"", "modelo4")

# deleting data -----------
def delete(id):
    con=conectar()
    cursor=con.cursor()
    cursor.execute(f"delete from articulos where id={id}")
    con.commit()
    con.close()
# delete(4)



# ------------------------------------------------------ 
# ------------------------------------------------------ 
#routes and templates


@app.route("/", methods=['GET', 'POST'])
def index():
    ArticlesList=read()
    # print(ArticlesList)
    listaArticulos=ArticlesList
    return render_template("index.html", li = listaArticulos, titulo="PRINCIPAL")

@app.route("/form", methods=['GET', 'POST'])
def form():
    if request.method == "POST":
        nombre= request.form['nombre']
        marca= request.form['marca']
        modelo= request.form['modelo']
        print(f"{nombre} - {marca} - {modelo}")
        create(nombre, marca, modelo)
        return redirect(url_for("index"))
    
    return render_template("form.html", titulo="formulario")

@app.route("/delete/<id>")
def deletePage(id):
    delete(id)
    return redirect(url_for("index"))
    
@app.route("/edit/<id>", methods=['GET' , 'POST'])
def editPage(id):
    data=readId(id)
    print(f" tipo: {type(data)}: {data}")
    if request.method=='POST':
        id=request.form['id']
        nombre= request.form['nombre']
        marca= request.form['marca']
        modelo= request.form['modelo']
        update(id, nombre, marca, modelo)
        return redirect(url_for("index"))

    return render_template("update.html", data=data)
    





if __name__ == "__main__":
    app.run(port=3000, debug=True)
