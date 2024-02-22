import time
from PIL import Image

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

# driver.maximize_window()
# get method to launch the URL
# https://www.softwaretestingmaterial.com/sample-webpage-to-automate/
driver.get("https://the-internet.herokuapp.com/key_presses")

driver.save_screenshot("screenshots/image3.png")

# Loading the image
#image = Image.open('image.png')

# Showing the image
#image.show()
