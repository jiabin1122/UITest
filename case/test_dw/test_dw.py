# -*- coding: utf-8 -*-
# @Author: Jiabin

from selenium.webdriver.common.by import By
from utils import const
from utils.action import is_element_exist
from utils.browserCli import br, userName
import time
from utils.randomUtils import generate_random_string

driver = br.driver
sql = "select * from a_atest.jia_6cols;"
task_name = "jia_uitest_" + generate_random_string(5)
task_name_rename = "jia_uitest_" + generate_random_string(5)
task_name_save_as = "jia_uitest_" + generate_random_string(5)

class Test_dw():
    def task_search(self, name):
        br.send_keys(name, By.XPATH, "//input[@class='s-searchInput']")
        br.click(By.XPATH, "//i[@class='i31']")

    def test_create_query_task(self):
        """
        新建sql查询脚本
        """
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
        self.task_search(task_name)
        assert is_element_exist(driver, "//h3[contains(text(),'{0}')]".format(task_name))

    def test_task_rename(self):
        """
        重命名脚本
        """
        br.mouse_move(By.XPATH, "//h3[contains(text(),'{0}')]".format(task_name))
        br.mouse_move(By.XPATH, "//dt/span[contains(text(),'...')]")
        br.mouse_click(By.XPATH, "//a[contains(text(),'重命名')]")
        br.send_keys(task_name_rename, By.XPATH, "//input[@class='inputMode']")
        br.click(By.XPATH, "//a[contains(text(),'确定')]")
        self.task_search(task_name_rename)
        assert is_element_exist(driver, "//h3[contains(text(),'{0}')]".format(task_name_rename))
        self.task_search(task_name)
        assert False == is_element_exist(driver, "//h3[contains(text(),'{0}')]".format(task_name))

    def test_task_save_as(self):
        """
        脚本另存为
        """
        br.mouse_send_keys("show databases;", By.XPATH, "//div[@class='ace_content']")
        br.click(By.XPATH, "//a[contains(text(),'另存为')]")
        br.send_keys(task_name_save_as, By.XPATH, "//input[@class='inputMode']")
        br.click(By.XPATH, "//a[contains(text(),'确定')]")
        time.sleep(2)
        br.click(By.XPATH, "//a[contains(text(),'运行')]")
        time.sleep(5)
        assert is_element_exist(driver,"//tr/th[contains(text(),'databaseName')]")

    def test_delete_task(self):
        """
        删除脚本
        """
        self.task_search(task_name_rename)
        br.mouse_move(By.XPATH, "//h3[contains(text(),'{0}')]".format(task_name_rename))
        br.mouse_move(By.XPATH, "//dt/span[contains(text(),'...')]")
        br.mouse_click(By.XPATH, "//a[contains(text(),'删除')]")
        br.click(By.XPATH, "//a[contains(text(),'确定')]")
        self.task_search(task_name_rename)
        assert False == is_element_exist(driver, "//h3[contains(text(),'{0}')]".format(task_name_rename))
        self.task_search(task_name_save_as)
        br.mouse_move(By.XPATH, "//h3[contains(text(),'{0}')]".format(task_name_save_as))
        br.mouse_move(By.XPATH, "//dt/span[contains(text(),'...')]")
        br.mouse_click(By.XPATH, "//a[contains(text(),'删除')]")
        br.click(By.XPATH, "//a[contains(text(),'确定')]")