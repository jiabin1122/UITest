# -*- coding: utf-8 -*-
# @Author: Jiabin

def is_element_exist(driver,element):
        flag=True
        try:
            driver.find_element_by_xpath(element)
            return flag
        except:
            flag=False
            return flag

def nav_scroll_down(driver):
    driver.execute_script("document.getElementsByClassName('menuBox')[0].style.marginTop = '-290px'")