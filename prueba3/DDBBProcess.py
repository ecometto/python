import sqlite3

def clearDDBB():
    con=sqlite3.connect("./prueba3/DDBB.sqlite")
    cursor=con.cursor()
    sql=f"delete from datos"
    cursor.execute(sql)
    con.commit()
    con.close
    
# clearDDBB()


def uploadData(data):
    con=sqlite3.connect("./prueba3/DDBB.sqlite")
    cursor=con.cursor()

    for cada in data:
        sql=f"insert into datos values ( {cada[0]} , '{cada[1]}' , '{cada[2]}' )"
        cursor.execute(sql)
        con.commit()
        
    con.close