from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return 'Bienvenidos a Programacion II !!'

@app.route("/about")
def hello_world():
    return 'Acerca de '
