#!/usr/bin/python3
"""
a script that starts a Flask web application
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """sends a GET request to the homepage"""
    return ("Hello HBNB!")


if __name__ == '__main__':
    app.run(debug=True, port=5000)
