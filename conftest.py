__author__ = 'jiabin5'
# coding: utf-8

import json
import pytest
from utils.browserCli import browserClient
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--config_file", action="store", default="conf.json",
                     help="test config file path")

@pytest.fixture(scope="session")
def config(request):
    file_path = request.config.getoption("config_file")
    conf_obj = json.load(open(file_path, 'r'))
    return conf_obj


# @pytest.fixture(scope="class")
# def browser_client():
#     chromedriver = "C:\Program Files (x86)\chromedriver.exe"
#     driver = webdriver.Chrome(chromedriver)
#     browser = browserClient(driver)
#     return browser







