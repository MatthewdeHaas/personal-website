from flask import Blueprint, url_for, render_template

home = Blueprint('home', __name__, template_folder='templates')

@home.route("/")
def index():
    return render_template("index.html")