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


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_cool(text):
    """Prints Python plus the string argument."""
    text = text.replace('_', ' ')
    return f"Python {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def int_check(n):
    """Only returns n if n is of type int."""
    if isinstance(n, int):
        return f"{n} is a number"
    else:
        return "404"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n=None):
    """Renders a HTML page"""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
