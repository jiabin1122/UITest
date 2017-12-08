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

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def script(self, src):
        return self.driver.execute_script(src)

    def send_keys(self, value, *loc):
        self.driver.find_element(*loc).clear()
        self.driver.find_element(*loc).send_keys(value)

    def click(self, *loc):
        return self.find_element(*loc).click()