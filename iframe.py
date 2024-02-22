import time

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.maximize_window()
# get method to launch the URL
# https://www.softwaretestingmaterial.com/sample-webpage-to-automate/
driver.get("https://the-internet.herokuapp.com/iframe")
#driver.switch_to.frame(0) #index
#driver.switch_to.frame('mce_0_ifr') #id/name

iframe1=driver.find_element(By.CSS_SELECTOR, ".tox-edit-area__iframe")
driver.switch_to.frame(iframe1) # locator


driver.find_element(By.ID,"tinymce").send_keys("selenium")
time.sleep(10)