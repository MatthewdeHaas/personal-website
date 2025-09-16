import os
from flask import Blueprint, url_for, render_template
from pathlib import Path
from bs4 import BeautifulSoup

home = Blueprint('home', __name__, template_folder='templates')


@home.route("/")
def index():
    return render_template("index.html")


@home.route("/projects")
def projects():
    return render_template("projects.html")


@home.route("/blogs")
def blogs():

    posts = [name.replace(".html", "") for name in os.listdir("app/static/media/blogs")]

    return render_template("blog-base.html", posts=posts)


@home.route("/blog/<post>")
def blog(post):
   
    file = Path(f"app/static/media/blogs/{post}.html")
    if not file.exists():
        return "Post not found", 404

    content = file.read_text(encoding="utf-8")   

    return render_template("blog.html", content=content) 



