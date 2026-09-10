from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service(r"C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(10)

#Count the no of rows and Columns
rows = driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr")
# print(len(rows))
columns = driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr/th")
# print(len(columns))

#Read Specific Row and column Data
# row = driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[2]")
# print(row.text)

#Read all the rows and columns data
# rows= driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr")
# for row in rows:
#     print(row.text)

#Read data based on condition
for r in range(2,len(rows)+1):
    for c in range(1,len(columns)+1):
        authorname = driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[2]").text
        if authorname == "Mukesh":
            bookname=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[1]").text
            print(bookname,authorname)
            break

driver.quit()