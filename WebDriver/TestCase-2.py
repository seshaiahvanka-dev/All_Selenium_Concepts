from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service(r"C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://blazedemo.com/login")
driver.maximize_window()

driver.find_element(By.ID, "email").send_keys("admin@gmail.com")
driver.find_element(By.ID, "password").send_keys("admin123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
driver.quit()
