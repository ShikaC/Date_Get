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

driver.get("https://fanyi.youdao.com/#/TextTranslate")
sleep(1)
print(driver.title) # 获取页面title
print(driver.current_url) # 获取当前页面URL

# 获取输入框
inputs = driver.find_element(By.ID, "js_fanyi_input")
inputs.send_keys("hello")
sleep(1)

print(inputs.text)# 获取元素文本
print(inputs.size)# 返回元素大小
print(inputs.get_attribute("href")) # 获取属性值
print(inputs.is_displayed())# 判断元素是否可见
print(inputs.is_enabled())# 判断元素是否可用

