from flask import Blueprint, jsonify, request
from .add_form import check_add
from .models import Iris, Species
from . import db

api = Blueprint('api', __name__)


@api.route('/api/data', methods=['GET'])
def get_iris_data():
    iris = db.session.query(Iris, Species.species_name).join(Species, Iris.species_id == Species.id).all()
    iris_data = [{'id': el.id, 'sepal_length': el.sepal_length, 'sepal_width': el.sepal_width,
                  'petal_length': el.petal_length, 'petal_width': el.petal_width,
                  'species_id': el.species_id, 'species_name': name} for el, name in iris]
    return jsonify(iris_data)


@api.route('/api/data', methods=['POST'])
def add_iris():
    try:
        if not check_add(request.form):
            return jsonify({'error': 'Missing required fields'}), 400
        new_iris = Iris(
            sepal_length=float(request.form['sepal_length']),
            sepal_width=float(request.form['sepal_width']),
            petal_length=float(request.form['petal_length']),
            petal_width=float(request.form['petal_width']),
            species_id=int(request.form['species_id'])
        )
        db.session.add(new_iris)
        db.session.flush()
        db.session.commit()
        return jsonify({'message': 'Resource created successfully', 'id': new_iris.id}), 201
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify({'error': str(e)}), 400


@api.route('/api/data/<int:record_id>', methods=['DELETE'])
def delete_iris(record_id):
    try:
        to_delete = Iris.query.get(record_id)
        if to_delete is None:
            return jsonify({'error': 'Record not found'}), 404
        db.session.delete(to_delete)
        db.session.flush()
        db.session.commit()
        return jsonify({'message': 'Resource deleted successfully'}), 204
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify({'error': str(e)}), 400
