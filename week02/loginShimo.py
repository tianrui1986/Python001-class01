import requests


user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'

loginurl = 'https://shimo.im/lizard-api/auth/password/login'
headers = {
    'user-agent': user_agent, 
    'referer': 'https://shimo.im/login?from=home',
    'x-requested-with': 'XmlHttpRequest',
    'x-source': 'lizard-desktop',
}

# 登录用用户名与密码
form_data = {
    'email': '309925062@qq.com',
    'mobile': '+86undefined',
    'password': '987654321qwerwertt'
}



reponse = requests.post(loginurl, data=form_data, headers=headers)

print(reponse.status_code)
print(reponse.content)