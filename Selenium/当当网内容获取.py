#导入webdriver
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

driver.get("https://www.dangdang.com/")
# sleep(1)
# 获取输入框
key = driver.find_element(By.ID,"key_S")
key.send_keys("科幻")
#获取搜索框，点击搜索
search = driver.find_element(By.CSS_SELECTOR,".search .button")
search.click()
# sleep(1)
#获取商品标题及价格
for i in range(5):
    shoplist = driver.find_elements(By.CSS_SELECTOR, ".shoplist li")
    for li in shoplist:
        print(li.find_element(By.CSS_SELECTOR, "a").get_attribute("title"))
        print(li.find_element(By.CSS_SELECTOR, ".search_now_price").text)
    #获取下一页按钮
    next = driver.find_element(By.LINK_TEXT,"下一页")
    next.click()