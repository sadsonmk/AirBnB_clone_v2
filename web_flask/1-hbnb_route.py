#!/usr/bin/python3
"""This is a script that starts a Flask web application which has two routes
"""

from flask import Flask
app = Flask(__name__)

port = 5000
host = '0.0.0.0'


@app.route("/", strict_slashes=False)
def index():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


if __name__ == '__main__':
    app.run(debug=True, host=host, port=port)
