from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service(r"C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()
driver.implicitly_wait(10)

driver.switch_to.frame(0)
# driver.find_element(By.ID,"datepicker").send_keys("09/10/2026")
driver.find_element(By.ID,"datepicker").click()

year = "2022"
month = "June"
day = "10"

while True:
    mon = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    yr = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text
    if month == mon and year == yr:
        break
    else:
        driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-w']").click()
dates = driver.find_elements(By.XPATH,"//a[@class='ui-state-default']")
for date in dates:
    if date.text == day:
        date.click()
import time
time.sleep(5)

driver.quit()