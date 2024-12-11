# 提取页面源代码: requests
# 通过re提取有效信息: re
# 目前只能够爬取到228条数据，问题未知。

import requests
import re
import csv

for start in range(0,250,25):

    url = f"https://movie.douban.com/top250?start={start}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
    }

    resp = requests.get(url,headers=headers)
    page_content = resp.text

    # 解析数据
    obj = re.compile(r'<li>.*?<div class="item">.*?<em class="">(?P<No>.*?)</em>.*?<span class="title">(?P<Name>.*?)</span>.*?'
                     r'<p class="">.*?<br>(?P<Year>.*?)&nbsp.*?<span class="rating_num" property="v:average">'
                     r'(?P<score>.*?)</span>.*?<span>(?P<number>.*?)</span>.*?'
                     r'<span class="inq">(?P<Blurb>.*?)</span>',re.S)
    result =obj.finditer(page_content)
    with open('top250.csv',mode = 'a',encoding='utf-8',newline='')as f:
        csvWriter = csv.writer(f)

        for i in result:
            # print(i.group('No'))
            # print(i.group("Name"))
            # print(i.group("Year").strip())
            # print(i.group("score"))
            # print(i.group("number"))
            # print(i.group("Blurb"))

            top250 = i.groupdict()
            top250["Year"] = top250["Year"].strip()
            csvWriter.writerow(top250.values())

    f.close()
    resp.close()

print("over!")





