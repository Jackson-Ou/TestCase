# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

#使用htmlunit需要开启selenium-server-standalone-2.43.1.jar(开启命令java -jar selenium-server-standalone-2.43.1.jar)
class vote(unittest.TestCase):
    def setUp(self):
		self.driver = webdriver.Remote("http://localhost:4444/wd/hub", webdriver.DesiredCapabilities.HTMLUNIT)
		self.driver.implicitly_wait(30)
		self.base_url = "http://www.surveyportal.cn/survey/vs.aspx?id=18869&source=link"
		self.verificationErrors = []
		self.accept_next_alert =True
    
    def test_1(self):
		driver = self.driver
		driver.get(self.base_url)
		for i in range(0,10000):
			driver.find_element_by_id("q1_2").click()
			driver.find_element_by_id("submit_button").click()
			driver.back()
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
	unittest.main(exit=False)

