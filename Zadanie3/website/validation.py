from .model import Iris


def check_add(form):
    required_fields = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species_id']
    for field in required_fields:
        if field not in form or form[field] == '':
            return 'Missing required fields', False
        if field != 'species_id' and float(form[field]) <= 0:
            return 'All fields have to be greater than 0', False
        if field == 'species_id' and int(form[field]) not in [0, 1, 2]:
            return 'Species ID must be 0, 1, or 2', False
    return 'Successful validation', True


def get_iris(record_id):
    iris = Iris.query.get(record_id)
    if iris is None:
        return 'Record not found'
    return iris


def check_predict(iris):
    for el in iris:
        if not isinstance(el, float) and not isinstance(el, int):
            return 'All fields have to be numbers', False
        if el <= 0:
            return 'All fields have to be greater than 0', False
    return 'Valid data', True
