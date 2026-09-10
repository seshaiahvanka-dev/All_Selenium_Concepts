from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service(r"C:\Drivers\edgedriver_win64\msedgedriver.exe")
driver = webdriver.Edge(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://www.saucedemo.com/")
driver.maximize_window()

# driver.find_element(By.ID, "user-name").send_keys("standard_user")   #ID
# driver.find_element(By.CSS_SELECTOR,"input#user-name").send_keys("standard_user") ##TAG AND ID
# driver.find_element(By.CSS_SELECTOR,"input.input_error.form_input").send_keys("standard_user")  ##TAG AND CLASS
# driver.find_element(By.CSS_SELECTOR,"input[type='text']").send_keys("standard_user")  ## TAG AND ATTRIBUTE
driver.find_element(By.CSS_SELECTOR,"input.input_error.form_input[type='text']").send_keys("standard_user")  ## TAG AND ATTRIBUTE AND CLASSNAME
driver.find_element(By.NAME, "password").send_keys("secret_sauce")  #NAME
driver.find_element(By.CLASS_NAME, "submit-button").click()
# import time
# time.sleep(5)
driver.quit()

