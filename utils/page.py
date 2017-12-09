import  time

from selenium.webdriver import ActionChains


class Page(object):

    host = "https://xdata.jcloud.com/"

    def __init__(self, driver, base_url = host, path = None):
        self.driver = driver
        self.base_url = base_url
        self.path = path

    def open(self, url, path = None):
        if path != None:
            url = self.base_url + path
        self.driver.get(url)
        time.sleep(2)

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def script(self, src):
        return self.driver.execute_script(src)

    def send_keys(self, value, *loc):
        self.driver.find_element(*loc).clear()
        self.driver.find_element(*loc).send_keys(value)

    def click(self, *loc):
        return self.find_element(*loc).click()

    def mouse_send_keys(self, keys, *loc):
        content = self.driver.find_element(*loc)
        action = ActionChains(self.driver)
        action.move_to_element(content).click()
        action.send_keys(keys).perform()

    def mouse_click(self, *loc):
        content = self.driver.find_element(*loc)
        ActionChains(self.driver).move_to_element(content).perform()
        ActionChains(self.driver).click(content).perform()