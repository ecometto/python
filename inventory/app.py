from flask import Flask, render_template, url_for, request, redirect
import DDBBUsers , DDBBArticulos

app=Flask(__name__)

# DEFINICIÓN DE RUTAS --------------------------------
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        user = request.form['user']
        password = request.form['pass']
        data=DDBBUsers.validar(user, password)
        print(data)
        print(len(data))
        if len(data) == 1 :
           return redirect("/index")       
    return render_template("login.html")


@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/altaArticulos', methods=['GET', 'POST'])
def altaArt():    
    if request.method == "POST":
        descripcion = request.form['descripcion']
        marca = request.form['marca']
        umedida = request.form['umedida']
        res = DDBBArticulos.insertArticle(descripcion, marca, umedida)
        if res == 1:
            print("insertado correctamente")
        else:
            print("error al cargar")
        
    return render_template("./articulos/alta.html", titulo="alta Articulos")

@app.route('/listadoArticulos', methods=['GET', 'POST'])
def listadoArt():    
    action=request.form
    for cada in action.items():
        if cada[0] == "editar":
            data=DDBBArticulos.readArticle(cada[1])
            return render_template("./articulos/editar.html",titulo="editarArticulos", data=data)
        elif cada[0]== "eliminar":
            DDBBArticulos.deleteArticles(cada[1])

    data = DDBBArticulos.readArticles()        
    return render_template("./articulos/listado.html", titulo="Lista Articulos", data=data)

@app.route('/editarArticulos', methods=['GET', 'POST'])
def editarArticulos():
    return render_template("./articulos/editar.html",titulo="editarArticulos")


if __name__ == "__main__":
    app.run(port=5000, debug=True)

