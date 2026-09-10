from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


serv_obj = Service(r"C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

# driver.get("https://www.amazon.com/")
# driver.maximize_window()
# driver.implicitly_wait(10)

#Mouse Hover
# act = ActionChains(driver)
# act.move_to_element(driver.find_element(By.XPATH,"//span[@id='nav-link-accountList-nav-line-1']")).perform()


#Right Click
# driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
# driver.maximize_window()
# driver.implicitly_wait(10)
#
# act = ActionChains(driver)
# act.context_click(driver.find_element(By.XPATH,"/html/body/main/p/span")).perform()

#Double Click
# driver.get("https://demoqa.com/buttons")
# driver.maximize_window()
# driver.implicitly_wait(10)
#
# act = ActionChains(driver)
# act.double_click(driver.find_element(By.ID,"doubleClickBtn")).perform()

#Drag And Drop
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(10)

# source_ele = driver.find_element(By.XPATH,"//div[@id='draggable']")
# target_ele = driver.find_element(By.XPATH,"//div[@id='droppable']")
#
# act = ActionChains(driver)
# act.drag_and_drop(source_ele,target_ele).perform()

#Slider
# min_slider = driver.find_element(By.XPATH,"//div[@id='HTML7']//span[1]")
# max_slider = driver.find_element(By.XPATH,"//div[@id='HTML7']//span[2]")
##Before Moving Sliders
# print(min_slider.location)  #{'x': 992, 'y': 2067}
# print(max_slider.location)  #{'x': 1100, 'y': 2067}

# act = ActionChains(driver)
# act.drag_and_drop_by_offset(min_slider,8,0).perform()
# act.drag_and_drop_by_offset(max_slider,-100,0).perform()
##Before Moving Sliders
# print(min_slider.location)
# print(max_slider.location)

#Scrolling page
# driver.execute_script("window.scrollBy(0,3000)")
# value = driver.execute_script("return window.pageYOffset;")
# print("No of pixes Moved",value)

#Scroll page till element is visible
element = driver.find_element(By.XPATH,"//label[normalize-space()='Colors:']")
driver.execute_script("arguments[0].scrollIntoView();", element)
value = driver.execute_script("return window.pageYOffset;")
print("No of pixes Moved",value)

#Scroll page till End
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
# time.sleep(5)

#Scroll page till Start
# driver.execute_script("window.scrollBy(0,-document.body.scrollHeight);")

time.sleep(5)

driver.quit()