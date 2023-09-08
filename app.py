from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    print("Ladies and genitals")
    print("Welcome to MovieFindr")
    return
