from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
print("test case started")
driver.maximize_window()
driver.get("https://www.w3schools.com/")
driver.find_element(by=By.LINK_TEXT, value="Tutorials").click()
time.sleep(1)
driver.find_element(by=By.LINK_TEXT, value="Learn Python").click()
time.sleep(5)
driver.close()
print("test case completed")
