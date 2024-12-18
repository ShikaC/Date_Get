#导入webdriver
import csv
from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service('chromedriver.exe')
driver = Chrome(service=service)

driver.implicitly_wait(30)# 隐式等待，最多30秒

def getWeather(url):
    weather_info = []

    driver.get(url)
    more = driver.find_element(By.CSS_SELECTOR, '.lishidesc2')
    more.click()
    # 获取所有天气信息的li元素
    weather_elements = driver.find_elements(By.CSS_SELECTOR, ".thrui li")

    # 遍历所有天气信息的li元素
    for element in weather_elements:
        day_weather_info = {}

        day_weather_info["date_time"] = element.find_element(By.CSS_SELECTOR, "div:nth-of-type(1)").text.split(" ")[0]

        high = element.find_element(By.CSS_SELECTOR, "div:nth-of-type(2)").text
        day_weather_info["high"] = high[:high.find("℃")]

        low = element.find_element(By.CSS_SELECTOR, "div:nth-of-type(3)").text
        day_weather_info["low"] = low[:low.find("℃")]

        day_weather_info["weather"] = element.find_element(By.CSS_SELECTOR, "div:nth-of-type(4)").text
        weather_info.append(day_weather_info)

    return weather_info
    driver.quit()  # 关闭浏览器


weathers = []

for month in range(1, 13):
    weather_time = "2024" + ("0" + str(month) if month < 10 else str(month))
    url = f"https://lishi.tianqi.com/taizhou/{weather_time}.html"
    weather = getWeather(url)
    weathers.append(weather)

with open('台州2024天气.csv', 'w', newline='', encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["日期", "最高气温", "最低气温", "天气"])
    for month_weather in weathers:
        for day_weather_dict in month_weather:
            writer.writerow([day_weather_dict["date_time"],
                             day_weather_dict["high"],
                             day_weather_dict["low"],
                             day_weather_dict["weather"]])
# print(weathers)
print("over!")