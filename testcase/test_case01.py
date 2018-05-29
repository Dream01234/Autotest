# coding:utf-8

import unittest,time

from common.logger import Log
from selenium import webdriver
from common.StartUp import Star
from config.config import Path
from common.Search import Find_Element

log = Log()

class Test(unittest.TestCase):

    def setUp(self):
        Star.start_browser(self,Path.brower,Path.host)
        # self.driver.get(Path.host)
        self.driver.implicitly_wait(30)

    def test_01(self):

        log.info("-------测试用例开始---------")

        Find_Element.id_element(self,"kw")
        # self.driver.find_element_by_id("kw").send_keys("yoyo")
        Find_Element.id_send_key(self,"kw","selenium")
        log.info("输入内容：selenium")

        # self.driver.find_element_by_id("su").click()
        Find_Element.id_click(self,"su")
        log.info("点击按钮：id = su")

        time.sleep(2)

        t = self.driver.title

        log.info(u"获取title内容：%s"%t)

        self.assertIn(u"百度搜索",t)

    def tearDown(self):

        self.driver.quit()

        log.info("-------测试用例结束----------")

if __name__ == "__main__":

    unittest.main()1
