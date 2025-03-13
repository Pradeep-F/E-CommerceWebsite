from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from PageObjectModel.ShopPage import ShopePage
from utility.BaseClass import BaseClass


class Form_sumisson(BaseClass):
# this project is developed by pradeep using python
    def __init__(self,driver):
        super().__init__(driver)     # using baseclass to call driver from that
        self.driver = driver
        self.username = (By.NAME, "name")
        self.email = (By.NAME, "email")
        self.password = (By.ID, "exampleInputPassword1")
        self.drop_down = (By.ID, "exampleFormControlSelect1")
        self.radio_button = (By.ID, "inlineRadio2")
        self.submit = (By.XPATH, "//input[@type='submit']")



    def formSubbison(self,usernme,email,password,drop_down):
        self.driver.find_element(*self.username).send_keys(usernme)
        self.driver.find_element(*self.email).send_keys(email)
        self.driver.find_element(*self.password).send_keys(password)
        dropdown = Select(self.driver.find_element(*self.drop_down))
        dropdown.select_by_visible_text(drop_down)
        self.driver.find_element(*self.radio_button).click()
        self.driver.find_element(*self.submit).click()
        shop_page = ShopePage(self.driver)
        return shop_page