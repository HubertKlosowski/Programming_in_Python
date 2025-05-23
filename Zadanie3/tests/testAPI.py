import unittest

from website import create_app

app = create_app()


class MyTestCase(unittest.TestCase):
    def test_get_iris_data(self):
        with app.test_client() as c:
            response = c.get('/api/data')
            self.assertEqual(response.status_code, 200)
            self.assertTrue(response.data is not None)

    def test_add_iris(self):
        with app.test_client() as c:
            response = c.post('/api/data', data={'sepal_length': 1, 'sepal_width': 1, 'petal_length': 1,
                                                 'petal_width': 1, 'species_id': 1})
            self.assertEqual(response.status_code, 200)

    def test_delete_iris(self):
        with app.test_client() as c:
            irises = c.get('/api/data').json
            length = len(irises)
            response = c.delete('/api/data/1')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json, {'id': 1})
            irises = c.get('/api/data').json
            self.assertTrue(len(irises) == length - 1)

    def test_add_iris_with_invalid_species_id(self):
        with app.test_client() as c:
            response = c.post('/api/data', data={'sepal_length': 1, 'sepal_width': 1, 'petal_length': 1,
                                                 'petal_width': 1, 'species_id': 4})
            self.assertEqual(response.status_code, 400)

    def test_add_iris_with_missing_fields(self):
        with app.test_client() as c:
            response = c.post('/api/data', data={'sepal_length': 1, 'sepal_width': 1, 'petal_length': 1,
                                                 'petal_width': 1})
            self.assertEqual(response.status_code, 400)

    def test_add_iris_with_invalid_fields(self):
        with app.test_client() as c:
            response = c.post('/api/data', data={'sepal_length': -1, 'sepal_width': -1, 'petal_length': -1,
                                                 'petal_width': 0, 'species_id': 0})
            self.assertEqual(response.status_code, 400)

    def test_predict_iris(self):
        with app.test_client() as c:
            response = c.get('/api/predictions?sepal_length=1&sepal_width=1&petal_length=1&petal_width=1')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json, {'prediction': 1})

    def test_predict_iris_with_invalid_fields(self):
        with app.test_client() as c:
            response = c.get('/api/predictions?sepal_length=-1&sepal_width=1&petal_length=1&petal_width=1')
            self.assertEqual(response.status_code, 400)
            self.assertEqual(response.json, {'error': 'All fields have to be greater than 0: [-1.0]'})


if __name__ == '__main__':
    unittest.main()
