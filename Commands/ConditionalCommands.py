from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service(r"C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.guru99.com/test/radio.html")
driver.maximize_window()

webelement = driver.find_element(By.XPATH,"//*[@id='navbar-brand-centered']/ul/li[9]/a")
print("Web Element Displayed:",webelement.is_displayed())
print("Web Element Enabled:",webelement.is_enabled())

option1 = driver.find_element(By.XPATH,"//input[@value='Option 1']")
print("Option1 Selected:",option1.is_selected())
option1.click()
print("Option1 Selected:",option1.is_selected())

checkbox1 = driver.find_element(By.XPATH,"//input[@id='vfb-6-0']")
print("CheckBox1 Selected:",checkbox1.is_selected())
checkbox1.click()
print("CheckBox1 Selected:",checkbox1.is_selected())

driver.quit()