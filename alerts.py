import time

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.maximize_window()
# get method to launch the URL
# https://www.softwaretestingmaterial.com/sample-webpage-to-automate/
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
#alert
#driver.find_element(By.XPATH,"//button[contains(text(),'Alert')]").click()
#alert = driver.switch_to.alert
#confirmation
#driver.find_element(By.XPATH,"//button[contains(text(),'Confirm')]").click()
#alert = driver.switch_to.alert
#Prompt
driver.find_element(By.XPATH,"//button[contains(text(),'Prompt')]").click()
alert = driver.switch_to.alert
time.sleep(5)
alert.send_keys("selenium")
alert.accept()
#alert.dismiss()
time.sleep(5)