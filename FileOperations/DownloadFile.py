import os

from selenium.webdriver.common.by import By

location = os.getcwd()
def chrome_setup():
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service

    serv_obj = Service(r"C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
    options = webdriver.ChromeOptions()
    preferences = {"download.default_directory": location}
    options.add_experimental_option("prefs", preferences)
    driver = webdriver.Chrome(service=serv_obj, options=options)
    return driver
driver = chrome_setup()
driver.get("https://the-internet.herokuapp.com/download")
driver.find_element(By.XPATH, "//a[normalize-space()='r2_test_upload_9sn5ps84.txt']").click()
driver.quit()
