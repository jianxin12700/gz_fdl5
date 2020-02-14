import requests
# 请求接口
login_data ={"keywords":"13210001000","password":"123qwe"}
response = requests.post("http://dev-www.zcbk.deayou.com/member/public/login",data=login_data)


# 查看结果
print(response.json())