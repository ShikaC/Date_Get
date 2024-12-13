#导入webdriver
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

# 访问百度
driver.get("http://www.baidu.com/")


# id="kw"是百度搜索输入框，输入字符串"长城"
kw = driver.find_element(By.ID,"kw")
kw.send_keys("长城")
# id="su"是百度搜索按钮，c1ick()是模拟点击
su = driver .find_element(By.CSS_SELECTOR,"#su")
# ID:#    CLASS:.
su.click()

#关闭浏览器
# driver.quit()


input()#防止闪退
