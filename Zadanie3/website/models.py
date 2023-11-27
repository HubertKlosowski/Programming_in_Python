from . import db  # from website import db
from sqlalchemy_serializer import SerializerMixin


class Iris(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    sepal_length = db.Column(db.Float, nullable=False)
    sepal_width = db.Column(db.Float, nullable=False)
    petal_length = db.Column(db.Float, nullable=False)
    petal_width = db.Column(db.Float, nullable=False)
    species_id = db.Column(db.Integer, db.ForeignKey('species.id'))


class Species(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    species_name = db.Column(db.String(20), nullable=False)
    irises = db.relationship('Iris')

