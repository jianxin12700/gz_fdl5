# 导包
import unittest
# 创建测试方法
import requests
import pprint

class TestProfile(unittest.TestCase):
    headers_data = {}

    @classmethod
    def setUpClass(cls) -> None:
        login_data = {"mobile": "13800000002", "password": "123456"}
        result = requests.post("http://182.92.81.159/api/sys/login", json=login_data).json()
        print("登录...:{}".format(result))
        str_data = result.get('data')
        token = "Bearer " + str_data
        TestProfile.headers_data['Authorization'] = token
        print(TestProfile.headers_data)

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    # 用户信息
    def test_profile(self):
        # 初始化数据
        # 请求接口
        result = requests.post("http://182.92.81.159/api/sys/profile", headers=TestProfile.headers_data).json()
        print(result)

        # 断言
        self.assertEqual("13800000002", result.get('data').get('mobile'))
        self.assertEqual("电饭锅电饭锅", result.get('data').get('roles').get('apis')[1])
