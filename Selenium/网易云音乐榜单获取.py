import csv
import csvwriter
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service('chromedriver.exe')
driver = Chrome(service=service)

driver.implicitly_wait(30)# 隐式等待，最多30秒

driver.get(url="https://music.163.com/#/discover/toplist")
driver.switch_to.frame('contentFrame')

with open('网易云热歌.csv', "w", encoding='utf-8', newline='') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(["歌名", "歌手"])
    for i in range(1, 5):
        xpath_expression = f'//*[@id="toplist"]/div[1]/div/ul[1]/li[{i}]'
        driver.find_element(By.XPATH, xpath_expression).click()
        time.sleep(2)
        divs = driver.find_elements(By.XPATH, '//*[@class="j-flag"]/table/tbody/tr')
        for div in divs:
            song_name = div.find_element(By.XPATH, './/div[@class="ttc"]//b').get_attribute('title')
            singer_name = div.find_element(By.XPATH, './td/div[@class="text"]/span').get_attribute('title')

            # 解决 &nbsp; 问题
            song_name = song_name.replace(u'\xa0', ' ')
            singer_name = singer_name.replace(u'\xa0', ' ')

            csvwriter.writerow([song_name, singer_name])
driver.quit()
print("over")