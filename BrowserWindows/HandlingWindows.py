from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service(r"C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(10)

##Window Id == current_window_handle
# winId = driver.current_window_handle
# print(winId) #7C4E8DF146C6A053D1FC47888A57C975  #3D59C117423376A9F8DC10590F5D365C

##Multiple Windows  == window_handles
window = driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc")
window.click()
winIds = driver.window_handles
# print(winIds[0],winIds[1]) #D1269444D0B1C38B12F2A75652BEC254 #5E2148A39EEB3A21867161B11B488ED2

# driver.switch_to.window(winIds[1])
# print(driver.title)

# driver.switch_to.window(winIds[0])
# print(driver.title)

for win in winIds:
    driver.switch_to.window(win)
    print(driver.title)

for win in winIds:
    driver.switch_to.window(win)
    if driver.title=="OrangeHRM":
        driver.close()

# driver.quit()