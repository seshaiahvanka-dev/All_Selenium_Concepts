from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


serv_obj = Service(r"C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)
# mywait = WebDriverWait(driver, 10) ##explicit wait declaration basic
# mywait = WebDriverWait(driver, 10,poll_frequency=2,ignored_exceptions=[Exception])

driver.get("https://duckduckgo.com/")
driver.maximize_window()

searchbox = driver.find_element(By.NAME,"q")
searchbox.send_keys("")
searchbox.send_keys("Selenium")
searchbox.submit()

driver.find_element(By.XPATH,"//*[@id='r1-0']/div[3]/h2/a/span").click()

# searchlink = mywait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='r1-0']/div[3]/h2/a/span")))

driver.quit()
