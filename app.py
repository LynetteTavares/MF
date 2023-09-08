from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    print("Hello Ladies and Genitals")
    print("This is MovieFindr")
    return
