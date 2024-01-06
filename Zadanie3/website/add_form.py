from flask import Blueprint, render_template, redirect, url_for, request

from . import db
from .models import Iris

add_form = Blueprint('add_form', __name__)


def check_add(form):
    required_fields = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species_id']
    for field in required_fields:
        if field not in form or form[field] == '':
            return 'Missing required fields', False
        if field != 'species_id' and float(form[field]) <= 0:
            return 'All fields have to be greater than 0', False
        if field == 'species_id' and int(form[field]) not in [0, 1, 2]:
            return 'Species ID must be 0, 1, or 2', False
    return 'Valid data', True


def create_iris(form):
    return Iris(
        sepal_length=float(form['sepal_length']),
        sepal_width=float(form['sepal_width']),
        petal_length=float(form['petal_length']),
        petal_width=float(form['petal_width']),
        species_id=int(form['species_id'])
    )


@add_form.route('/add_form', methods=['GET'])
def home():
    return render_template("add_form.html")


@add_form.route('/add_form/add', methods=['POST'])
def add():
    try:
        check = check_add(request.form)
        if not check[1]:
            return render_template('400_error.html', error_message=check[0]), 400
        new_iris = create_iris(request.form)
        db.session.add(new_iris)
        db.session.commit()
        return redirect(url_for('table.home'))
    except Exception as e:
        print(e)
        db.session.rollback()
        return render_template('400_error.html', error_message=str(e)), 400
