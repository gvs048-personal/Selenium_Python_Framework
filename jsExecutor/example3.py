# import the webdriver
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.maximize_window()
# get method to launch the URL
driver.get("https://demoqa.com/books")
driver.find_element(By.XPATH,"//input[@type='number']").send_keys("5")
# to scroll with Javascript executor
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
time.sleep(3)
