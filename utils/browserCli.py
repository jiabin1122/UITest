__author__ = 'jiabin5'
# coding: utf-8


from selenium import webdriver
from utils.set_cookies import save_cookies
import time

with open("./data/account.txt", "r") as f :
    for item in f.readlines():
        line = item.split(":")
        if line[0] == "user1":
            user, pwd = line[1].split(",")[0], line[1].split(",")[1].strip()

class browserClient(object):
    def __init__(self):
        chromedriver = "C:\Program Files (x86)\chromedriver.exe"
        self.driver = webdriver.Chrome(chromedriver)

    def setup(self, driver):
        url = "https://uc.jcloud.com/login?returnUrl=https://xdata.jcloud.com/console_page"
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(10)
        driver.switch_to.frame("login_frame")
        driver.implicitly_wait(3)
        driver.find_element_by_id("loginname").clear()
        driver.find_element_by_id("loginname").send_keys(user)
        driver.find_element_by_id("nloginpwd").clear()
        driver.find_element_by_id("nloginpwd").send_keys(pwd)
        time.sleep(10)
        driver.find_element_by_id("paipaiLoginSubmit").click()
        driver.implicitly_wait(10)
        driver.find_element_by_xpath("//li[1]/a/dl/dd").click()
        cookies = driver.get_cookies()
        save_cookies(cookies)

    def close(self,driver):
        driver.close()

br = browserClient()
