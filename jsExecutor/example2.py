# import the webdriver
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.maximize_window()
# get method to launch the URL
driver.get("https://the-internet.herokuapp.com/upload")
# to click on button with Javascript executor
btn = driver.find_element(By.ID,"file-submit")
driver.execute_script("arguments[0].click();",btn)
time.sleep(3)