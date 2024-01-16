from .exceptions import DataValidationException


def check_add(form):
    required_fields = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species_id']
    for field in required_fields:
        if field not in form or form[field] == '':
            raise DataValidationException('Missing field: [' + field + ']')
        if field != 'species_id' and float(form[field]) <= 0:
            raise DataValidationException('All fields have to be greater than 0: [' + field + ']')
        if field == 'species_id' and int(form[field]) not in [0, 1, 2]:
            raise DataValidationException('Invalid species id: [' + form[field] + ']')


def check_predict(iris):
    for el in iris:
        if not isinstance(el, float) and not isinstance(el, int):
            raise DataValidationException('All fields have to be numbers: [' + type(el) + ']')
        if el <= 0:
            raise DataValidationException('All fields have to be greater than 0: [' + str(el) + ']')


def check_for_knn(num_neighbors):
    if num_neighbors < 5:
        raise DataValidationException('Too little points for num_neighbors KNN')
