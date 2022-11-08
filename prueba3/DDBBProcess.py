import sqlite3

def clearDDBB():
    con=sqlite3.connect("./prueba3/DDBB.sqlite")
    cursor=con.cursor()
    sql=f"delete from data"
    cursor.execute(sql)
    con.commit()
    con.close
    
# clearDDBB()


def uploadData(data):
    con=sqlite3.connect("./prueba3/DDBB.sqlite")
    cursor=con.cursor()
    for cada in data:
        # sql=f"insert into data values ( {cada[0]} , '{cada[1]}' , '{cada[2]}' )"
        sql=f"insert into data values ( null, {cada[0]} , '{cada[1]}' , '{cada[2]}', '{cada[3]}' )"
        cursor.execute(sql)
    con.commit()
    con.close

def verifyingUser(user, password):
    con=sqlite3.connect("./prueba3/DDBB.sqlite")
    cursor=con.cursor()
    cursor.execute(f"select * from users where name='{user}' and pass='{password}'")
    data= cursor.fetchone()
    con.close()
    print(data)
    return data
    





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

