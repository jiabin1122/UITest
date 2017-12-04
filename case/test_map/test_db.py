# coding: utf-8
from utils.browserCli import browserClient, br
import time

__author__ = 'jiabin'

driver = br.driver

class Test_db():
    def test_db(self):
        driver.get("https://xdata.jcloud.com/map/resources/app2/database.html")
        time.sleep(10)
