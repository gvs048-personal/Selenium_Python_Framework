# import the webdriver
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.maximize_window()
# get method to launch the URL
driver.get("https://the-internet.herokuapp.com/inputs")
# to enter text in edit box
tb = driver.find_element(By.XPATH,"//input[@type='number']")
tb.send_keys("1234")
#print(tb.text)
time.sleep(5)
# extract the value with Javascript Executor
print(driver.execute_script('document.getElementsByTagName("input")[0].valueAsNumber'))
