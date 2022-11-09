from flask import Flask, render_template, session, redirect, request, flash

# importing module 
import JSON

app = Flask(__name__)

@app.before_request
def validarSession():
    ruta = request.endpoint
    print(ruta)
    if 'user' not in session and ruta != 'login':
        # print("not in session")
        return redirect('/login')
    else:
        print("sssiiii")

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        # user = request.form['user']
        # password = request.form['password'"]
        user = "Edgardo"
        password = "123"
        res = JSON.validarUser(user, password)
        if res != "error" and res != 0:
            session['user']= user
            print("Usuario: ",session['user'])
            redirect("/")
            
    return render_template('login.html')







@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 