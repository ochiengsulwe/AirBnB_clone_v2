#!/usr/bin/python3
"""Start a Flask web applicaton"""

from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Routing to root, strict_slashes ensure
    the URL works when it ends both with or without the /
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Routing to /hbnb, strict_slashes ensure
    the URL works when it ends both with or without the /
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """Routing to C using Variables"""
    text = text.replace('_', ' ')
    return f"C {excape(text)}"


@app.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text):
    """Routing to python with default value using Variables"""
    text = text.replace('_', ' ')
    return f"Python {escape(text)}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
