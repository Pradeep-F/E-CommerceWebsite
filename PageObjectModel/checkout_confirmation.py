from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class CheckOut_Confirmation:

    def __init__(self,driver):
        self.driver = driver
        #self.checkOut_button = (By.CSS_SELECTOR, "a[class*='btn-primary']")
        self.checkOutButton = (By.XPATH, "//button[@class='btn btn-success']")
        self.search_county = (By.ID, "country")
        self.country_name = (By.LINK_TEXT,"India")
        self.checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
        self.submit_button = (By.CSS_SELECTOR, "[type='submit']")
        self.success_text = (By.CLASS_NAME, "alert-success")

    # def checkout(self):
    #     self.driver.find_element(*self.checkOut_button).click()

    def check_out_button(self):
        self.driver.find_element(*self.checkOutButton).click()


    def enter_country(self,country_Name):
        self.driver.find_element(*self.search_county).send_keys(country_Name)

        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((self.country_name)))    # By.LINK_TEXT, "india" insted we call tuple

        self.driver.find_element(*self.country_name).click()
        self.driver.find_element(*self.checkbox).click()
        self.driver.find_element(*self.submit_button).click()


    def validting(self):
        successText = self.driver.find_element(*self.success_text).text
        assert "Success! Thank you!" in successText