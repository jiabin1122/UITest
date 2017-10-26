__author__ = 'jiabin'
# coding: utf-8

from utils.browserCli import browser_client

driver = browser_client.driver

class Test_db():
    def test_db(self):
        driver.get("https://xdata.jcloud.com/map/resources/app2/database.html?dataCenter=bj_02")
