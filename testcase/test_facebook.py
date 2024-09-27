import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.find_element(By.ID,"email").send_keys("standard_user")
driver.find_element(By.NAME,"pass").send_keys("secret_sauce")
driver.find_element(By.NAME,"login").click()
time.sleep(30)