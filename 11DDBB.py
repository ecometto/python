import sqlite3

conn = sqlite3.connect('aaaa.db')

cursor = conn.cursor()

query = 'select * from users'

cursor.execute(query)
cursor.fetchall()

conn.commit()

conn.close()