from flask import Blueprint, render_template, redirect, url_for, request

from . import db
from .model import Iris, create_iris
from .validation import check_add, check_predict
from .trainingModel import train_model
from .exceptions import DataValidationException

table = Blueprint('table', __name__)


@table.route('/', methods=['GET'])
def home_page():
    irises = db.session.query(Iris).all()
    return render_template('table.html', irises=irises)


@table.route('/delete/<int:record_id>', methods=['POST'])
def delete(record_id):
    to_delete = Iris.query.get(record_id)
    if to_delete is None:
        return render_template('404_error.html', error_message='Record not found'), 404
    db.session.delete(to_delete)
    db.session.commit()
    return redirect(url_for('table.home_page'))


@table.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        try:
            check_add(request.form)
        except DataValidationException as e:
            return render_template('400_error.html', error_message=e), 400
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
        try:
            check_predict(iris)
        except DataValidationException as e:
            return render_template('predict.html', result=e)

        train_iris = Iris.query.all()
        x_data = [[i.sepal_length, i.sepal_width, i.petal_length, i.petal_width] for i in train_iris]
        y = [i.species_id for i in train_iris]
        prediction = int(train_model(x_data, y, [iris]))
        return render_template('predict.html', result=prediction)
    else:
        return render_template('predict.html')
