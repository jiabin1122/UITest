# coding: utf-8
from selenium.webdriver.support import wait
from utils import const
from utils.action import nav_scroll_down, is_element_exist
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
        assert is_element_exist(driver,"//li[@class='cur']/a/span[contains(text(),'数知控制台')]")

    def test_dataIntegration(self):
        """
        访问数据集成
        """
        driver.find_element_by_xpath("//span[contains(text(),'数据集成')]").click()
        time.sleep(2)
        assert driver.current_url == const.dataIntegration
        assert is_element_exist(driver,"//li[@class='cur']/a/span[contains(text(),'数据集成')]")

    def test_bi(self):
        """
        访问BI报表
        """
        driver.find_element_by_xpath("//span[contains(text(),'BI报表')]").click()
        time.sleep(2)
        assert driver.current_url == const.bi
        assert is_element_exist(driver,"//li[@class='cur']/a/span[contains(text(),'BI报表')]")

    def test_instance(self):
        """
        访问数据计算服务
        """
        driver.find_element_by_xpath("//span[contains(text(),'数据计算服务')]").click()
        time.sleep(2)
        assert driver.current_url == const.instance
        assert is_element_exist(driver,"//li[@class='cur']/a/span[contains(text(),'数据计算服务')]")

    def test_bigscreen(self):
        """
        访问数据大屏
        """
        driver.find_element_by_xpath("//span[contains(text(),'数据大屏')]").click()
        time.sleep(2)
        assert driver.current_url == const.bigscreen
        assert is_element_exist(driver,"//li[@class='cur']/a/span[contains(text(),'数据大屏')]")

    def test_profile(self):
        """
        访问画像分析
        """
        nav_scroll_down(driver)
        time.sleep(3)
        driver.find_element_by_xpath("//span[contains(text(),'画像分析')]").click()
        time.sleep(3)
        assert driver.current_url == const.profile
        assert is_element_exist(driver,"//li[@class='cur']/a/span[contains(text(),'画像分析')]")

    def test_jmr(self):
        """
        访问JMR
        """
        nav_scroll_down(driver)
        driver.find_element_by_xpath("//span[contains(text(),'JMR')]").click()
        time.sleep(3)
        assert driver.current_url == const.jmr
        assert is_element_exist(driver,"//li[@class='cur']/a/span[contains(text(),'JMR')]")

    def test_jls(self):
        """
        访问日志服务
        """
        nav_scroll_down(driver)
        driver.find_element_by_xpath("//span[contains(text(),'日志服务')]").click()
        time.sleep(3)
        assert driver.current_url == const.jls
        assert is_element_exist(driver,"//li[@class='cur']/a/span[contains(text(),'日志服务')]")

    def test_streamhub(self):
        """
        访问流数据中心
        """
        nav_scroll_down(driver)
        driver.find_element_by_xpath("//span[contains(text(),'流数据中心')]").click()
        time.sleep(3)
        assert driver.current_url == const.streamhub
        assert is_element_exist(driver,"//li[@class='cur']/a/span[contains(text(),'流数据中心')]")

    def test_stream_compute(self):
        """
        访问流计算
        """
        nav_scroll_down(driver)
        driver.find_element_by_xpath("//span[contains(text(),'流计算')]").click()
        time.sleep(3)
        assert driver.current_url == const.stream_compute
        assert is_element_exist(driver,"//li[@class='cur']/a/span[contains(text(),'流计算')]")