from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service(r"C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj)
driver.implicitly_wait(10)

driver.get("https://admin-demo.nopcommerce.com/login")
driver.maximize_window()

driver.find_element(By.NAME,"Email").clear()
driver.find_element(By.NAME,"Email").send_keys("admin@yourstore.com")
driver.find_element(By.ID,"Password").clear()
driver.find_element(By.ID,"Password").send_keys("admin")
driver.find_element(By.XPATH,"//button[@type='submit']").click()

driver.quit()