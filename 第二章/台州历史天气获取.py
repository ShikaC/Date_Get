import requests
from lxml import etree
import csv
# 该代码不完善，只能爬取每月的前十天，改进后的代码在selenium文件夹中
def getWeather(url):
    weather_info = []

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
    }

    resp = requests.get(url, headers=headers)
    resp_html = etree.HTML(resp.text)

    resp_list = resp_html.xpath("//ul[@class='thrui']/li")
    for li in resp_list:
        day_weather_info = {}
        day_weather_info["date_time"]=li.xpath("./div[1]/text()")[0].split(" ")[0]

        high = li.xpath("./div[2]/text()")[0]
        day_weather_info["high"]=high[:high.find("℃")]
        low = li.xpath("./div[3]/text()")[0]
        day_weather_info["low"]=low[:low.find("℃")]
        day_weather_info["weather"]=li.xpath("./div[4]/text()")[0]
        weather_info.append(day_weather_info)
    print(weather_info)
    resp.close()
    return weather_info

weathers = []

for month in range(1, 13):
    weather_time = "2024" + ("0" + str(month) if month < 10 else str(month))
    # print(weather_time)
    url = f"https://lishi.tianqi.com/taizhou/{weather_time}.html"
    weather = getWeather(url)
    weathers.append(weather)

print(weathers)

with open('台州2024天气.csv', 'w', newline='', encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["日期","最高气温","最低气温","天气"])
    for month_weather in weathers:
        for day_weather_dict in month_weather:
            writer.writerow([day_weather_dict["date_time"],
                             day_weather_dict["high"],
                             day_weather_dict["low"],
                             day_weather_dict["weather"]])

print("over!")

