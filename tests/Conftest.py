from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import pytest
import requests


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="http://localhost:8888/Opencart/opencart-3.0.3.2/upload/",
        help="This is request url"
    )

    parser.addoption(
        "--browser",
        action="store",
        default='Сhrome',
        help='Type name of browser on which you want start the tests'
    )

@pytest.fixture
def url_param(request):
    return request.config.getoption("--url")


@pytest.fixture
def browser_param(request):
    return request.config.getoption("--browser")


@pytest.fixture
def driver(request, browser_param):
    if browser_param == 'Firefox':
        capabilities = DesiredCapabilities.FIREFOX
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        dr = webdriver.Firefox(options=options)
        dr.maximize_window()

    elif browser_param == 'Safari':
        dr = webdriver.Safari()

    else:
        capabilities = DesiredCapabilities.CHROME
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--kiosk")
        dr = webdriver.Chrome(options=options)

    dr.implicitly_wait(10)
    request.addfinalizer(dr.quit)

    return dr



