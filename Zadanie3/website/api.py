from flask import Blueprint, jsonify, request

from . import db
from .models import Iris
from .trainingModel import train_model
from .validation import check_add, create_iris, get_iris, check_predict

api = Blueprint('api', __name__)


@api.route('/api/data', methods=['GET', 'POST'])
def add_iris():
    if request.method == 'POST':
        try:
            check = check_add(request.form)
            if not check[1]:
                return jsonify({'error': check[0]}), 400
            iris = create_iris(request.form)
            db.session.add(iris)
            db.session.commit()
            return jsonify({'id': iris.id}), 200
        except Exception as e:
            print(e)
            db.session.rollback()
            return jsonify({'error': str(e)}), 400
    else:
        irises = db.session.query(Iris).all()
        iris_data = [{'id': el.id, 'sepal_length': el.sepal_length, 'sepal_width': el.sepal_width,
                      'petal_length': el.petal_length, 'petal_width': el.petal_width,
                      'species_id': el.species_id} for el in irises]
        return jsonify(iris_data)


@api.route('/api/data/<int:record_id>', methods=['DELETE'])
def delete_iris(record_id):
    try:
        to_delete = get_iris(record_id)
        if isinstance(to_delete, str):
            return jsonify({'error': to_delete}), 404
        db.session.delete(to_delete)
        db.session.commit()
        return jsonify({'id': to_delete.id}), 200
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify({'error': str(e)}), 400


@api.route('/api/predictions', methods=['GET'])
def predict_iris():
    try:
        iris_data = [float(el) for el in request.form.values()]
        iris_data[-1] = int(iris_data[-1])
        check = check_predict(iris_data)
        if not check[1]:
            return jsonify({'error': check[0]}), 400
        test_iris = db.session.query(Iris).all()
        X = [[i.sepal_length, i.sepal_width, i.petal_length, i.petal_width] for i in test_iris]
        y = [i.species_id for i in test_iris]
        return jsonify({'prediction': int(train_model(X, y, [iris_data]))}), 200
    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 400
