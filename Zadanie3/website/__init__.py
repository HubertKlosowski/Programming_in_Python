from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost:3306/flask'

    db.init_app(app)

    from .table import table
    from .api import api

    app.register_blueprint(table, url_prefix='/')
    app.register_blueprint(api, url_prefix='/')

    return app
