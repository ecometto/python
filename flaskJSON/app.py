from flask import Flask, render_template, session, redirect, request

import ProcessJSON

app=Flask(__name__)
app.secret_key="secreta"


#geting data from json file
data=ProcessJSON.getData()


# ------------- rutas ------------------
@app.before_request
def validarUser():
    if "user" not in session:
        print("no loged")
    if "user" not in session and request.endpoint != 'login' and '/static/' not in request.path:
        return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        us = request.form['user']
        pa = request.form['pass']
        res=ProcessJSON.validarUser(us,pa)
        if res:
            session['user'] = us
            session['type']= res['type']
            return redirect('/')

    return render_template('login.html')

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', title="Principal", data=data)

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.clear()
    return redirect('/login')

@app.route('/search', methods=['GET', 'POST'])
def search():
    pass





if __name__ == "__main__":
    app.run(port=3000, debug=True)