import unittest
import requests
import app
from unittest import TestCase

class TestDatetimeAPI(TestCase):
	#def test_test(self):
	#	assert app.test() == "Works!"
	
	def test_dicePage(self):
		data = requests.get("http://0.0.0.0:5000/voting")
		self.assertEqual(data.status_code, 200)

if __name__ == '__main__':
    unittest.main()