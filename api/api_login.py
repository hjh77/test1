import requests

import api
from api import BASE_URL, headers


class ApiLogin:
    # 初始化
    def __init__(self):
        # 初始化url
        self.url = BASE_URL + "/api/sys/login"

    # 登录
    def api_login(self, mobile, password):
        data = {"mobile": mobile, "password": password}
        return requests.post(url=self.url, json=data, headers=headers)

