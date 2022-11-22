import sqlite3

class Usuarios():
    def __init__(self) -> None:
        con = sqlite3.connect("./repaso/DDBBPOO.db")
        sql="create table users if not exists"
        return con
        
    def newUser( name, age):
        cur = self.db.cursor()
        sql = f"insert into usuarios values('NULL, {name}, {age}, True)"
        cur.execute(sql)
        con.commit()
        con.close()
        
    def showUsers(self):
        cur =self.con.cursor()
        sql="select * from users"
        data = cur.execute()
        self.con.close()
        return data

Usuarios.newUser()