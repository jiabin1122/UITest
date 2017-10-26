__author__ = 'jiabin'
# coding: utf-8

import os
import time
from utils.browserCli import browserClient, browser_client
from utils.common import commonHttpClient

browser_client.setup()
driver = browser_client.driver
filename = "6cols_100.txt"

class Test_up_file():
    def up_file(self):
        path  = os.path.join(os.getcwd(),"data",filename)
        if driver.current_url != "https://xdata.jcloud.com/dataIntegration/index.html?dataCenter=bj_02":
            driver.get("https://xdata.jcloud.com/dataIntegration/index.html")
        driver.find_element_by_xpath("//ul[@class='show clearfix']/a/li").click()
        upload = driver.find_element_by_id("mylocalfile")
        upload.send_keys(path)
        driver.find_element_by_xpath("//a[@class='glBtn mr10']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//a[@class='glBtn mr10']").click()

    def test_up_to_tb(self):
        Test_up_file().up_file()
        driver.find_element_by_id("r-cn").click()
        driver.find_element_by_xpath("//select[@class='select-box w335 overHidden']/option[@title='a_atest']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//select[@class='select-box w335 overHidden']/option[@title='jia_6cols']").click()
        driver.implicitly_wait(3)
        driver.find_element_by_xpath("//input[@type='checkbox']").click()
        driver.find_element_by_xpath("//a[@class='blueLink mr10']").click()
        time.sleep(3)
        driver.find_element_by_xpath("//a[@class='glBtn mr10']").click()
        alerttext = driver.find_element_by_xpath(" //div[@class='layui-layer-content']").text
        assert "成功上传了100条记录， 总共100条记录！".decode("utf-8")  ==  alerttext

    def test_up_to_file(self):
        path = "/a_atest/" + filename
        data = {"pathName":path, "recursive":True}
        re, status = commonHttpClient().http_request("POST", "map/file/deleteFileOrFolder.action", data)
        print re
        Test_up_file().up_file()
        driver.find_element_by_link_text("选择文件夹".decode("utf-8")).click()
        time.sleep(3)
        driver.find_element_by_xpath("//li[@_path='/a_atest']/a/span").click()
        driver.find_element_by_xpath("//a[@class='layui-layer-btn0']").click()
        driver.find_element_by_xpath("//input[@class='inputMode w335 gray']").send_keys("file remark")
        driver.find_element_by_xpath("//a[@class='glBtn mr10']").click()
        time.sleep(2)
        alerttext = driver.find_element_by_xpath("//div[@class='layui-layer-content']").text
        assert "上传成功!".decode("utf-8")  ==  alerttext

