from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj = Service(r"C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://the-internet.herokuapp.com/nested_frames")
# driver.get("https://demo.automationtesting.in/Register.html")
driver.maximize_window()
driver.implicitly_wait(10)
#
driver.switch_to.frame("frame-bottom")
driver.switch_to.default_content()

# driver.switch_to.frame("basicBootstrapForm")
# driver.find_element(By.XPATH,"//*[@id='eid']/input").send_keys("seshu")

time.sleep(5)

driver.quit()


