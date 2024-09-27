import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://www.saucedemo.com/v1/")
driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.NAME,"password").send_keys("secret_sauce")
driver.find_element(By.CLASS_NAME,"btn_action").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"Backpack").click()
driver.find_element(By.CSS_SELECTOR,".btn_primary.btn_inventory").click()
driver.find_element(By.TAG_NAME,"path").click()
driver.find_element(By.XPATH,"//*[contains(text(),'CHECKOUT')]").click()
driver.find_element(By.CLASS_NAME,"form_input").send_keys("standard_user")
driver.find_element(By.ID,"last-name").send_keys("secret_sauce")
driver.find_element(By.ID,"postal-code").send_keys("600062")
driver.find_element(By.CSS_SELECTOR,".btn_primary.cart_button").click()
driver.find_element(By.CSS_SELECTOR,".btn_action.cart_button").click()
time.sleep(10)