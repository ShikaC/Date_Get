#导入webdriver
import csv
from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service('chromedriver.exe')
driver = Chrome(service=service)

driver.implicitly_wait(30)# 隐式等待，最多30秒

driver.get("https://music.163.com/#/song?id=5308028")
driver.switch_to.frame(0)
js = "document.documentElement.scrollTop = document.documentElement.scrollHeight"

for i in range(100):
    sleep(1)
    lst = driver.find_elements(By.CSS_SELECTOR, ".itm")
    driver.execute_script(js)  # 划到最下方
    for li in lst:
        content = li.find_element(By.CSS_SELECTOR, ".cnt").text
        # print(content)
        with open("My Soul评论.csv",mode='a',newline='',encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([content])
    next = driver.find_element(By.LINK_TEXT, "下一页")
    next.click()
driver.quit()
