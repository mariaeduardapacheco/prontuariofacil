import click
from ext.database import db
from ext.models import tables

def init_app(app):

    @app.cli.command()
    def create_db():
        """Este comando inicializa o banco de dados"""
        click.echo("Banco de dados criado.")
        db.create_all()