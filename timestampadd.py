import time

import self
from selenium import webdriver
from time import gmtime, strftime

from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument('disable-infobars')
driver = webdriver.Chrome(options=options)
driver.get("http://www.google.com")
driver.find_element(By.NAME,"q").send_keys("James Stott{}".format(strftime("%Y-%m-%d %H:%M:%S", gmtime())))

time.sleep(15)