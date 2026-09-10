from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service(r"C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj)
driver.implicitly_wait(10)

driver.get("https://parabank.parasoft.com/parabank/index.htm;jsessionid=B9AEB1F91A9CF90DB571602BA535D639")
driver.maximize_window()

driver.find_element(By.LINK_TEXT,"Register").click() #LINK_TEXT
# driver.find_element(By.PARTIAL_LINK_TEXT,"ter").click()  #PARTIAL_LINK_TEXT

# inputs = driver.find_elements(By.CLASS_NAME,"input")    ##CLASS_NAME
# print(len(inputs))    #2
# links = driver.find_elements(By.TAG_NAME,"a")           ##TAG_NAME
# print(len(links))     #33

