from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from base.base_class import Base


class Auth(Base):
    url = 'https://lite-mobile.ru/'

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
    profile_list_down = "//div[@class='header-auth__arr']"
    logout_option = "//a[@href='https://lite-mobile.ru/logout']"
    logout_url = "https://lite-mobile.ru/logout"
    foursquare = "//a[@href='https://ru.foursquare.com/litemobile']"
    vk = "//a[@href='https://vk.com/litemobileru']"
    telegram = "//a[@ href='https://t.me/litemobilenews']"
    youtube = "//a[@href='https://youtube.com/@litemobilenews']"
    yappy = "//a[@href='https://yappy.media/s/p_4wRg8RQPZcTnBM1TnNKNNr']"
    foursquare_link = "https://ru.foursquare.com/litemobile"
    vk_link = "https://vk.com/litemobileru"
    telegram_link = "https://t.me/litemobilenews"
    youtube_link = "https://www.youtube.com/@litemobilenews"
    yappy_link = "https://yappy.media/profile/94d74ed1-6e32-4b90-b3a1-008656decfbd?utm_" \
                 "source=url&utm_medium=share&utm_campaign=profile"

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

    def get_logout_option(self):
        return WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, self.logout_option)))

    def get_foursquare(self):
        return WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, self.foursquare)))

    def get_vk(self):
        return WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, self.vk)))

    def get_telegram(self):
        return WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, self.telegram)))

    def get_youtube(self):
        return WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, self.youtube)))

    def get_yappy(self):
        return WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, self.yappy)))

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

    def click_logout_option(self):
        self.get_logout_option().click()
        print("Click logout")

    def click_foursquare(self):
        self.get_foursquare().click()
        print("Click foursquare icon")

    def click_vk(self):
        self.get_vk().click()
        print("Click vk icon")

    def click_telegram(self):
        self.get_telegram().click()
        print("Click telegram icon")

    def click_youtube(self):
        self.get_youtube().click()
        print("Click youtube icon")

    def click_yappy(self):
        self.get_yappy().click()
        print("Click yappy icon")

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

    def logout(self):
        self.move_to_element(self.profile_list_down)
        self.click_logout_option()
        self.assert_url(self.logout_url)

    def check_social_medias(self):
        self.click_foursquare()
        self.assert_url(self.foursquare_link)
        self.click_vk()
        self.assert_url(self.vk_link)
        self.click_telegram()
        self.assert_url(self.telegram_link)
        self.click_youtube()
        self.assert_url(self.youtube_link)
        self.click_yappy()
        self.assert_url(self.yappy_link)