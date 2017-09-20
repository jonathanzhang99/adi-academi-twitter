from flask import render_template
from . import routes

@routes.route('/', methods=["GET", "POST"])
def home():
    return render_template('home.html')
