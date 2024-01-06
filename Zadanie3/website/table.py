from flask import Blueprint, render_template, redirect, url_for

from . import db
from .models import Iris

table = Blueprint('table', __name__)


@table.route('/', methods=['GET'])
def home_page():
    irises = db.session.query(Iris).all()
    return render_template("table.html", irises=irises)


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


def get_iris(record_id):
    iris = Iris.query.get(record_id)
    if iris is None:
        return False
    return iris
