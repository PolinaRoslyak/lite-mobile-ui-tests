from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from base.base_class import Base


class ItemCard(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    item_name_item_card = "//h1[@itemprop='name']"
    cart_button = "/html/body/main/div[1]/div[5]/div/div[2]/div[2]/div[3]/div[1]/div/div[5]/a[1]"
    checkout_button = "//*[@id='cart-popup']/div/div[4]/a/span[2]"
    price_item_card = "/html/body/main/div[1]/div[5]/div/div[2]/div[2]/div[3]/div[1]/div/div[3]/div[1]"

    # Getters

    def get_item_name_item_card(self):
        return WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable((By.XPATH, self.item_name_item_card)))

    def get_cart_button(self):
        return WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable((By.XPATH, self.cart_button)))

    def get_checkout(self):
        return WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable((By.XPATH, self.checkout_button)))

    def get_price_item_card(self):
        return WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable((By.XPATH, self.price_item_card)))

    # Actions
    def click_cart_button(self):
        self.get_cart_button().click()
        print("click Buy")

    def click_checkout_button(self):
        self.get_checkout().click()
        print("click Checkout")

    # Methods
    def check_item(self):
        list_for_comparison_item_card = [self.save_text_for_comparison(self.get_item_name_item_card()),
                                         self.save_text_for_comparison(self.get_price_item_card())]
        return list_for_comparison_item_card

    def buy_item(self):
        self.get_current_url()
        self.click_cart_button()
        self.click_checkout_button()

    # def save_title(self):
    #     saved_title = self.get_item_name().text
    #     print(saved_title)
    #     return saved_title
    #
    # def save_price(self):
    #     saved_price = self.get_price().text
    #     print(saved_price)
    #     return saved_price
