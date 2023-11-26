from flask import Blueprint, render_template, redirect, url_for, request

from .models import Iris
from . import db

add_form = Blueprint('add_form', __name__)


def check_add(form):
    required_fields = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species_id']
    for field in required_fields:
        if field not in form or form[field] == '':
            return 'Missing required fields', False
        if field != 'species_id' and not form[field].replace('.', '', 1).isdigit():
            return 'All fields have to be numbers', False
        if field == 'species_id' and int(form[field]) not in [1, 2, 3]:
            return 'Species ID must be 1, 2, or 3', False
    return 'Valid data', True


def create_iris(form):
    return Iris(
        sepal_length=float(form['sepal_length']),
        sepal_width=float(form['sepal_width']),
        petal_length=float(form['petal_length']),
        petal_width=float(form['petal_width']),
        species_id=int(form['species_id'])
    )


@add_form.route('/', methods=['GET'])
def home():
    return render_template("add_form.html")


@add_form.route('/add', methods=['POST'])
def add():
    try:
        check = check_add(request.form)
        if not check[1]:
            return render_template('400_error.html', error_message=check[0]), 400
        new_iris = create_iris(request.form)
        db.session.add(new_iris)
        db.session.flush()
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
        return render_template('400_error.html', error_message=str(e)), 400
    return redirect(url_for('add_form.home'))
