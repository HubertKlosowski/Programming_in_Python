from flask import Blueprint, jsonify, request

from . import db
from .models import Iris
from .trainingModel import train_model
from .validation import check_add, create_iris, get_iris, check_predict

api = Blueprint('api', __name__)


@api.route('/data', methods=['GET', 'POST'])
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


@api.route('/data/<int:record_id>', methods=['DELETE'])
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


@api.route('/predictions', methods=['GET'])
def predict_iris():
    try:
        s_l = float(request.args.get('sepal_length'))
        s_w = float(request.args.get('sepal_width'))
        p_l = float(request.args.get('petal_length'))
        p_w = float(request.args.get('petal_width'))
        iris_data = [s_l, s_w, p_l, p_w]

        check = check_predict(iris_data)
        if not check[1]:
            return jsonify({'error': check[0]}), 400
        test_iris = db.session.query(Iris).all()
        x_data = [[i.sepal_length, i.sepal_width, i.petal_length, i.petal_width] for i in test_iris]
        y = [i.species_id for i in test_iris]
        prediction = int(train_model(x_data, y, [iris_data], None))
        return jsonify({'prediction': prediction}), 200
    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 400
