from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://iris_user:iris_user@localhost:3306/flask'

    db.init_app(app)

    from .table import table
    from .add_form import add_form

    app.register_blueprint(table, url_prefix='/')
    app.register_blueprint(add_form, url_prefix='/add_form')

    return app
