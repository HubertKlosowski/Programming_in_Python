from flask import Blueprint, render_template, redirect, url_for

from .models import Iris, Species
from . import db

table = Blueprint('table', __name__)


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
