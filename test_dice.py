import unittest
import requests
import app
import json
from unittest import TestCase

class TestDatetimeAPI(TestCase):
	def test_test(self):
		assert app.test() == "Works!!!"
	
	def test_dicePage(self):
		ResultDict = app.GetURL('48d75c359ce4')
		ResultDictJ = json.loads(ResultDict)
		assert (ResultDictJ["question"]) =="Which is the best interactive presentation platform?"

if __name__ == '__main__':
    unittest.main()