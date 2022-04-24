from flask import Flask ,render_template

from prontuariofacil.ext import view

def create_app():
    app = Flask(__name__)
    view.init_app(app)
    return app
    