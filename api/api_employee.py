# 初始化
import requests

import api


class ApiEmployee:
    def __init__(self):
        self.url_add = api.BASE_URL + "/api/sys/user"
        self.url_employee = api.BASE_URL + "/api/sys/user/{}"

    # 新增员工
    def post_empolyee(self, username, mobile, workNumber):
        data = {"username": username,
                "mobile": mobile,
                "workNumber": workNumber}

        return requests.post(url=self.url_add, json=data, headers=api.headers)

    # 修改员工
    def put_employee(self, username):
        data = {"username": username}
        return requests.put(url=self.url_employee.format(api.user_id), json=data, headers=api.headers)

    # 查询员工
    def get_employee(self):
        return requests.get(url=self.url_employee.format(api.user_id), headers=api.headers)

    # 删除员工
    def delete_employee(self, user_id):
        return requests.delete(url=self.url_employee.format(user_id), headers=api.headers)
