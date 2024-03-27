#!/usr/bin/python3
"""Starts a Flask web application."""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Returns a simple greeting."""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display():
    """Displays a simple String type."""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """Prints C is fun.

        Replaces '_' with white space.
    """
    text = text.replace('_', ' ')
    return f"C {text}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)