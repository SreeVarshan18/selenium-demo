from selenium import webdriver
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Chrome(ChromeDriverManager().install())
print("test case started")

driver.maximize_window()

driver.get("https://www.google.co.in/")
driver.find_element(by=By.NAME, value="q").send_keys("harman")
time.sleep(2)
driver.find_element(by=By.NAME, value="btnK").send_keys(Keys.ENTER)
time.sleep(5)
driver.close()
print("test case completed")