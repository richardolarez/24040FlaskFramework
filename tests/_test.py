import unittest
from app import app, db, User, Projects

class TestFlaskApp(unittest.TestCase):
    # This method will be called before every test method.
    def setUp(self):
        # Create a test client and set up a testing environment
        self.app = app.test_client()
        app.config['TESTING'] = True
        # Create a test database
        db.create_all()

    # This method will be called after every test method.
    def tearDown(self):
        # Clean up the database after each test
        db.session.remove()
        db.drop_all()

    # Helper function to register a test user
    def register_test_user(self, username, password):
        return self.app.post('/register', data=dict(
            username=username,
            password=password
        ), follow_redirects=True)

    # Helper function to log in a test user
    def login_test_user(self, username, password):
        return self.app.post('/login', data=dict(
            username=username,
            password=password
        ), follow_redirects=True)

    # Test user registration
    def test_user_registration(self):
        response = self.register_test_user('testuser', 'testpassword')
        self.assertEqual(response.status_code, 200)
        # Check if user is redirected to the login page after registration
        self.assertTrue(b'Login' in response.data)

    # Test user login
    def test_user_login(self):
        # Register a test user
        self.register_test_user('testuser', 'testpassword')
        response = self.login_test_user('testuser', 'testpassword')
        self.assertEqual(response.status_code, 200)
        # Check if user is redirected to the home page after login
        self.assertTrue(b'Home Page' in response.data)

    # Test project creation
    def test_create_project(self):
        # Log in a test user
        self.register_test_user('testuser', 'testpassword')
        self.login_test_user('testuser', 'testpassword')
        # Create a project
        response = self.app.post('/project', json={'name': 'Test Project'})
        self.assertEqual(response.status_code, 200)
        # Check if the project is created
        self.assertTrue(b'id' in response.data)

    # Test getting all projects
    def test_get_projects(self):
        # Log in a test user
        self.register_test_user('testuser', 'testpassword')
        self.login_test_user('testuser', 'testpassword')
        # Create some projects
        self.app.post('/project', json={'name': 'Project 1'})
        self.app.post('/project', json={'name': 'Project 2'})
        # Get all projects
        response = self.app.get('/projects')
        self.assertEqual(response.status_code, 200)
        # Check if both projects are retrieved
        self.assertTrue(b'Project 1' in response.data)
        self.assertTrue(b'Project 2' in response.data)

if __name__ == '__main__':
    unittest.main()
