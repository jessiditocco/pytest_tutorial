import pytest

@pytest.mark.slow
def test_very_long_running_test():
	pass

# py.test -m slow