from flask_sqlalchemy import SQLAlchemy
import psycopg2

db = SQLAlchemy()

def init_app(app):
    db.init_app(app)