from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://marcojakob.github.io/dart-dnd/basic/",
        help="This is request url"
    )

    parser.addoption(
        "--browser",
        action="store",
        default='Сhrome',
        help='Type name of browser on which you want start the tests'
    )


@pytest.fixture(scope="session", autouse=True)
def driver(request):
    browser_param = request.config.getoption("--browser")
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
        dr = webdriver.Chrome(options=options)

    dr.implicitly_wait(10)
    request.addfinalizer(dr.quit)
    dr.get(request.config.getoption("--url"))

    return dr
