from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

serv_obj = Service(r"C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://www.snapdeal.com/")
driver.get("https://www.amazon.com/")

driver.back()
time.sleep(5)
driver.forward()
time.sleep(5)
driver.refresh()
time.sleep(5)

driver.quit()