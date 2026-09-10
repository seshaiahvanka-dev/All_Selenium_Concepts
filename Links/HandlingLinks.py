from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests

serv_obj = Service(r"C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(10)

#Click On the Link
# driver.find_element(By.LINK_TEXT,"Udemy Courses").click()

#Find total Number of Links
# links = driver.find_elements(By.TAG_NAME,"a")
# print("No.Of Links:",len(links))

#Print All the links in tag(name)
# links = driver.find_elements(By.TAG_NAME,"a")
# for link in links:
#     print(link.text)

#Print All the links
# links = driver.find_elements(By.TAG_NAME,"a")
# for link in links:
#     print(link.get_attribute("href"))

#Count broken links
links = driver.find_elements(By.TAG_NAME,"a")
count =0
for link in links:
    url = link.get_attribute("href")
    try:
        res = requests.head(url)
    except:
        None
    if res.status_code >= 400:
        print(url,"is Broken Link")
        count += 1
    else:
        print(url,"is Valid Link")
print("No Of Broken Links:",count)
driver.quit()