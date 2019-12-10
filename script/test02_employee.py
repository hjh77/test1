import unittest

import api
from api.api_employee import ApiEmployee
from tools.read_json import read_json
from tools.assert_common import assert_common
from parameterized import parameterized


class TestEmployee(unittest.TestCase):
    # 初始化
    @classmethod
    def setUpClass(cls):
        cls.api = ApiEmployee()

    # 新增员工
    @parameterized.expand(read_json("a.json"))
    def test01_post(self, username, mobile, workNumber):
        # 调用新增员工接口
        r = self.api.post_empolyee(username, mobile, workNumber)
        print(r.json())
        api.user_id = r.json().get("data").get("id")
        assert_common(self, r)

    # 更新
    @parameterized.expand(read_json("b.json"))
    def test02_post(self, username):
        # 调用新增员工接口
        r = self.api.put_employee(username)
        print(r.json())
        assert_common(self,r)
    # 查询
    def test03_get(self):
        r = self.api.get_employee()
        print(r.json())
        assert_common(self,r)

    # 删除员工
    def test04_delete(self):
        r = self.api.delete_employee(api.user_id)
        print(r.json())
        assert_common(self, r)
