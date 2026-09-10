from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service(r"C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://parabank.parasoft.com/parabank/index.htm;jsessionid=3ADF2B33E7940EC22B2ADA3A5F547C66")
driver.maximize_window()

# driver.find_element(By.XPATH,"//input[@type='text' and @name='username']").send_keys("admin")
driver.find_element(By.XPATH,"//input[starts-with(@type,'te')]").send_keys("admin")
driver.find_element(By.XPATH,"//input[@type='password' or @name='password']").send_keys("admin123")
driver.find_element(By.XPATH,"//input[contains(@value,'Log In')]").click()
driver.find_element(By.XPATH,"//a[text()='Register']").click()

