import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_test_route(self):
        response = self.app.get('/test')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], 'Test route works!')

    def test_get_projects(self):
        response = self.app.get('/projects')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)
        # Add more assertions for the response data if needed

    def test_get_batteries(self):
        response = self.app.get('/batteries/1')  # Assuming project ID 1 exists
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)
        # Add more assertions for the response data if needed

    def test_get_power_supplies(self):
        response = self.app.get('/power_supplies/1')  # Assuming project ID 1 exists
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)
        # Add more assertions for the response data if needed

    def test_get_controllers(self):
        response = self.app.get('/controllers/1')  # Assuming project ID 1 exists
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)
        # Add more assertions for the response data if needed

if __name__ == '__main__':
    unittest.main()
