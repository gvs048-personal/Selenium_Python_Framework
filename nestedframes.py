import time

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.maximize_window()
# get method to launch the URL
# https://www.softwaretestingmaterial.com/sample-webpage-to-automate/
driver.get("https://the-internet.herokuapp.com/nested_frames")

driver.switch_to.frame("frame-top")
driver.switch_to.frame("frame-middle")
right=driver.find_element(By.TAG_NAME, 'body').text
print(right)
time.sleep(10)