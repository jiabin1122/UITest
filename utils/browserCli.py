# -*- coding: utf-8 -*-
# @Author: Jiabin

import yaml
from selenium.webdriver.common.by import By
from utils.page import Page
from selenium import webdriver
from utils.set_cookies import save_cookies
import time


with open("./data/account.yaml", "r") as f :
    inf = yaml.load(f)
    for key, value in inf.items():
        if key == "account" :
            user = value
    for key, value in user.items():
        userName, pwd = key, value

class browserClient(Page):

    def setup(self, driver):
        login_url = "https://uc.jcloud.com/login?returnUrl=https://xdata.jcloud.com/console_page"
        driver.maximize_window()
        self.open(login_url)
        driver.implicitly_wait(5)
        driver.switch_to.frame("login_frame")
        driver.implicitly_wait(3)
        self.send_keys(userName, By.ID,"loginname")
        self.send_keys(pwd, By.ID,"nloginpwd")
        time.sleep(8)
        self.click(By.ID,"paipaiLoginSubmit")
        driver.implicitly_wait(2)
        self.click(By.XPATH, "//span[contains(text(),'数知控制台')]")
        cookies = driver.get_cookies()
        save_cookies(cookies)

    def close(self,driver):
        driver.quit()

chromedriver = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(chromedriver)

br = browserClient(driver)
