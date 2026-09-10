from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

ser_obj = Service(r"C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service =ser_obj)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(10)

#Select Specific CheckBox
# driver.find_element(By.XPATH,"//input[@id='wednesday']").click()

#Select all the checkboxes
checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox' and @class='form-check-input']")
for checkbox in checkboxes:
    checkbox.click()
time.sleep(5)
#Select Multiple CheckBoxes by choice
# checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox' and @class='form-check-input']")
# for checkbox in checkboxes:
#     weekname = checkbox.get_attribute("id")
#     if weekname == "monday" or weekname == "wednesday" or weekname == "saturday":
#         checkbox.click()

#Select Last 2 Checkboxes
# checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox' and @class='form-check-input']")
# for checkbox in range((len(checkboxes)-2),len(checkboxes)):
#     checkboxes[checkbox].click()

#Select First 2 Checkboxes
# checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox' and @class='form-check-input']")
# for checkbox in range(len(checkboxes)):
#     if checkbox<2:
#         checkboxes[checkbox].click()

#Clear All Checkboxes
checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox' and @class='form-check-input']")
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()


time.sleep(5)
driver.quit()