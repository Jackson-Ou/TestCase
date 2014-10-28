# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import HTMLTestRunner

class my_test2(unittest.TestCase):
    u"""我的测试2"""
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)
        self.base_url = "http://www.baidu.com"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_3(self):
        u"""测试3"""
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys(u"中国2")
        driver.find_element_by_id("su").click()
        driver.close()


    def test_4(self):
        u"""测试4"""
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys(u"美国2")
        driver.find_element_by_id("su").click()
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()