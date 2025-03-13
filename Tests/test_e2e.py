import json

import pytest
from selenium import webdriver
#chrome driver
from selenium.webdriver.chrome.service import Service
#-- Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from PageObjectModel.ShopPage import ShopePage
from PageObjectModel.checkout_confirmation import CheckOut_Confirmation
from PageObjectModel.form_subbmison import Form_sumisson


# to read test data from json file steps to do

test_data_path = "D:/PythonProject/SeleniumProject1/data/test_e2e.json"

     # step1 '../' to come out of test file #S2 Data/ to go for json package #S3 use json file path test_e2e.json
with open(test_data_path) as f:   # file to read

    test_data = json.load(f)
    test_list = test_data["data"]

                        # variable to hold test list
@pytest.mark.parametrize("test_list_items",test_list)  #test_list put this in
def test_e2e(browserInstance,test_list_items):
    driver = browserInstance  # to call driver from conftest

    form_Submisson = Form_sumisson(driver)
    print(form_Submisson.getTitel())
    shop_page =form_Submisson.formSubbison(test_list_items["username"],test_list_items["email"],test_list_items["password"],test_list_items["drop_down"])

                                                     #"pradeep","pradeepf679@gmail.com","Pradeep@123","Male"
    shop_page.add_product_to_cart(test_list_items["product_name"])   #Blackberry
    checkout_confirmation = shop_page.goToCart()
    #checkout_confirmation.checkout()
    checkout_confirmation.check_out_button()
    checkout_confirmation.enter_country("ind")
    checkout_confirmation.validting()



    # driver.find_element(By.ID,"country").send_keys("ind")
    # wait = WebDriverWait(driver,10)
    # wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
    # driver.find_element(By.LINK_TEXT,"India").click()
    # driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
    # driver.find_element(By.CSS_SELECTOR,"[type='submit']").click()
    # successText = driver.find_element(By.CLASS_NAME,"alert-success").text
    # assert "Success! Thank you!" in successText
    # driver.close()








# def pytest_addoption(parser):
#     parser.addoption(
#         "--browser_name", action="store", default="type1", help="my option: type1 or type2"
#     )
#
#
# def browserInstance(request):
#     browser_name = request.config.getoption("browser_name")
#     if browser_name == "chrome":
#         driver = webdriver.Chrome()
#     elif browser_name == "firfox":
#         driver = webdriver.Firefox()
#     elif browser_name == "edge":
#         driver = webdriver.Edge()
#         driver.implicitly_wait(4)
#     driver.get("https://rahulshettyacademy.com/angularpractice/")
#     yield driver
#
#











