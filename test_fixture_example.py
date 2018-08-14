import pytest
from selenium.webdriver import Chrome

@pytest.fixture
def webdriver(request):
	driver = Chrome()
	request.addfinalizer(driver.quit)
	return driver


def test_nix_website_title(webdriver):
	webdriver.get("https://nixos.org/nix/")
	assert "Nix" in webdriver.title

def test_pytest_website_title(webdriver):
	webdriver.get("http://pytest.org/latest/")
	assert "pytest" in webdriver.title