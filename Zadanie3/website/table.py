from flask import Blueprint, render_template, redirect, url_for, request

from .models import Iris, Species
from . import db

table = Blueprint('table', __name__)


@table.route('/', methods=['GET'])
def home():
    iris = db.session.query(Iris, Species.species_name).join(Species, Iris.species_id == Species.id).all()
    return render_template("table.html", iris=iris)


@table.route('/add', methods=['POST'])
def add():
    try:
        new_iris = Iris(
            sepal_length=float(request.form['sepal_length']),
            sepal_width=float(request.form['sepal_width']),
            petal_length=float(request.form['petal_length']),
            petal_width=float(request.form['petal_width']),
            species_id=int(request.form['species_id'])
        )
        db.session.add(new_iris)
        db.session.flush()
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
    return redirect(url_for('table.home'))


@table.route('/delete/<int:record_id>', methods=['POST'])
def delete(record_id):
    try:
        to_delete = Iris.query.get(record_id)
        db.session.delete(to_delete)
        db.session.flush()
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
    return redirect(url_for('table.home'))
