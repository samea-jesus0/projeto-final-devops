import unittest
from app import app
import werkzeug

if not hasattr(werkzeug, '__version__'): 
    werkzeug.__version__ = "mock-version"

class APITestCase(unittest.TestCase): 
    @classmethod 
    def setUpClass(cls): 
        cls.client = app.test_client()    
    
    def test_verificar_itens(self):
        response = self.client.get('/items')
        self.assertEqual(response.status_code, 200)
        self.assertIn('items', response.json)
        self.assertIsInstance(response.json['items'], list)

    def test_formato_token_login(self):
        response = self.client.post('/login')
        token = response.json.get("access_token")

        self.assertIsNotNone(token)
        self.assertIsInstance(token, str)
        self.assertGreater(len(token), 10) 
        
    def test_metodo_incorreto(self):
        response = self.client.post('/items')  
        self.assertEqual(response.status_code, 405)        

if __name__ == '__main__':
    unittest.main()