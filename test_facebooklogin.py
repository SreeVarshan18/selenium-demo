from selenium import webdriver
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Chrome(ChromeDriverManager().install())
print("test case started")

driver.maximize_window()

driver.get("https://www.facebook.com/")
driver.find_element(by=By.NAME, value="email").send_keys("8825806302")
time.sleep(2)
driver.find_element(by=By.NAME, value="pass").send_keys("sreevarshan18*")
time.sleep(2)
driver.find_element(by=By.NAME, value="login").send_keys(Keys.ENTER)
time.sleep(10)
driver.close()
print("test case completed")