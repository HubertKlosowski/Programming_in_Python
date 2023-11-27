import unittest

from website import create_app

app = create_app()


class MyTestCase(unittest.TestCase):

    def test_get_iris_data(self):
        with app.test_client() as c:
            response = c.get('/api/data')
            self.assertEqual(response.status_code, 200)
            self.assertTrue(len(response.json) == 150)

    def test_add_iris(self):
        with app.test_client() as c:
            response = c.post('/api/data', data={'sepal_length': 1, 'sepal_width': 1, 'petal_length': 1,
                                                 'petal_width': 1, 'species_id': 1})
            self.assertEqual(response.status_code, 201)
            self.assertEqual(response.json, {'message': 'Resource created successfully'})

    def test_delete_iris(self):
        with app.test_client() as c:
            response = c.delete('/api/data/1')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json, {'message': 'Resource deleted successfully'})
            irises = c.get('/api/data')
            self.assertTrue(len(irises.json) == 150)

    def test_add_iris_with_invalid_species_id(self):
        with app.test_client() as c:
            response = c.post('/api/data', data={'sepal_length': 1, 'sepal_width': 1, 'petal_length': 1,
                                                 'petal_width': 1, 'species_id': 4})
            self.assertEqual(response.status_code, 400)
            self.assertEqual(response.json, {'error': 'Species ID must be 1, 2, or 3'})

    def test_add_iris_with_missing_fields(self):
        with app.test_client() as c:
            response = c.post('/api/data', data={'sepal_length': 1, 'sepal_width': 1, 'petal_length': 1,
                                                 'petal_width': 1})
            self.assertEqual(response.status_code, 400)
            self.assertEqual(response.json, {'error': 'Missing required fields'})

    def test_add_iris_with_invalid_fields(self):
        with app.test_client() as c:
            response = c.post('/api/data', data={'sepal_length': -1, 'sepal_width': -1, 'petal_length': -1,
                                                 'petal_width': 0, 'species_id': 0})
            self.assertEqual(response.status_code, 400)
            self.assertEqual(response.json, {'error': 'All fields have to be greater than 0'})

    def test_predict_iris(self):
        with app.test_client() as c:
            response = c.get('/api/predictions', query_string={'s_l': 1, 's_w': 1, 'p_l': 1, 'p_w': 1})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json, {'prediction': 1})


if __name__ == '__main__':
    unittest.main()
