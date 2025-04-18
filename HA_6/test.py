import sys
import pytest
from selenium import webdriver
from pages.page import LoginPage, InventoryPage, CartPage
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class TestCheckoutProcess:

    @pytest.fixture(scope="class")
    def driver(self):
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com/")
        yield driver
        driver.quit()

    @pytest.fixture(scope="class")
    def login(self, driver):
        login_page = LoginPage(driver)
        credentials = {"user-name": "standard_user", "password": "secret_sauce"}
        login_page.login(credentials, "login-button")
        return driver

    @pytest.fixture(scope="class")
    def inventory_page(self, login):
        return InventoryPage(login)

    @pytest.fixture(scope="class")
    def cart_page(self, login):
        return CartPage(login)

    def test_checkout_process(self, inventory_page, cart_page):
        # Добавляем товары
        product_ids = [
            "add-to-cart-sauce-labs-backpack",
            "add-to-cart-sauce-labs-bolt-t-shirt",
            "add-to-cart-sauce-labs-onesie"
        ]
        for product_id in product_ids:
            assert inventory_page.add_product(product_id)


        result_url = inventory_page.open_page_via_element("shopping_cart_link", by=By.CLASS_NAME)
        assert result_url == "https://www.saucedemo.com/cart.html"

        # Переход к Checkout
        result_url = cart_page.go_to_checkout()
        assert result_url == "https://www.saucedemo.com/checkout-step-one.html"


        info = {
            "first-name": "Maryna",
            "last-name": "Shelenkova",
            "postal-code": "34563"
        }
        result_url = cart_page.fill_form(info, "continue")
        assert result_url == "https://www.saucedemo.com/checkout-step-two.html"


        total_text = cart_page.check_total("summary_total_label", by=By.CLASS_NAME).text
        total_value = float(total_text.replace("Total: $", ""))
        assert total_value == 58.29
