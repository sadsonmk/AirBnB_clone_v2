#!/usr/bin/python3
"""This is a script that starts a Flask web
    application display a HTML page only if n is an integer:
    H1 tag: “Number: n is even|odd” inside the tag BODY
"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display(text):
    new_text = text.replace('_', ' ')
    return f'C {new_text}'


@app.route('/python', strict_slashes=False, defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def is_cool(text):
    new_text = text.replace('_', ' ')
    return f'Python {new_text}'


@app.route('/number/<int:n>', strict_slashes=False)
def display_n(n):
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_temp(n):
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def even_odd(n):
    return render_template('6-number_odd_or_even.html', number=n)


port = 5000
host = '0.0.0.0'

if __name__ == '__main__':
    app.run(debug=True, host=host, port=port)
