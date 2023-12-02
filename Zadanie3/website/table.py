from flask import Blueprint, render_template, redirect, url_for

from . import db
from .models import Iris

table = Blueprint('table', __name__)


def check_delete(form):
    required_fields = ['record_id']
    for field in required_fields:
        if field not in form or form[field] == '':
            return False
    return True


@table.route('/', methods=['GET'])
def home():
    iris = db.session.query(Iris).all()
    return render_template("table.html", iris=iris)


@table.route('/get/<int:record_id>', methods=['GET'])
def get(record_id):
    iris = Iris.query.get(record_id)
    if iris is None:
        return False
    return iris


@table.route('/delete/<int:record_id>', methods=['POST'])
def delete(record_id):
    try:
        if get(record_id) is False:
            return render_template('404_error.html', error_message='Record not found'), 404
        to_delete = Iris.query.get(record_id)
        db.session.delete(to_delete)
        db.session.commit()
        return redirect(url_for('table.home'))
    except Exception as e:
        print(e)
        db.session.rollback()
        return render_template('404_error.html', error_message=str(e)), 404


"""
{% for el, name in iris %}
                                    <tr>
                                        <td>{{ el.id }}</td>
                                        <td>{{ el.sepal_length }}</td>
                                        <td>{{ el.sepal_width }}</td>
                                        <td>{{ el.petal_length }}</td>
                                        <td>{{ el.petal_width }}</td>
                                        <td>{{ name }}</td>
                                        <td>
                                            <form action="{{ url_for('table.delete', record_id=el.id) }}" method="post">
                                                <button type="submit" class="btn btn-danger">X</button>
                                            </form>
                                        </td>
                                    </tr>
                                {% endfor %}
"""
