from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj = Service(r"C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

# driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth") ##Authentication Popup
driver.maximize_window()
driver.implicitly_wait(10)
# Opens Alert Window
# driver.find_element(By.XPATH,"//*[@id='content']/div/ul/li[1]/button").click()
# driver.switch_to.alert.accept()

#Prints Alert Message
# driver.find_element(By.XPATH,"//*[@id='content']/div/ul/li[1]/button").click()
# alertwindow = driver.switch_to.alert
# print(alertwindow.text)
# alertwindow.dismiss()

#Enter the value into alert
# driver.find_element(By.XPATH,"//*[@id='content']/div/ul/li[3]/button").click()
# alertwindow = driver.switch_to.alert
# alertwindow.send_keys("Welcome")
# alertwindow.accept()


time.sleep(5)
driver.quit()