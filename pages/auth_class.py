from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from base.base_class import Base


class Auth(Base):
    url = 'https://lite-mobile.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    enter_button = "//a[@class='header-auth__btn']"
    user_name = "//*[@id='auth']/div/div[3]/div[1]/form/div[1]/div[1]/div[2]/input"
    password = "//*[@id='auth']/div/div[3]/div[1]/form/div[1]/div[2]/div[2]/input"
    login_button = "//*[@id='auth']/div/div[3]/div[1]/form/div[2]/button/span[2]"
    user_profile = "/html/body/header/div[1]/div[2]/div[1]/div/div/div/div[1]"
    assertion_profile_text = "Полина"
    wrong_email = "/html/body/div[15]/div[2]/div[4]/div/div/div/div[3]/div[1]/form/div[1]/div[1]/div[2]/input"
    wrong_password = "/html/body/main/main/div[3]/div/div/div[1]"
    assertion_wrong_password_text = "Неправильно заполнены поле E-Mail и/или пароль!"
    new_password = "/html/body/main/main/div[3]/div/div/div[2]/form/div[1]/div[2]/div[2]/input"
    second_login_button = "/html/body/main/main/div[3]/div/div/div[2]/form/div[2]/button"

    # Getters
    def get_enter_button(self):
        return WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable((By.XPATH, self.enter_button)))

    def get_user_name(self):
        return WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_user_profile(self):
        return WebDriverWait(self.driver, 60).until(ec.element_to_be_clickable((By.XPATH, self.user_profile)))

    def get_wrong_password(self):
        return WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable((By.XPATH, self.wrong_password)))

    def get_new_password(self):
        return WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, self.new_password)))

    def get_second_login_button(self):
        return WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, self.second_login_button)))

    # Actions
    def click_enter_button(self):
        self.get_enter_button().click()
        print("Click enter button")

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("Input user name")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_login_button(self):
        self.get_login_button().click()
        print("Click login button")

    def check_wrong_email(self):
        self.driver.find_element(By.XPATH, "//input[@placeholder='Укажите корректный E-mail']")
        print("form is red")

    def input_new_password(self, password):
        self.get_new_password().clear()
        self.get_new_password().send_keys(password)
        print("Send second password")

    def click_second_login_button(self):
        self.get_second_login_button().click()
        print("Click login again")

    # Methods
    def auth_on_site(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_enter_button()
        self.input_user_name("polina3169559@yandex.ru")
        self.input_password("qwerty12345")
        self.click_login_button()
        self.assert_word(self.get_user_profile(), self.assertion_profile_text)

    def enter_without_auth(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()

    def fail_email(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_enter_button()
        self.input_user_name("polina3169559@yandex.r")
        self.input_password("qwerty12345")
        self.click_login_button()
        self.check_wrong_email()
        self.get_user_name().clear()
        self.input_user_name("polina3169559@yandex.ru")
        self.click_login_button()
        self.assert_word(self.get_user_profile(), self.assertion_profile_text)

    def fail_password(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_enter_button()
        self.input_user_name("polina3169559@yandex.ru")
        self.input_password("qwerty1234")
        self.click_login_button()
        self.assert_word(self.get_wrong_password(), self.assertion_wrong_password_text)
        self.input_new_password("qwerty12345")
        self.click_second_login_button()
        self.assert_word(self.get_user_profile(), self.assertion_profile_text)
