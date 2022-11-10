import sqlite3

try:
    con=sqlite3.connect("./proyectoFlaskSqlite/DDBB.sqlite", check_same_thread=False)
    
except Exception:
    print(Exception)

cursor=con.cursor()
cursor.execute("delete from sqlite_sequence where name='articulos'")
con.commit()
con.close()