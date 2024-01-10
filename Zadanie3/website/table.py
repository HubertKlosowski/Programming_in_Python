from flask import Blueprint, render_template, redirect, url_for, request

from . import db
from .model import Iris, create_iris
from .validation import check_add, get_iris, check_predict
from .trainingModel import train_model

table = Blueprint('table', __name__)


@table.route('/', methods=['GET'])
def home_page():
    irises = db.session.query(Iris).all()
    return render_template('table.html', irises=irises)


@table.route('/delete/<int:record_id>', methods=['POST'])
def delete(record_id):
    to_delete = get_iris(record_id)
    if isinstance(to_delete, str):
        return render_template('404_error.html', error_message=to_delete), 404
    db.session.delete(to_delete)
    db.session.commit()
    return redirect(url_for('table.home_page'))


@table.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        check = check_add(request.form)
        if not check[1]:
            return render_template('400_error.html', error_message=check[0]), 400
        db.session.add(create_iris(request.form))
        db.session.commit()
        return redirect(url_for('table.home_page'))
    else:
        return render_template('add_form.html')


@table.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            iris = [float(el) for el in request.form.values()]
        except ValueError as e:
            return render_template('400_error.html', error_message=str(e)), 400
        check = check_predict(iris)
        if check[1]:
            train_iris = Iris.query.all()
            x_data = [[i.sepal_length, i.sepal_width, i.petal_length, i.petal_width] for i in train_iris]
            y = [i.species_id for i in train_iris]
            return render_template('predict.html', result=train_model(x_data, y, [iris]))
        else:
            return render_template('predict.html', result=check[0])
    else:
        return render_template('predict.html')
