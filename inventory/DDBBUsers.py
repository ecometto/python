import sqlite3
from flask import Flask, request

#CREANDO LA TABLA USUARIOS
# con=sqlite3.connect("./inventory/usuarios.sqlite")
# cursor=con.cursor()
# sql="create table if not exists usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT, usuario VARCHAR(50), pass VARCHAR(100))"
# cursor.execute(sql)
# con.close()

def insertUser(usuario, password):
    con=sqlite3.connect("./inventory/usuarios.sqlite", check_same_thread=False)
    cursor=con.cursor()
    sql=f"insert into usuarios values(null, '{usuario}','{password}')"
    cursor.execute(sql)
    con.commit()
    con.close()
# insertUser("ecometto@hotmail.com", "123")
# insertUser("ecometto@vengsa.com.ar", "123")
# insertUser("123", "123")

def readUsers():
    con=sqlite3.connect("./inventory/usuarios.sqlite", check_same_thread=False)
    cursor=con.cursor()
    sql=f"select * from usuarios"
    cursor.execute(sql)
    data = cursor.fetchall()
    print(data)
    con.close()
# readUsers()

def validar(user, password):
    con=sqlite3.connect("./inventory/usuarios.sqlite", check_same_thread=False)
    cursor=con.cursor()
    sql=f"select * from usuarios where usuario = '{user}' and pass='{password}' "
    cursor.execute(sql)
    data = cursor.fetchall()
    print(data)
    con.close()
    return data


def deleteUser(id):
    con=sqlite3.connect("./inventory/usuarios.sqlite", check_same_thread=False)
    cursor=con.cursor()
    sql=f"delete from usuarios where id = {id}"
    cursor.execute(sql)
    con.commit()
    con.close()
# deleteUser(1)