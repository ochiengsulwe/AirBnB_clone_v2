#!/usr/bin/python3
"""Starts a Flask we application."""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Routing to root, with strict_slashes to ensure the URL works when
        when it ends both with or without the `/`.
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
