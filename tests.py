#python -m pytest tests.py -v
import pytest
from main import *

def test_durov_id():
	re = getUsers(['1'])

	assert re[0]['response'][0]['id'] == 1
	

def test_bad_address():
	try:
		getUsers(['ы'])
	except UnicodeEncodeError:
		assert True
	else:
		assert False