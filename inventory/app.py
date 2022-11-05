from flask import Flask, render_template, url_for, request, redirect, session, flash
import DDBBUsers , DDBBArticulos

app=Flask(__name__)
app.secret_key = 'username'
# session['user']=None

# DEFINICIÓN DE RUTAS --------------------------------
@app.route('/close', methods=['GET', 'POST'])
def close():
    session.clear()
    return redirect(url_for("login"))


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        user = request.form['user']
        password = request.form['pass']
        data=DDBBUsers.validar(user, password)
        if len(data) == 1 :
            session["user"] = data[0][1]
            if "user" in session:
                print("usuario: ", user)
                return redirect(url_for("index"))

    return render_template("login.html",titulo="login")  



@app.route('/index', methods=['GET', 'POST'])
def index():
    if "user" in session:
        return render_template("index.html", titulo="Principal", usuario=session['user'])
    else:
        return redirect(url_for("login"))
        # return redirect("/")



@app.route('/altaArticulos', methods=['GET', 'POST'])
def altaArt():    
    if request.method == "POST":
        descripcion = request.form['descripcion']
        marca = request.form['marca']
        umedida = request.form['umedida']
        res = DDBBArticulos.insertArticle(descripcion, marca, umedida)
        if res == 1:
            flash("articulo ingresado correctamente")
        else:
             flash("aError al cargar")
             
    return render_template("./articulos/alta.html", titulo="alta Articulos")


@app.route('/listadoArticulos', methods=['GET', 'POST'])
def listadoArt():    
    action=request.form
    for cada in action.items():
        if cada[0] == "editar":
            return redirect(url_for("editarArticulos", id=cada[1]))

        elif cada[0]== "eliminar":
            DDBBArticulos.deleteArticles(cada[1])
            flash("Articulo eleminado correctamente")

    data = DDBBArticulos.readArticles()        
    return render_template("./articulos/listado.html", titulo="Lista Articulos", data=data)


@app.route('/editArt/<id>', methods=['GET', 'POST'])
def editarArticulos(id):
    
    if request.method == "POST":
        print("enviando")
        id = request.form['id']
        descripcion = request.form['descripcion']
        marca = request.form['marca']
        umedida = request.form['umedida']
        print(id, descripcion,  marca, umedida) 
        res = DDBBArticulos.editArticles(id, descripcion, marca, umedida)
        print(res)
        if res == 1:
            flash("Registro modificado correctamente")
            return render_template("./articulos/listado.html",titulo="Listado")
             
    data=DDBBArticulos.readArticle(id)
    return render_template("./articulos/editar.html",titulo="Editando", data=data)



if __name__ == "__main__":
    app.run(port=5000, debug=True)

