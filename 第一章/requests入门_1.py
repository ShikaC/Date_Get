# pip install requests  下载包
# 百度搜索

import requests
wd = input("请输入搜索内容：")

url = f'https://www.baidu.com/s?wd={wd}'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
}

resp = requests.get(url,headers=headers)# 处理反爬

print(resp)
print(resp.text)# 获取页面源代码
resp.close()