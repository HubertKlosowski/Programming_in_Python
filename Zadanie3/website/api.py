from flask import Blueprint, jsonify, request

from . import db
from .models import Iris
from .predict import check_predict
from .trainingModel import train_model

api = Blueprint('api', __name__)


@api.route('/api/data', methods=['GET'])
def get_iris_data():
    iris = db.session.query(Iris).all()
    iris_data = [{'id': el.id, 'sepal_length': el.sepal_length, 'sepal_width': el.sepal_width,
                  'petal_length': el.petal_length, 'petal_width': el.petal_width,
                  'species_id': el.species_id} for el in iris]
    return jsonify(iris_data)


"""
@api.route('/api/data', methods=['POST'])
def add_iris():
    try:
        check = check_add(request.form)
        if not check[1]:
            return jsonify({'error': check[0]}), 400
        iris = create_iris(request.form)
        db.session.add(iris)
        db.session.commit()
        return jsonify({'message': 'Resource created successfully'}), 201
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify({'error': str(e)}), 400
"""


@api.route('/api/data/<int:record_id>', methods=['DELETE'])
def delete_iris(record_id):
    try:
        to_delete = Iris.query.get(record_id)
        if to_delete is None:
            return jsonify({'error': 'Record not found'}), 404
        db.session.delete(to_delete)
        db.session.commit()
        return jsonify({'message': 'Resource deleted successfully'}), 200
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify({'error': str(e)}), 400


@api.route('/api/predictions', methods=['GET'])
def predict_iris():
    try:
        s_l = float(request.args.get('s_l'))
        s_w = float(request.args.get('s_w'))
        p_l = float(request.args.get('p_l'))
        p_w = float(request.args.get('p_w'))
        iris_data = [s_l, s_w, p_l, p_w]
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
