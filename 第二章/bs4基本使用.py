# pip install bs4
# 拿到页面源代码
# 使用bs4进行解析

import requests
from bs4 import BeautifulSoup
import csv

url = "http://www.vegnet.com.cn/Price/list_ar330000.html?marketID=null"
resp = requests.get(url)


# 解析数据
# 把页面源代码交给BeautifulSoup进行处理，生成bs对象
page = BeautifulSoup(resp.text, 'html.parser')# 指定html解释器

# 从bs对象中查找数据
# find(标签, 属性 = 值)
# find_all(标签, 属性)
# table = (page.find("div",class_="jxs_list price_l"))
table = page.find("div",attrs = {"class":"jxs_list price_l"})# 与上行同义

titles = table.find("p",class_= "skin_gre")
title_spans = titles.find_all("b")

data_rows = table.find("div", class_="pri_k")
p_tags = data_rows.find_all("p")

f = open("菜价.csv",mode="w",newline="",encoding="utf-8")
writer = csv.writer(f)

for p in p_tags:
    spans = p.find_all("span")
    Date = spans[0].text
    Name = spans[1].text
    Market = spans[2].text
    Low = spans[3].text
    High = spans[4].text
    avg = spans[5].text
    unit = spans[6].text
    writer.writerow([])
    writer.writerow([Date, Name, Market, Low, High, avg, unit])
f.close()
resp.close()
print("over!")
