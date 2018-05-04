from selenium import webdriver

# 基础类
class BasePage(object):
    def _int_(self,driver):
        self.driver=driver

class Find_Element(BasePage):
    #根据ID查找
    def id_element(self,ID):
        self.driver.find_element_by_id(ID)
    #根据ID查找并键入
    def id_send_key(self,ID,something):
        self.driver.find_element_by_id(ID).send_keys(something)
    #根据ID点击
    def id_click(self,ID):
        self.driver.find_element_by_id(ID).click()