from flask import Blueprint, render_template, redirect, url_for, request

from . import db
from .models import Iris

table = Blueprint('table', __name__)


@table.route('/', methods=['GET'])
def home_page():
    irises = db.session.query(Iris).all()
    return render_template('table.html', irises=irises)


@table.route('/delete/<int:record_id>', methods=['POST'])
def delete(record_id):
    try:
        if not get_iris(record_id):
            return render_template('404_error.html', error_message='Nie można usunąć irysa, '
                                                                   'którego nie ma'), 404
        to_delete = Iris.query.get(record_id)
        db.session.delete(to_delete)
        db.session.commit()
        return redirect(url_for('table.home_page'))
    except Exception as e:
        print(e)
        db.session.rollback()
        return render_template('404_error.html', error_message=str(e)), 404


@table.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        try:
            check = check_add(request.form)
            if not check[1]:
                return render_template('400_error.html', error_message=check[0]), 400
            db.session.add(create_iris(request.form))
            db.session.commit()
            return redirect(url_for('table.home_page'))
        except Exception as e:
            print(e)
            db.session.rollback()
            return render_template('400_error.html', error_message=str(e)), 400
    else:
        return render_template('add_form.html')


def create_iris(form):
    return Iris(
        sepal_length=float(form['sepal_length']),
        sepal_width=float(form['sepal_width']),
        petal_length=float(form['petal_length']),
        petal_width=float(form['petal_width']),
        species_id=int(form['species_id'])
    )


def check_add(form):
    required_fields = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species_id']
    for field in required_fields:
        if field not in form or form[field] == '':
            return 'Brak wymaganych pól', False
        if field != 'species_id' and float(form[field]) <= 0:
            return 'Wszystkie pola nie mogą być ujemne', False
        if field == 'species_id' and int(form[field]) not in [0, 1, 2]:
            return 'Id gatunku musi być 0, 1 lub 2', False
    return 'Poprawne dane', True


def get_iris(record_id):
    iris = Iris.query.get(record_id)
    if iris is None:
        return False
    return iris
