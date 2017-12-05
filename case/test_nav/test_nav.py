# coding: utf-8
from selenium.webdriver.support import wait
from utils import const
from utils.action import isElementExist
from utils.browserCli import br
import time

__author__ = 'jiabin'

driver = br.driver


class ExpectedConditions(object):
    pass


class Test_nav():
    def test_console_page(self):
        """
        访问数知控制台
        """
        driver.get(const.console_page)
        driver.find_element_by_xpath("//span[contains(text(),'数知控制台')]").click()
        time.sleep(2)
        assert driver.current_url == const.console_page
        assert isElementExist(driver,"//li[@class='cur']/a/span[contains(text(),'数知控制台')]")

    def test_dataIntegration(self):
        """
        访问数据集成
        """
        driver.get(const.dataIntegration)
        driver.find_element_by_xpath("//span[contains(text(),'数据集成')]").click()
        time.sleep(2)
        assert driver.current_url == const.dataIntegration
        assert isElementExist(driver,"//li[@class='cur']/a/span[contains(text(),'数据集成')]")

    def test_bi(self):
        """
        访问BI报表
        """
        driver.get(const.bi)
        driver.find_element_by_xpath("//span[contains(text(),'BI报表')]").click()
        time.sleep(2)
        assert driver.current_url == const.bi
        assert isElementExist(driver,"//li[@class='cur']/a/span[contains(text(),'BI报表')]")

    def test_instance(self):
        """
        访问数据计算服务
        """
        driver.get(const.instance)
        driver.find_element_by_xpath("//span[contains(text(),'数据计算服务')]").click()
        time.sleep(2)
        assert driver.current_url == const.instance
        assert isElementExist(driver,"//li[@class='cur']/a/span[contains(text(),'数据计算服务')]")

    def test_bigscreen(self):
        """
        访问数据大屏
        """
        driver.get(const.bigscreen)
        driver.find_element_by_xpath("//span[contains(text(),'数据大屏')]").click()
        time.sleep(2)
        assert driver.current_url == const.bigscreen
        assert isElementExist(driver,"//li[@class='cur']/a/span[contains(text(),'数据大屏')]")

    def test_profile(self):
        """
        访问画像分析
        """
        driver.execute_script("document.getElementByXpath(\"//div[@class='menuBox']\").style.margin-top = '-290';")
        time.sleep(3)
        driver.get(const.profile)
        driver.find_element_by_xpath("//span[contains(text(),'画像分析')]").click()
        time.sleep(3)
        print driver.current_url
        assert driver.current_url == const.profile
        assert isElementExist(driver,"//li[@class='cur']/a/span[contains(text(),'画像分析')]")

    def test_jmr(self):
        """
        访问JMR
        """
        driver.get(const.jmr)
        driver.find_element_by_xpath("//span[contains(text(),'JMR')]").click()
        time.sleep(3)
        print driver.current_url
        assert driver.current_url == const.jmr
        assert isElementExist(driver,"//li[@class='cur']/a/span[contains(text(),'JMR')]")

    def test_jls(self):
        """
        访问日志服务
        """
        driver.get(const.jls)
        driver.find_element_by_xpath("//span[contains(text(),'日志服务')]").click()
        time.sleep(3)
        print driver.current_url
        assert driver.current_url == const.jls
        assert isElementExist(driver,"//li[@class='cur']/a/span[contains(text(),'日志服务')]")

    def test_streamhub(self):
        """
        访问流数据中心
        """
        driver.get(const.streamhub)
        driver.find_element_by_xpath("//span[contains(text(),'流数据中心')]").click()
        time.sleep(3)
        print driver.current_url
        assert driver.current_url == const.streamhub
        assert isElementExist(driver,"//li[@class='cur']/a/span[contains(text(),'流数据中心')]")

    def test_stream_compute(self):
        """
        访问流计算
        """
        driver.get(const.stream_compute)
        driver.find_element_by_xpath("//span[contains(text(),'流计算')]").click()
        time.sleep(3)
        print driver.current_url
        assert driver.current_url == const.stream_compute
        assert isElementExist(driver,"//li[@class='cur']/a/span[contains(text(),'流计算')]")