import unittest
from app import app


class TestApp(unittest.TestCase):

    def test_hello(self):
        client = app.test_client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"<html>", response.data)
        self.assertIn(b"Azure DevOps Pipeline", response.data)


if __name__ == '__main__':
    unittest.main()
