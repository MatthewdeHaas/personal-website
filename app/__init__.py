import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, static_folder="")

    # register blueprints
    from app.routes import home
    app.register_blueprint(home)

    return app
