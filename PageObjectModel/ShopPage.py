from selenium.webdriver.common.by import By

from PageObjectModel.checkout_confirmation import CheckOut_Confirmation
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ShopePage:

    def __init__(self,driver):
        self.driver = driver
        self.shop_link = (By.LINK_TEXT,"Shop")
        self.products_card = (By.XPATH, "//div[@class='card h-100']")
        self.check_to_cart = (By.CSS_SELECTOR, "a[class*='btn-primary']")



    def add_product_to_cart(self,product_name):    # add palce prrduct_ name = blackberry

        self.driver.find_element(*self.shop_link).click()  # //a[contains(@href,'shop')]    a[href*='shop']
        products = self.driver.find_elements(*self.products_card)

        wait = WebDriverWait(self.driver, 7)

        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            if productName == product_name:  # Replacing 'blackberry'
                add_to_cart_button = wait.until(
                    EC.element_to_be_clickable(product.find_element(By.XPATH, "div/button")))
                add_to_cart_button.click()
                print(f"Clicked on {productName} and added it to the cart.")

    def goToCart(self):
        self.driver.find_element(*self.check_to_cart).click()
        checkout_confirmation = CheckOut_Confirmation(self.driver)
        return checkout_confirmation


