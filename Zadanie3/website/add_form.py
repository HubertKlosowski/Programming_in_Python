from flask import Blueprint, render_template, redirect, url_for, request

from .models import Iris
from . import db

add_form = Blueprint('add_form', __name__)


def check_add(form):
    required_fields = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species_id']
    for field in required_fields:
        if field not in form or form[field] == '':
            return False
    return True


@add_form.route('/', methods=['GET'])
def home():
    return render_template("add_form.html")


@add_form.route('/add', methods=['POST'])
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
    return redirect(url_for('add_form.home'))
