from time import sleep

import requests
import re
import csv
url = "https://music.163.com/discover/toplist?id=19723756"
ids = [19723756,3779629,2884035,3778678,6723173524,8246775932]
#id分别对应飙升榜、新歌榜、原创榜、热歌榜、网络热歌榜、实时热度榜
for id in ids:
     param = {
        "id": f"{id}",
     }
     headers = {
          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
     }

     resp = requests.get(url=url,headers=headers)
     page_content = resp.text
     sleep(2)

     obj = re.compile(r'<li><a href="/song.*?">(?P<Name>.*?)</a></li>',re.S)
     result =obj.finditer(page_content)

     with open("网易云热歌.csv",mode = "a",encoding="utf-8",newline="") as f:
          writer = csv.writer(f)
          for i in result:
               writer.writerow(i.groups())

     resp.close()
print("over!")