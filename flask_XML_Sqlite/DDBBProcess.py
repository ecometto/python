import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from flask import flash

rutaDDBB="./flask_XML_Sqlite/DDBB.sqlite"

def clearDDBB():
    con=sqlite3.connect(rutaDDBB)
    cursor=con.cursor()
    sql=f"delete from data"
    cursor.execute(sql)
    con.commit()
    resetId="UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='data'"
    cursor.execute(resetId)
    con.commit()
    con.close
    
# clearDDBB()


def uploadData(data):
    con=sqlite3.connect(rutaDDBB)
    cursor=con.cursor()
    for cada in data:
        sql=f"insert into data values ( null, {cada[0]} , '{cada[1]}' , '{cada[2]}', '{cada[3]}' )"
        cursor.execute(sql)
    con.commit()
    con.close
   

def readData():
    con=sqlite3.connect(rutaDDBB)
    cursor=con.cursor()
    sql="select * from data"
    cursor.execute(sql)
    datos = cursor.fetchall()
    con.close
    return datos


def readPartialData():
    con=sqlite3.connect(rutaDDBB)
    cursor=con.cursor()
    sql="select * from data where Type LIKE '%DataTake%'" 
    cursor.execute(sql)
    datos = cursor.fetchall()
    con.close
    return datos
# readPartialData()


def verifyingUser(user, password):
    con=sqlite3.connect(rutaDDBB)
    cursor=con.cursor()
    cursor.execute(f"select * from users where name='{user}' and pass='{password}'")
    data= cursor.fetchone()
    con.close()
    return data

def verifyingEncriptedUser(user, password):
    con=sqlite3.connect(rutaDDBB)
    cursor=con.cursor()
    cursor.execute(f"select * from users where name='{user}'")
    data= cursor.fetchone()
    if not data is None:
        if  check_password_hash(data[2], password):
            con.close()
            return data
        
def addUser(name, passw, type):
    con=sqlite3.connect(rutaDDBB)
    cursor=con.cursor()
    cursor.execute('select name from users')
    users=cursor.fetchall()
    for cada in users:
        if name == cada[0]:
            return 0
        
    passw=generate_password_hash(passw)
    cursor.execute(f"insert into users values(NULL, '{name}','{passw}','{type}')")
    res=cursor.rowcount
    con.commit()
    con.close()
    return res

    

con=sqlite3.connect(rutaDDBB)
cursor=con.cursor()
sql="update users set pass='pbkdf2:sha256:260000$dZgrdYyAB5ai7QOu$13cecafba866bf99912e3afbedb923703d780c9236411e730d0d5d430be0d2c7' where id=2" 
cursor.execute(sql)
con.commit()
con.close




#creando nueva tabla (a duplicar / modificar)
# con = sqlite3.connect("./prueba3/DDBB.sqlite")
# cursor = con.cursor()
# sql=" create table data (id INTEGER PRIMARY KEY AUTOINCREMENT, refIf varchar(50), TimeStart varchar(50), TimeEnd varchar(50))"
# cursor.execute(sql)
# con.commit()
# con.close()

#copiando datos de una tabla a otra
# con = sqlite3.connect("./prueba3/DDBB.sqlite")
# cursor = con.cursor()
# sql="INSERT INTO data (refIf, TimeStart, TimeEnd ) SELECT * FROM datos"
# cursor.execute(sql)
# con.commit()
# con.close()

#elimino la tabla "defectuosa"
# con = sqlite3.connect("./prueba3/DDBB.sqlite")
# cursor = con.cursor()
# sql="drop table datos"
# cursor.execute(sql)
# con.commit()
# con.close()




#VER CURSOR.EXECUTE MANY PARA INGRESAR TODOS JUNTOS

