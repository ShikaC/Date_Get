# 定位到2024必看热片
# 提取子页面的链接地址
# 请求子页面的链接地址，拿到下载地址

import requests
import re
import csv

domain = "https://www.dy2018.com/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
}

resp = requests.get(domain,headers=headers)
resp.encoding = "gbk" #指定字符集

# 定位2024必看热片
obj1 = re.compile(r"2024必看热片.*?<ul>(?P<ul>.*?)</ul>",re.S)
obj2 = re.compile(r"<a href='(?P<href>.*?)'",re.S)
obj3 = re.compile(r'◎片　　名(?P<Name>.*?)<br />.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf">'
                  r'<a href="(?P<download>.*?)">',re.S)


result1 = obj1.finditer(resp.text)
child_href_list = []
for i in result1:
    ul = i.group("ul")

    # 提取子页面链接
    result2 = obj2.finditer(ul)
    for j in result2:
        #拼接url:域名+子页面地址
        child_href = domain + j.group("href").strip("/")
        child_href_list.append(child_href) # 保存子页面链接

# 提取子页面内容
for href in child_href_list:
    child_resp = requests.get(href,headers=headers)
    child_resp.encoding = "gbk"
    result3 = obj3.finditer(child_resp.text)
    with open("电影天堂热片.csv","a",encoding="utf-8",newline="") as f:
        csv_writer = csv.writer(f)
        for k in result3:
            # print(k.group("No"))
            # print(k.group("Name"))
            # print(k.group("score"))
            download = k.groupdict()
            csv_writer.writerow(download.values())

    child_resp.close()
print("Over!")
resp.close()