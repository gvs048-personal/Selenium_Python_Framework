import time

from selenium import webdriver
from time import gmtime, strftime
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('disable-infobars')
driver = webdriver.Chrome(options=options)
driver.maximize_window()
#get method to launch the URL
driver.get("https://demoqa.com/automation-practice-form")

driver.find_element(By.ID,"dateOfBirthInput").clear()
driver.find_element(By.ID,"dateOfBirthInput").clear()
driver.find_element(By.ID,"dateOfBirthInput").send_keys("01-Jan-2024")
driver.find_element(By.ID,"dateOfBirthInput").clear()
#driver.find_element(By.ID,"dateOfBirthInput").click()
#time.sleep(5)
#driver.find_element(By.XPATH,"//div[contains(@aria-label,'13th')]").click()
time.sleep(10)