import pytest

class TestClass(object):
	def test_one(self):
		x = "this"
		assert 'h' in x

	def test_two(self):
		x = "hello"
		assert "el" in x