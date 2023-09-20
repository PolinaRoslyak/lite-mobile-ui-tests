from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pages.itemcard import ItemCard


class CartPage(ItemCard):

    # Locators
    name = "//input[@id='firstname-ch']"
    surname = "//input[@id='lastname-ch']"
    email = "//input[@id='email-ch']"
    phone_number = "//input[@id='telephone-ch']"
    title_name_checkout = "//*[@id='order-cart']/div[1]/div/div[1]/div"
    price_checkout = "//*[@id='order-cart']/div[1]/div/div[2]/div[2]"
    checkbox_user_agreement = "/html/body/main/main/div[3]/div/div/div[1]/form/div[6]/div[2]/div[2]/label/span[1]"
    checkbox_privacy_policy = "/html/body/main/main/div[3]/div/div/div[1]/form/div[6]/div[2]/div[3]/label/span[1]"
    close_user_agreement = "//*[@id='ch-agree_checkbox']/button/svg"
    close_privacy_policy = "//*[@id='ch-agree_checkbox']/button/svg"
    total_amount = "/html/body/main/main/div[3]/div/div/div[1]/form/div[6]/div[1]/div[4]/div[1]"
    accept_cookie_button = "//*[@id='cookie_note']/button"

    # Getters
    def get_name(self):
        return WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable((By.XPATH, self.name)))

    def get_surname(self):
        return WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable((By.XPATH, self.surname)))

    def get_email(self):
        return WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable((By.XPATH, self.email)))

    def get_phonenumber(self):
        return WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable((By.XPATH, self.phone_number)))

    def get_title_name_checkout(self):
        return WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable((By.XPATH, self.title_name_checkout)))

    def get_price_checkout(self):
        return WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable((By.XPATH, self.price_checkout)))

    # this block could be useful for first run
    # def get_close_user_agreement(self):
    #     return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.close_user_agreement)))
    #
    # def get_close_privacy_policy(self):
    #     return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.close_privacy_policy)))

    def get_cookie_accept(self):
        return WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable((By.XPATH, self.accept_cookie_button)))

    # Actions
    def send_name(self, name):
        self.get_name().send_keys(name)
        print("Send name")

    def send_surname(self, surname):
        self.get_surname().send_keys(surname)
        print("Send surname")

    def send_email(self, email):
        self.get_email().send_keys(email)
        print("Send email")

    def send_phonenumber(self, phonenumber):
        self.get_phonenumber().send_keys(phonenumber)
        print("Send phone number")

    def click_checkbox_user_agreement(self):
        element = self.driver.find_element(By.XPATH, self.checkbox_user_agreement)
        self.driver.execute_script("arguments[0].click();", element)
        print("click checkbox user agreement")
        # probably need to use if you run first time
        # self.get_close_user_agreement().click()

    def click_checkbox_privacy_policy(self):
        element = self.driver.find_element(By.XPATH, self.checkbox_privacy_policy)
        self.driver.execute_script("arguments[0].click();", element)
        print("click checkbox privacy policy")
        # probably need to use if you run first time
        # self.get_close_privacy_policy().click()

    def click_accept_cookie(self):
        self.get_cookie_accept().click()
        print("accepted cookie")

    # Methods
    def fill_checkout_form_without_auth(self):
        self.get_current_url()
        self.assert_word(self.get_name(), "")
        self.send_name("Ivan")
        self.assert_word(self.get_surname(), "")
        self.send_surname("Ivanov")
        self.assert_word(self.get_email(), "")
        self.send_email("test@yandex.ru")
        self.assert_word(self.get_phonenumber(), "")
        self.send_phonenumber("9000000000")
        self.click_accept_cookie()
        self.click_checkbox_user_agreement()
        self.click_checkbox_privacy_policy()

    def check_item_and_price(self):
        list_for_comparison_checkout = [self.save_text_for_comparison(self.get_title_name_checkout()),
                                        self.save_text_for_comparison(self.get_price_checkout())]
        return list_for_comparison_checkout

    def fill_checkout_form_with_auth(self):
        self.get_current_url()
        self.send_surname("Ivanova")
        self.send_phonenumber("9000000000")
        self.click_accept_cookie()
        self.click_checkbox_user_agreement()
        self.click_checkbox_privacy_policy()
