from flask import Flask, render_template
import json
import sqlite3

app=Flask(__name__)

# ------------------------------------------------------- 
# DDBB consulting
try:
    con=sqlite3.connect("./proyectoFlaskSqlite/DDBB.sqlite")
    cursor = con.cursor()
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
    cursor.execute(f"insert into articulos values (null, '{nombre}', '{marca}', '{modelo}')")
    con.commit()
# insert("art3", "marca3", "modelo3")

# Getting data -----------
def read():
    cursor.execute("select * from articulos")
    data = cursor.fetchall()
    return data
# read()

# Getting data -----------
def update(id, campo, valor):
    cursor.execute(f"update articulos set {campo}='{valor}' where id={id}")
    con.commit()
# update(5,"", "modelo4")

# deleting data -----------
def delete(id):
    cursor.execute(f"delete from articulos where id={id}")
    con.commit()
# delete(4)



# ------------------------------------------------------ 
# ------------------------------------------------------ 
#routes and templates
ArticlesList=read()
print(ArticlesList)

@app.route("/")
def index():
    listaArticulos=ArticlesList
    return render_template("index.html", li = listaArticulos, titulo="PRINCIPAL")

@app.route("/form")
def form():
    return render_template("form.html", titulo="FORMULARIO")


con.close()

if __name__ == "__main__":
    app.run(port=3000, debug=True)
