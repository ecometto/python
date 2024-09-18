from flask import Flask, render_template, request, redirect, url_for
import database.dataBase as dataBase


app = Flask(__name__)

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', title='Welcome!!')

@app.route('/list', methods=['GET'])
def list():
    data = dataBase.getAll()
    print(data)
    return render_template('list.html', title='', data=data)

@app.route('/details/<song>',methods=['GET'])
def detail(song):
    song=dataBase.getById(song)
    print(song)
    return render_template('songdetails.html', song=song)

@app.route('/manage',methods=['GET'])
def manage():
    data = dataBase.getAll()
    genres = dataBase.getGenres()
    return render_template('manage.html', data=data, genres=genres)

@app.route('/create',methods=['POST'])
def create():
    song = {
        "title": f"{request.form.get('title')}",
        "autor": f"{request.form.get('autor')}",
        "genre": f"{request.form.get('genre')}",
        "lyric": f"{request.form.get('lyric')}"
    }
    print(request.form)
    dataBase.create(song)
    return redirect(url_for('manage'))

@app.route('/delete/<id>',methods=['GET'])
def delete(id):
    dataBase.delete(id)
    return redirect(url_for('manage'))

@app.route('/edit/<id>', methods=['GET'])
def edit(id):
    songData = dataBase.getById(id)
    return render_template('edit.html', songData=songData)


# @app.route('/contact', methods=['GET'])
# def contact():
#     return render_template('contact.html', title='Contact Form')






if __name__ == '__main__':
    app.run(debug=True, port=5000)
    