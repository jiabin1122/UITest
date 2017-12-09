# coding: utf-8
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from utils import const
from utils.action import nav_scroll_down, is_element_exist
from utils.browserCli import br
import time

from utils.page import Page

__author__ = 'jiabin'

driver = br.driver

class Test_nav():
    def test_console_page(self):
        """
        访问数知控制台
        """
        br.click(By.XPATH, "//span[contains(text(),'数知控制台')]")
        time.sleep(2)
        assert driver.current_url == const.console_page
        assert is_element_exist(driver,"//li[@class='cur']/a/span[contains(text(),'数知控制台')]")

    def test_dataIntegration(self):
        """
        访问数据集成
        """
        br.click(By.XPATH, "//span[contains(text(),'数据集成')]")
        time.sleep(2)
        assert driver.current_url == const.dataIntegration
        assert is_element_exist(driver,"//li[@class='cur']/a/span[contains(text(),'数据集成')]")

    def test_bi(self):
        """
        访问BI报表
        """
        br.click(By.XPATH, "//span[contains(text(),'BI报表')]")
        time.sleep(2)
        assert driver.current_url == const.bi
        assert is_element_exist(driver,"//li[@class='cur']/a/span[contains(text(),'BI报表')]")

    def test_instance(self):
        """
        访问数据计算服务
        """
        br.click(By.XPATH, "//span[contains(text(),'数据计算服务')]")
        time.sleep(2)
        assert driver.current_url == const.instance
        assert is_element_exist(driver,"//li[@class='cur']/a/span[contains(text(),'数据计算服务')]")

    def test_bigscreen(self):
        """
        访问数据大屏
        """
        br.click(By.XPATH, "//span[contains(text(),'数据大屏')]")
        time.sleep(2)
        assert driver.current_url == const.bigscreen
        assert is_element_exist(driver,"//li[@class='cur']/a/span[contains(text(),'数据大屏')]")

    def test_profile(self):
        """
        访问画像分析
        """
        nav_scroll_down(driver)
        time.sleep(3)
        br.click(By.XPATH, "//span[contains(text(),'画像分析')]")
        time.sleep(3)
        assert driver.current_url == const.profile
        assert is_element_exist(driver,"//li[@class='cur']/a/span[contains(text(),'画像分析')]")

    def test_jmr(self):
        """
        访问JMR
        """
        nav_scroll_down(driver)
        br.click(By.XPATH, "//span[contains(text(),'JMR')]")
        time.sleep(3)
        assert driver.current_url == const.jmr
        assert is_element_exist(driver,"//li[@class='cur']/a/span[contains(text(),'JMR')]")

    def test_jls(self):
        """
        访问日志服务
        """
        nav_scroll_down(driver)
        br.click(By.XPATH, "//span[contains(text(),'日志服务')]")
        time.sleep(3)
        assert driver.current_url == const.jls
        assert is_element_exist(driver,"//li[@class='cur']/a/span[contains(text(),'日志服务')]")

    def test_streamhub(self):
        """
        访问流数据中心
        """
        nav_scroll_down(driver)
        br.click(By.XPATH, "//span[contains(text(),'流数据中心')]")
        time.sleep(3)
        assert driver.current_url == const.streamhub
        assert is_element_exist(driver,"//li[@class='cur']/a/span[contains(text(),'流数据中心')]")

    def test_stream_compute(self):
        """
        访问流计算
        """
        nav_scroll_down(driver)
        br.click(By.XPATH, "//span[contains(text(),'流计算')]")
        time.sleep(3)
        assert driver.current_url == const.stream_compute
        assert is_element_exist(driver,"//li[@class='cur']/a/span[contains(text(),'流计算')]")