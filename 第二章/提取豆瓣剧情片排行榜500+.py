


import requests
import re
import csv
url = "https://movie.douban.com/j/chart/top_list"

for start in range(0,600,20):
    param = {
        "type": "11",
        "interval_id": "100:90",
        "action": "",
        "start": f"{start}",
        "limit": "20"
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
    }

    resp = requests.get(url=url, params=param,headers=headers)
    page_content = resp.text
    # print(page_content)

    obj = re.compile(r'{"rating":.*?"rank":(?P<No>.*?),"cover_url".*?'
                     r'"title":"(?P<Name>.*?)".*?"score":"(?P<score>.*?)","actors":.*?"is_watched":false}',re.S)
    result = obj.finditer(page_content)

    with open("剧情好片500+.csv","a",encoding="utf-8",newline="") as f:
        csv_writer = csv.writer(f)
        for i in result:
            # print(i.group("No"))
            # print(i.group("Name"))
            # print(i.group("score"))

            top500 = i.groupdict()
            csv_writer.writerow(top500.values())

    f.close()
    resp.close()

print("over!")