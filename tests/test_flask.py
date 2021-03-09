import unittest
import requests
import json
import sys, os
from unittest import TestCase
sys.path.append(os.path.abspath(os.path.join('..', 'travis-Integration')))
import app


class TestDatetimeAPI(TestCase):
	def test_test(self):
		assert app.test() == "Works!!!"
	
	def test_GetURL(self):
		ResultDict = app.GetURL('48d75c359ce4')
		ResultDictJ = json.loads(ResultDict)
		assert (ResultDictJ["question"]) =="Which is the best interactive presentation platform?"
	
	def test_URLConnectivity(self):
		QuestionURI='https://travis-menti.herokuapp.com/voting?questionid=48d75c359ce4'
		QURIResponse = requests.get(QuestionURI)
		assert (str(QURIResponse.status_code)) =="200"

if __name__ == '__main__':
    unittest.main()