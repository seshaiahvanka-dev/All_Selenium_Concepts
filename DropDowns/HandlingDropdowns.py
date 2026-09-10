from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

serv_obj = Service(r"C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(10)

drp_country = Select(driver.find_element(By.XPATH,"//select[@id='country']"))

#Select Option From the Dropdown
# drp_country.select_by_visible_text("India")
# drp_country.select_by_value("france")
# drp_country.select_by_index(3)

#Capture all the options and print them
alloptions = drp_country.options
# print(len(alloptions))
# for option in alloptions:
#     print(option.text)

#Select Option from dropdown without using built-in methods
for option in alloptions:
    if option.text =='India':
        option.click()
        break

time.sleep(5)
driver.quit()



