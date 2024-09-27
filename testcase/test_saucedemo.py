import time
import pytest
from selenium import webdriver
from pages.addproduct import AddProduct
from pages.loginpage import LoginPage
from pages.sauce import AddProduct1
@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
class TestA:
    def test_addproduct1(self, setup):
        self.driver=setup
        self.driver.get("https://www.saucedemo.com/v1/")
        self.lp=LoginPage(self.driver)
        self.lp.login("standard_user","secret_sauce")
        self.addprod=AddProduct1(self.driver)
        self.addprod.addproduct1()
        time.sleep(10)