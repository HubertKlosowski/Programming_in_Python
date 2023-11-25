from flask import Blueprint, render_template, redirect, url_for, request

from .models import Iris, Species
from . import db

table = Blueprint('table', __name__)


def check_add(form):
    required_fields = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species_id']
    for field in required_fields:
        if field not in form or form[field] == '':
            return False
    return True


def check_delete(form):
    required_fields = ['record_id']
    for field in required_fields:
        if field not in form or form[field] == '':
            return False
    return True


@table.route('/', methods=['GET'])
def home():
    iris = db.session.query(Iris, Species.species_name).join(Species, Iris.species_id == Species.id).all()
    return render_template("table.html", iris=iris)


@table.route('/get/<int:record_id>', methods=['GET'])
def get(record_id):
    iris = db.session.query(Iris, Species.species_name).join(Species, Iris.species_id == Species.id).filter(
        Iris.id == record_id).first()
    if iris is None:
        return False
    return True


@table.route('/add', methods=['POST'])
def add():
    try:
        if not check_add(request.form):
            return render_template('400_error.html', error_message='Missing required fields'), 400
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
        return render_template('400_error.html', error_message=str(e)), 400
    return redirect(url_for('table.home'))


@table.route('/delete/<int:record_id>', methods=['POST'])
def delete(record_id):
    try:
        if get(record_id) is False:
            return render_template('404_error.html', error_message='Record not found'), 404
        to_delete = Iris.query.get(record_id)
        db.session.delete(to_delete)
        db.session.flush()
        db.session.commit()
        return redirect(url_for('table.home'))
    except Exception as e:
        print(e)
        db.session.rollback()
        return render_template('404_error.html', error_message=str(e)), 404
