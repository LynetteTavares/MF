from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1>Hello Ladies and Genitals! This is MovieFindr!</h1>'
