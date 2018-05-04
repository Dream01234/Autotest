from selenium import webdriver
from config.config import Path

class Star:

    def start_browser(self,browsername,url):
        if browsername=='Firefox':
            self.driver=webdriver.Firefox()
            self.driver.get(url)
        elif browsername=='Chrome':
            self.driver=webdriver.Chrome()
            self.driver.get(url)
        elif browsername=='IE':
            self.driver=webdriver.Ie()
            self.driver.get(url)


