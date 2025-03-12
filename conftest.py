

import pytest

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests on")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")
