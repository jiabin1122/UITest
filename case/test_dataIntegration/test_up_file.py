# -*- coding: utf-8 -*-
# @Author: Jiabin

from selenium.webdriver.common.by import By
from utils.browserCli import br, userName
import os
import time
from utils.common import commonHttpClient

filename = "6cols_100.txt"
driver = br.driver

class Test_up_file():
    def up_file(self):
        path  = os.path.join(os.getcwd(),"data",filename)
        br.open("https://xdata.jcloud.com/dataIntegration/index.html")
        br.click(By.XPATH, "//ul[@class='show clearfix']/a/li")
        upload = driver.find_element_by_id("mylocalfile")
        upload.send_keys(path)
        br.click(By.XPATH, "//a[@class='glBtn mr10']")
        time.sleep(1)
        br.click(By.XPATH, "//a[@class='glBtn mr10']")

    def test_up_to_tb(self):
        """
        本地文件上传至数仓
        """
        Test_up_file().up_file()
        br.click(By.ID, "r-cn")
        br.click(By.XPATH, "//select[@class='select-box w335 overHidden']/option[@title='a_atest']")
        time.sleep(1)
        br.click(By.XPATH, "//select[@class='select-box w335 overHidden']/option[@title='jia_6cols']")
        time.sleep(5)
        br.click(By.XPATH, "//input[@type='checkbox']")
        br.click(By.XPATH, "//a[@class='blueLink mr10']")
        time.sleep(500)
        br.click(By.XPATH, "//a[@class='glBtn mr10']")
        alerttext = br.find_element(By.XPATH, "//div[@class='layui-layer-content']").text
        assert "成功上传了100条记录， 总共100条记录！".decode("utf-8")  ==  alerttext

    def test_up_to_file(self):
        """
        本地文件上传至hdfs
        """
        path = "/a_atest/" + filename
        data = {"pathName":path, "recursive":"true", "instanceName":userName}
        re, status = commonHttpClient().http_request("POST", "dw/file/deleteFileOrFolder.action", data)
        print re
        Test_up_file().up_file()
        br.click(By.PARTIAL_LINK_TEXT, "选择文件夹".decode("utf-8"))
        time.sleep(3)
        br.click(By.XPATH, "//li[@_path='/a_atest']/a/span")
        br.click(By.XPATH, "//a[@class='layui-layer-btn0']")
        br.send_keys("file remark", By.XPATH, "//input[@class='inputMode w335 gray']")
        br.click(By.XPATH, "//a[@class='glBtn mr10']")
        time.sleep(2)
        alerttext = br.find_element(By.XPATH, "//div[@class='layui-layer-content']").text
        assert "上传成功!".decode("utf-8")  ==  alerttext

