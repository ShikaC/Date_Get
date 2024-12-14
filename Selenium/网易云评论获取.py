#导入webdriver
import csv
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 指定chromedriver的路径
service = Service(executable_path="./chromedriver.exe")

# 设置Chrome选项
chrome_options = Options()
# chrome_options.add_argument("--headless")  # 如果需要无头模式，可以取消注释这行

# 创建WebDriver对象
driver = webdriver.Chrome(service=service, options=chrome_options)

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
        with open("My Soul评论.csv",mode='a',newline='',encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([content])
    next = driver.find_element(By.LINK_TEXT, "下一页")
    next.click()
driver.quit()
