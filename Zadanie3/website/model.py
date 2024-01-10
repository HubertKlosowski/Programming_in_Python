from . import db  # from website import db


class Iris(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sepal_length = db.Column(db.Float, nullable=False)
    sepal_width = db.Column(db.Float, nullable=False)
    petal_length = db.Column(db.Float, nullable=False)
    petal_width = db.Column(db.Float, nullable=False)
    species_id = db.Column(db.Integer, nullable=False)


def create_iris(form):
    return Iris(
        sepal_length=float(form['sepal_length']),
        sepal_width=float(form['sepal_width']),
        petal_length=float(form['petal_length']),
        petal_width=float(form['petal_width']),
        species_id=int(form['species_id'])
    )
