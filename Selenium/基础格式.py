#导入webdriver
import csv
from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service('chromedriver.exe')
driver = Chrome(service=service)