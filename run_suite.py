import unittest
from tools.HTMLTestReportCN import HTMLTestRunner

suite = unittest.defaultTestLoader.discover("./script")
with open("./report/report.html", "wb") as f:
    HTMLTestRunner(stream=f).run(suite)
    print("11111111111")