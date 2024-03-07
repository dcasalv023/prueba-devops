# -*- coding: utf-8 -*-
"""
This module contains the Flask application.
"""

from datetime import datetime
import locale
from flask import Flask, render_template

app = Flask(__name__)
locale.setlocale(locale.LC_TIME, '')

@app.route('/')
def homepage():
    """
    Render the homepage with current time and a random theme.
    """
    the_time = datetime.now().strftime("%A, %d %b %Y %H:%M")
    return render_template("index.html", the_time=the_time, tema="dogs")

@app.route('/status')
def status():
    """
    Returns OK status.
    """
    return "OK Todo"

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)


