# from selenium import webdriver
# import pytest
# import requests
#
# @pytest.fixture
# def driver(request, browser_param):
#     if browser_param == "Chrome":
#         dr = webdriver.Chrome()
#         dr.implicitly_wait(30)
#         return dr
#     elif browser_param == 'Firefox':
#         dr = webdriver.Firefox()
#         dr.implicitly_wait(30)
#         return dr
#
#
# def pytest_addoption(parser):
#     parser.addoption(
#         "--url",
#         action="store",
#         default="https://http://localhost:8888/Opencart/opencart-3.0.3.2/upload/",
#         help="This is request url"
#     )
#
#     parser.addoption(
#         "--browser",
#         action="store",
#         default='Chrome',
#         help='Type name of browser on which you want start the tests'
#     )
#
# @pytest.fixture
# def url_param(request):
#     return request.config.getoption("--url")
#
#
# @pytest.fixture
# def browser_param(request):
#     return request.config.getoption("--browser")
#
#
