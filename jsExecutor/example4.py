# import the webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.maximize_window()
# get method to launch the URL
driver.get("https://www.softwaretestingmaterial.com/")
# to scroll with Javascript executor
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
# print the page title in console
print(driver.execute_script('return document.title'))
# print the page URL in console
print(driver.execute_script('return document.URL'))
# to close the browser
driver.close()
