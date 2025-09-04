from flask import Blueprint, url_for, render_template

home = Blueprint('home', __name__, template_folder='templates')


@home.route("/")
def index():
    return render_template("index.html")


@home.route("/about")
def about():
    return render_template("about.html")


@home.route("/projects")
def projects():
    return render_template("projects.html")


@home.route("/blogs")
def blogs():
    return render_template("blogs.html")



@home.route("/blog/<blog>")
def blog(blog):
    # TODO: extend base.html, perhaps from this funciton call
    return render_template(f"blogs/{blog}.html")

