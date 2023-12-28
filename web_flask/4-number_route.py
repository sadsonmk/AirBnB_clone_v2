#!/usr/bin/python3
"""This is a script that starts a Flask web application
    displays “n is a number” only if n is an integer
"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display(text):
    new_text = replace('_', ' ')
    return f'C {new_text}'


@app.route("/python", strict_slashes=False, defaults={"text": 'is cool'})
@app.route("/python/<text>", strict_slashes=False)
def iscool(text):
    new_text = text.replace('_', ' ')
    return f'Python {new_text}'


@app.route("/number/<int:n>", strict_slashes=False)
def display_n(n):
    return f'{n} is a number'


port = 5000
host = '0.0.0.0'

if __name__ == '__main__':
    app.run(debug=True, host=host, port=port)
