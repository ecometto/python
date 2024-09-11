from flask import Flask, render_template

app = Flask(__name__)

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


@app.route('/', methods=['GET'])
def index():
    data={'title':'Cancionero'}
    return render_template('index.html', data=data)



if __name__ == '__main__':
    app.run(debug=True)
    