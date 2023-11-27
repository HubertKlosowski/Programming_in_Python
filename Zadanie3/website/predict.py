from flask import Blueprint, render_template, request
from .trainingModel import train_model, scale_data

from .models import Iris

predict = Blueprint('predict', __name__)


def check_predict(iris):
    for el in iris:
        if not isinstance(el, float):
            return 'All fields have to be numbers', False
        if el <= 0:
            return 'All fields have to be greater than 0', False
    return 'Valid data', True


@predict.route('/predict', methods=['GET'])
def home():
    return render_template("predict.html")


@predict.route('/predict', methods=['POST'])
def predict_iris():
    try:
        iris = [float(request.form['sepal_length']), float(request.form['sepal_width']),
                float(request.form['petal_length']), float(request.form['petal_width'])]
    except ValueError as e:
        print(e)
        return render_template('400_error.html', error_message=str(e)), 400
    check = check_predict(iris)
    if check[1]:
        test_iris = Iris.query.all()
        X = [[i.sepal_length, i.sepal_width, i.petal_length, i.petal_width] for i in test_iris]
        y = [i.species_id for i in test_iris]
        return render_template("predict.html", result=train_model(X, y, [iris]))
    else:
        return render_template("predict.html", result=check[0])
