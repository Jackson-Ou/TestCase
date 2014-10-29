# -*- coding: utf-8 -*-
import unittest, time
import HTMLTestRunner
import sys
sys.path.append("\testcase")
from testcase.my_test1 import my_test1
from testcase.my_test2 import my_test2


now=time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
Browsers=['Ie','Chrome','Firefox']
TestClasses=[my_test1,my_test2]
for Browser in Browsers:
	testunit=unittest.TestSuite()
	for TestClass in TestClasses:
		TestClass.Browser=Browser
		testunit.addTest(unittest.makeSuite(TestClass))
	filename="C:\\Study_Selenium\\report\\Report_"+now+"_"+Browser+".html"
	fp=file(filename,'wb')
	runner=HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'测试报告', description=u'用例执行情况')
	runner.run(testunit)
	fp.close()
	print 'Report:'+'C:\\Study_Selenium\\report\\Report_'+now+'_'+Browser+'.html'
