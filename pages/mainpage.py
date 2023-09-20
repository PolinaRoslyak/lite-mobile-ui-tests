from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from base.base_class import Base
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException


class MainPage(Base):
    # Locators
    phones = "/html/body/header/nav[1]/ul/li[3]/a"
    phones_title = "/html/body/main/div[2]/div/div/div[1]/h1"
    assertion_text = "Мобильные телефоны (смартфоны)"
    form_search = "//input[@placeholder='Введите название или бренд. Найдем все!']"
    specific_smartphone_base_xpath = "//a[@href="
    iphone13 = '"/smartfon-apple-iphone-13-128gb-nfc-cvet-midnight-1"]'
    ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)

    # Getters
    def get_phones(self):
        return WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable((By.XPATH, self.phones)))

    def get_phones_title(self):
        return WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable((By.XPATH, self.phones_title)))

    def get_form_search(self):
        return WebDriverWait(self.driver, 20, ignored_exceptions=self.ignored_exceptions) \
            .until(ec.element_to_be_clickable((By.XPATH, self.form_search)))

    def get_iphone13(self):
        return WebDriverWait(self.driver, 20). \
            until(ec.element_to_be_clickable((By.XPATH, self.specific_smartphone_base_xpath + self.iphone13)))

    # Actions
    def click_phones(self):
        self.get_phones().click()
        print("Click phones button")

    def click_item(self, item_xpath):
        item_xpath.click()
        print("Click chosen item")

    # Methods
    def open_phones(self):
        self.get_current_url()
        self.click_phones()
        self.assert_word(self.get_phones_title(), self.assertion_text)

    def find_iphone13(self):
        self.get_current_url()
        self.get_form_search().send_keys("Iphone13")
        self.click_item(self.get_iphone13())
        self.move_to_page(1)
