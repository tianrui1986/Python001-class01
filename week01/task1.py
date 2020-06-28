# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

# 获取网页内容
url = "https://maoyan.com/films?showType=3"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
Cookie = "uuid_n_v=v1; uuid=73A84670B86F11EA909D9FF2C00A78C336F381410B1A45AD8F31F1947DC1123D; _csrf=d785ffa5fe6d8f82b6f5b75bd7a4ee70ebbed0a147eff24f05c3052baa9a972c; _lxsdk_cuid=172f5b16192c8-0a6f7139fdfbd9-4353760-144000-172f5b161921b; _lxsdk=73A84670B86F11EA909D9FF2C00A78C336F381410B1A45AD8F31F1947DC1123D; mojo-uuid=cd6b033fba6d946724b7d14876a0f1c6; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593259942,1593263151; mojo-session-id={\"id\":\"7eb0a3efa58d2beefb77fb5ff20fc89e\",\"time\":1593266187442}; mojo-trace-id=1; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593266188; __mta=174504477.1593259942553.1593263151593.1593266187964.3; _lxsdk_s=172f6103ded-1fa-ad0-80b%7C%7C3"
header = {"User-Agent": user_agent, "Cookie": Cookie}
response = requests.get(url, headers=header)
# print(response.text)

# 解析网页内容
bs_info = bs(response.text, 'html.parser')

datas_list = []
for tags in bs_info.find_all('dl', attrs={'class': 'movie-list'}):
    i = 0
    data_list = []
    for atag in tags.find_all('div', attrs={'class': 'movie-hover-title'}, limit=40):
        if i % 4 == 2:
            i += 1
            continue
        if i % 4 == 0:
            title = atag.find('span', {'class': 'name'}).text
            data_list.append(title)
            # print(title)
        if i % 4 == 1:
            movieType = atag.text.split('\n')[2].strip()
            data_list.append(movieType)
            # print(movieType)
        if i % 4 == 3:
            releaseTime = atag.text.split('\n')[2].strip()
            data_list.append(releaseTime)
            datas_list.append(data_list)
            data_list = []
            # print(releaseTime)
        i += 1 

print(datas_list)

# 将获取的数据存入CSV文件
movies = pd.DataFrame(data=datas_list)

movies.to_csv('./movies.csv', encoding='utf-8', index=False, header=False)