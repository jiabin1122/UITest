# -*- coding: utf-8 -*-
# @Author: Jiabin

from utils.browserCli import br
import time

driver = br.driver

class Test_db():
    def test_db(self):
        driver.get("https://xdata.jcloud.com/map/resources/app2/database.html")
        time.sleep(10)
