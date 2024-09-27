from selenium.webdriver.common.by import By
class AddProduct1:
    bpack="Backpack"
    inven=".btn_primary.btn_inventory"
    tag_name="path"
    XPATH1="//*[contains(text(),'CHECKOUT')]"
    cart=".btn_primary.cart_button"
    sauc=".btn_action.cart_button"
    use="form_input"
    pss="last-name"
    plase="postal-code"
    def __init__(self, driver):
        self.driver = driver

    def addproduct1(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, self.bpack).click()
        self.driver.find_element(By.CSS_SELECTOR, self.inven).click()
        self.driver.find_element(By.TAG_NAME, self.tag_name).click()
        self.driver.find_element(By.XPATH,self.XPATH1).click()
        self.driver.find_element(By.CLASS_NAME,self.use).send_keys("standard_user")
        self.driver.find_element(By.ID,self.pss).send_keys("")
        self.driver.find_element(By.ID,self.plase).send_keys("600062")
        self.driver.find_element(By.CSS_SELECTOR, self.cart).click()
        self.driver.find_element(By.CSS_SELECTOR, self.sauc).click()
