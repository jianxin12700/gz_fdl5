import unittest

from api.api_login import ApiLogin
from setting import headers_data


class TestUserList(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        #请求登录
        cls.login = ApiLogin()
        headers_data = cls.login.login("13800000002","123456")

    #测试用户列表
    def test_user_list(self):
        #请求接口
        result = self.login.user_list(headers_data)
        print(result)
        #断言
        self.assertEqual(10000,result.get('code'))
        self.assertEqual("13800000002",result.get('data').get('rows')[0].get('mobile'))
