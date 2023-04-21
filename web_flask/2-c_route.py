#!/usr/bin/python3
"""
a script that starts a Flask web application
"""
from flask import Flask, escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """sends a GET request to the homepage"""
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """sends a GET request to the hbnb page"""
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    """sends a GET request to the hbnb page"""
    return ('C %s' % escape(text.replace('_', ' ')))


if __name__ == '__main__':
    # I know there is no need for 'port=5000' just bored.
    app.run(debug=True, port=5000)
