import unittest

import api
from api.api_login import ApiLogin
from tools.assert_common import assert_common


class TestLogin(unittest.TestCase):
    # 初始化
    @classmethod
    def setUpClass(cls):
        cls.api_login = ApiLogin()
    # 用例
    def test01_login(self,mobile="13800000002",password="123456"):
        r = self.api_login.api_login(mobile,password)
    # 断言
        print(r.json())
        assert_common(self, r)
        token = r.json().get("data")
        api.headers['Authorization'] = "Bearer " + token
        print(api.headers)


