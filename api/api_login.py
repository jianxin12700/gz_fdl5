import requests

from setting import BASE_URL, headers_data


class ApiLogin(object):

    # 初始化
    def __init__(self):
        # 组装 登录url
        self.url_login = BASE_URL + "/api/sys/login"
        self.user_url = BASE_URL + "/api/sys/user?page=1&size=1"

    # 登录
    def login(self,mobile,password):
        login_data = {"mobile": mobile, "password": password}
        result = requests.post(self.url_login, json=login_data).json()
        data_str = result.get('data')
        token = "Bearer " + data_str
        headers_data['Authorization'] = token
        return headers_data

    # 用户列表
    def user_list(self, headers_data):
        try:
            return requests.get(self.user_url, headers=headers_data).json()
        except Exception as e:
            print("请求用户列表接口数据异常:{}".format(e))
