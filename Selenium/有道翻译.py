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
# 加载有道翻译页面
driver.get("https://fanyi.youdao.com/#/TextTranslate")
sleep(1)
# 获取输入框
inputs = driver.find_element(By.ID, "js_fanyi_input")
# 输入内容
inputs.send_keys("hello")
sleep(1)

transTarget = driver.find_element(By.ID, "js_fanyi_output_resultOutput")
print(transTarget.text)