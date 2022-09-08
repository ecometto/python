import sqlite3

conn = sqlite3.connect('aaa.db')
cursor = conn.cursor()

# ----------- creating table -------------- 
# query = 'create table users (id integer primary key autoincrement, mail varchar(100), pass varchar(100))'


# -------- insert data -----------
# insert = "insert into users (mail, pass) values ('ecometto', '123'),('edgardo', '123456'),   ('edicom', '1234')"
# cursor.execute(insert)
# conn.commit()


# --------- show data ----------- 
# select = 'select * from users'
# cursor.execute(select)
# data = cursor.fetchall()
# for dato in data:
#     print(dato)


# ---------- editing data ------------ 
# update = "update users set mail = 'ecometto@hotmail.com' where id = 1"
# cursor.execute(update)
# conn.commit()


# -------- deleting data ----------
# delete = "delete from users where id = 2"
# cursor.execute(delete)
# conn.commit()



conn.close()































# import sqlite3

# conn = sqlite3.connect('aaaa.db')

# cursor = conn.cursor()

# select = 'select * from users'
# # insert = "insert into users (descripcion) values ('Edi'), ('romeo'),('Martin')"

# # insertmultiple = "insert into users (descripcion) values (?)"
# # LISTAMULTIPLE = [('jUAN'), ('pEDRO'), ('Mar')]
# # cursor.executemany(insertmultiple, LISTAMULTIPLE)

# cursor.execute(select)

# data = cursor.fetchall()
# for d in data :
#     print(d[1])
    
# conn.commit()

# conn.close()