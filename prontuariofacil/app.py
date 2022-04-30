from flask import Flask

from ext import view
from ext import database
from ext import config
from ext import cli

def create_app():
    app = Flask(__name__)
    config.init_app(app)
    database.init_app(app)
    cli.init_app(app)
    view.init_app(app)
    return app
    