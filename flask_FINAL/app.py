from flask import Flask
from flask import render_template, request, session, redirect, url_for

import login as lg

app=Flask(__name__)
app.secret_key="ecometto"


#  ROUTES ----------------

@app.before_request
def validarSession():
    if not 'nombre' in session and request.endpoint not in ['login']:
        redirect('/login')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method =="POST":
        nombre=request.form['nombre']
        passw=request.form['passw']
        res=lg.validar(nombre, passw)
        print(res)
        if res == 1:
            session['user']=nombre
            return redirect('/')
        
            
    
    
    return render_template('login.html')

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.clear()
    return redirect(url_for('login'))
    # return redirect('/login')

    
if __name__ == "__main__":
    app.run( port=3000, debug=True)
 