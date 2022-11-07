from flask import Flask, render_template
import sqlite3

# importing files 
import XMLProcess as XML
import DDBBProcess 

app = Flask(__name__)

# extracting data from the File and storaging in DataBase

# data= XML.readFile()
# DDBBProcess.uploadData(data)


#reading database
con=sqlite3.connect("./prueba3/DDBB.sqlite")
cursor=con.cursor()
sql="select * from datos"
cursor.execute(sql)
datos = cursor.fetchall()
con.close

@app.route('/')
def index():
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(port=8000, debug=True)
 