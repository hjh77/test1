#导包
import unittest
from tools.HTMLTestReportCN import HTMLTestRunner
#创建测试套件
suite = unittest.defaultTestLoader.discover("./script")
#打开文件流 运行套件
with open("./report/report2.html","wb") as f:
    HTMLTestRunner(f).run(suite)

#run