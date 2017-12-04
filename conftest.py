# coding: utf-8
__author__ = 'jiabin5'


import pytest
from utils.browserCli import browserClient, br


@pytest.fixture(scope="session", autouse=True)
def browser_client(request):
    driver = br.driver
    br.setup(driver)
    print "================ started ================"
    def tear_down():
        br.close(driver)
        print "================ finished ================"
    request.addfinalizer(tear_down)








