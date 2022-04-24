from flask import Flask

from prontuariofacil.ext import view
from prontuariofacil.ext import database
from prontuariofacil.ext import config
from prontuariofacil.ext import cli

def create_app():
    app = Flask(__name__)
    config.init_app(app)
    database.init_app(app)
    cli.init_app(app)
    view.init_app(app)
    @app.route('/')
    def comeco():
        return "comeco"
    return app
    