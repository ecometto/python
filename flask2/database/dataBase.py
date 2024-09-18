import sqlite3


def connect():
    conn = sqlite3.connect('./database/DDBB.sqlite')
    return conn


def getAll():
    conn = connect()
    conn.row_factory = sqlite3.Row  # Esto hará que las filas sean accesibles por nombre de columna
    cur = conn.cursor()
    sql = "SELECT s.id, s.title, s.autor, g.genre, s.lyric from songs as s join genres as g on s.genre = g.id"
    query = cur.execute(sql)
    data = query.fetchall()
    print(data)
    conn.close()
    return data

def getById(id):
    conn = connect()
    conn.row_factory = sqlite3.Row  # Esto hará que las filas sean accesibles por nombre de columna
    cur = conn.cursor()
    sql = f"SELECT s.id, s.title, s.autor, g.genre, s.lyric from songs as s join genres as g on s.genre = g.id where s.id = {id} "
    query = cur.execute(sql)
    data = query.fetchone()
    conn.close()
    return data

def create(song):
    conn = connect()
    cur = conn.cursor()
    sql = "insert into songs(title, autor, genre, lyric) values (?,?,?,?)"
    cur.execute(sql, (song['title'], song['autor'], int(song['genre']) , song['lyric']))
    conn.commit()
    conn.close()

def update(song):
    conn = connect()
    cur = conn.cursor()
    cur.execute(f"update songs set title={song.title} autor={song.autor} genre={song.genre} lyric={song.lyric} where id={song.id}")
    conn.commit()
    conn.close()
    
    
def delete(id):
    conn = connect()
    cur = conn.cursor()
    cur.execute(f"delete from songs where id = {id}")
    conn.commit()
    conn.close
    
def getGenres():
    conn = connect()
    conn.row_factory = sqlite3.Row  # Esto hará que las filas sean accesibles por nombre de columna
    cur = conn.cursor()
    sql = "SELECT * from genres"
    query = cur.execute(sql)
    data = query.fetchall()
    print(data)
    conn.close()
    return data

# conn = connect()
# cur = conn.cursor()
# sql = "insert into genres(genre) values ('Tango')"
# cur.execute(sql)
# conn.commit()
# conn.close()
    
    
    
# def create_table_genres():
#     sql = """create table genres (
#                                 id integer primary key autoincrement,
#                                 genre text
#                                 )"""
#     conn = connect()
#     conn.execute(sql)
#     conn.commit()
#     print("table created??")
#     conn.close()
    
    
# def create_table_songs():
#     sql = """create table songs (
#                                 id integer primary key autoincrement,
#                                 title text,
#                                 autor text,
#                                 genre int,
#                                 lyric text,
#                                 FOREIGN KEY (genre) references genres(id)
#                                 )"""
#     conn = connect()
#     conn.execute(sql)
#     conn.commit()
#     conn.close()
    