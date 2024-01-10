from flask import Blueprint, request

from . import db
from .model import Iris, create_iris
from .trainingModel import train_model
from .validation import check_add, get_iris, check_predict

api = Blueprint('api', __name__)


@api.route('/data', methods=['GET', 'POST'])
def add_iris():
    if request.method == 'POST':
        check = check_add(request.form)
        if not check[1]:
            return {'error': check[0]}, 400
        iris = create_iris(request.form)
        db.session.add(iris)
        db.session.commit()
        return {'id': iris.id}
    else:
        irises = db.session.query(Iris).all()
        iris_data = [{'id': el.id, 'sepal_length': el.sepal_length, 'sepal_width': el.sepal_width,
                      'petal_length': el.petal_length, 'petal_width': el.petal_width,
                      'species_id': el.species_id} for el in irises]
        return iris_data


@api.route('/data/<int:record_id>', methods=['DELETE'])
def delete_iris(record_id):
    to_delete = get_iris(record_id)
    if isinstance(to_delete, str):
        return {'error': to_delete}, 404
    db.session.delete(to_delete)
    db.session.commit()
    return {'id': to_delete.id}


@api.route('/predictions', methods=['GET'])
def predict_iris():
    s_l = float(request.args.get('sepal_length'))
    s_w = float(request.args.get('sepal_width'))
    p_l = float(request.args.get('petal_length'))
    p_w = float(request.args.get('petal_width'))

    iris_data = [s_l, s_w, p_l, p_w]
    check = check_predict(iris_data)

    if not check[1]:
        return {'error': check[0]}, 400
    train_iris = db.session.query(Iris).all()
    x_data = [[i.sepal_length, i.sepal_width, i.petal_length, i.petal_width] for i in train_iris]
    y = [i.species_id for i in train_iris]
    prediction = int(train_model(x_data, y, [iris_data]))
    return {'prediction': prediction}
