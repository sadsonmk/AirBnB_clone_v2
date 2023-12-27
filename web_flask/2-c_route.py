#!/usr/bin/python3
"""This is a script that starts a Flask web application
    displaying “C ” followed by the value of the text variable
"""

from flask import Flask
port = 5000
host = '0.0.0.0'

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display(text):
    new_text = text.replace('_', ' ')
    return f'C {new_text}'


if __name__ == '__main__':
    app.run(debug=True, host=host, port=port)
