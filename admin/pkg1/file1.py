from selenium import webdriver
import time
driver=webdriver.Chrome(executable_path="C:\\Users\\Admin\\Desktop\\driver3\\chromedriver.exe")

driver.get("https://www.amazon.in")
driver.maximize_window()
time.sleep(2)

searchitemelement=driver.find_element_by_id("twotabsearchtextbox")
searchitemelement.send_keys("Iphone X")
time.sleep(2)

searchbutton=driver.find_element_by_id("nav-search-submit-button")
searchbutton.click()
time.sleep(2)

selectitem=driver.find_element_by_link_text("Apple iPhone 13 (128GB) - Starlight")
selectitem.click()
