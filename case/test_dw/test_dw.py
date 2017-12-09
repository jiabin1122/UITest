# coding: utf-8
#__author__ = 'jiabin'
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from utils import const
from utils.action import is_element_exist
from utils.browserCli import br, userName
import time
from utils.randomUtils import generate_random_string

driver = br.driver
sql = "select * from a_atest.jia_6cols"

class Test_dw():
    def test_create_query_task(self):
        """
        新建sql查询脚本
        """
        task_name = "jia_uitest_" + generate_random_string(5)
        br.open(const.instance)
        br.click(By.XPATH, "//div/a[@title='{0}']".format(userName))
        br.click(By.XPATH, "//a[contains(text(),'开发')]")
        br.click(By.XPATH, "//a[contains(text(),'任务开发')]")
        br.mouse_send_keys(sql, By.XPATH, "//div[@class='ace_content']")
        time.sleep(2)
        br.click(By.XPATH, "//a[contains(text(),'运行')]")
        time.sleep(5)
        assert is_element_exist(driver,"//tr/th[contains(text(),'str1')]")
        assert is_element_exist(driver,"//div[contains(text(),'FINISHED')]")
        br.click(By.XPATH, "//a[contains(text(),'保存')]")
        br.send_keys(task_name, By.XPATH, "//input[@class='inputMode']")
        br.click(By.XPATH, "//a[contains(text(),'确定')]")
        br.mouse_click(By.XPATH, "//p[contains(text(),'开发脚本')]")
        br.send_keys(task_name, By.XPATH, "//input[@class='s-searchInput']")
        br.click(By.XPATH, "//i[@class='i31']")
        assert is_element_exist(driver, "//h3[contains(text(),'{0}')]".format(task_name))

    # def test_saveas_task(self):