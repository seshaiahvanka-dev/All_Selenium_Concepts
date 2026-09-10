from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


serv_obj = Service(r"C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://money.rediff.com/index.html")
driver.maximize_window()

#Self
# driver.find_element(By.LINK_TEXT,"Gainers").click()
# name = driver.find_element(By.XPATH,"//*[@id='leftcontainer']/table/tbody/tr[5]/td[1]/a/self::a").text
# print(name)

#Parent
# driver.find_element(By.LINK_TEXT,"Gainers").click()
# name = driver.find_element(By.XPATH,"//*[@id='leftcontainer']/table/tbody/tr[5]/td[1]/a/parent::td").text

#Ancestor
# driver.find_element(By.LINK_TEXT,"Gainers").click()
# name = driver.find_element(By.XPATH,"//*[@id='leftcontainer']/table/tbody/tr[5]/td[1]/a/ancestor::tr").text
# print(name)

#Child
# driver.find_element(By.LINK_TEXT,"Gainers").click()
# name = driver.find_element(By.XPATH,"//*[@id='leftcontainer']/table/tbody/tr[5]/td[1]/a/ancestor::tr/child::td").text
# print(name)

#Descendant
# driver.find_element(By.LINK_TEXT,"Gainers").click()
# name = driver.find_element(By.XPATH,"//*[@id='leftcontainer']/table/tbody/tr[5]/descendant::a").text
# # name = driver.find_element(By.XPATH,"//*[@id='leftcontainer']/table/tbody/tr[5]/td[1]/a/ancestor::tr/descendant::a").text
# print(name)

#Following
# driver.find_element(By.LINK_TEXT,"Gainers").click()
# name = driver.find_element(By.XPATH,"//*[@id='leftcontainer']/table/tbody/tr[5]/following::tr").text
# name = driver.find_element(By.XPATH,"//*[@id='leftcontainer']/table/tbody/tr[5]/td[1]/a/ancestor::tr/following::tr").text
# print(name)

#Preceding
# driver.find_element(By.LINK_TEXT,"Gainers").click()
# name = driver.find_element(By.XPATH,"//*[@id='leftcontainer']/table/tbody/tr[5]/preceding::tr").text
# name = driver.find_element(By.XPATH,"//*[@id='leftcontainer']/table/tbody/tr[5]/td[1]/a/ancestor::tr/preceding::tr").text
# print(name)

#Following-Sibling
# driver.find_element(By.LINK_TEXT,"Gainers").click()
# name = driver.find_element(By.XPATH,"//*[@id='leftcontainer']/table/tbody/tr[5]/following-sibling::tr").text
# name = driver.find_element(By.XPATH,"//*[@id='leftcontainer']/table/tbody/tr[5]/td[1]/a/ancestor::tr/following-sibling::*").text
# print(name)

#Preceding-Sibling
driver.find_element(By.LINK_TEXT,"Gainers").click()
name = driver.find_element(By.XPATH,"//*[@id='leftcontainer']/table/tbody/tr[5]/preceding-sibling::tr").text
# name = driver.find_element(By.XPATH,"//*[@id='leftcontainer']/table/tbody/tr[5]/td[1]/a/ancestor::tr/preceding-sibling::*").text
print(name)
