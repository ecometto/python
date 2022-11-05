import sqlite3
from flask import Flask, request

#CREANDO LA TABLA USUARIOS
# con=sqlite3.connect("./inventory/articulos.sqlite")
# cursor=con.cursor()
# sql="create table if not exists articulos (id INTEGER PRIMARY KEY AUTOINCREMENT, descripcion VARCHAR(50), marca VARCHAR(50), umedida VARCHAR(50), estado BOOLEAN)"
# cursor.execute(sql)
# con.close()

def insertArticle(descripcion, marca, umedida):
    con=sqlite3.connect("./inventory/articulos.sqlite", check_same_thread=False)
    cursor=con.cursor()
    sql=f"insert into articulos values(null, '{descripcion}','{marca}', '{umedida}', 1)"
    cursor.execute(sql)
    con.commit()
    res=cursor.rowcount
    con.close()
    return res


def readArticles():
    con=sqlite3.connect("./inventory/articulos.sqlite", check_same_thread=False)
    cursor=con.cursor()
    sql=f"select * from articulos"
    cursor.execute(sql)
    data = cursor.fetchall()
    con.close()
    return data

def readArticle(id):
    con=sqlite3.connect("./inventory/articulos.sqlite", check_same_thread=False)
    cursor=con.cursor()
    sql=f"select * from articulos where id = {id}"
    cursor.execute(sql)
    data = cursor.fetchall()
    con.close()
    return data[0]

def deleteArticles(id):
    con=sqlite3.connect("./inventory/articulos.sqlite", check_same_thread=False)
    cursor=con.cursor()
    sql=f"delete from articulos where id = {id} "
    cursor.execute(sql)
    res=cursor.rowcount
    con.commit()
    con.close()
    print(res)
    return res

def editArticles(id, descripcion, marca, umedida):
    con=sqlite3.connect("./inventory/articulos.sqlite", check_same_thread=False)
    cursor=con.cursor()
    sql=f"update articulos set descripcion = '{descripcion}', marca = '{marca}', umedida = '{umedida}' where id = {id} "
    cursor.execute(sql)
    res=cursor.rowcount
    print("resultado - ", res)    
    con.commit()
    con.close()
    return res
