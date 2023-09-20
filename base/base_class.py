import datetime
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By


class Base:

    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        get_url = self.driver.current_url
        print(get_url)

    def assert_word(self, word, result):
        assert word.text == result
        print("assertion is ok")

    def screenshot(self):
        now_date = str(datetime.datetime.now())
        name_screenshot = "screen" + now_date + ".png"
        self.driver.save_screenshot("/PycharmProjects/dns/screens/"+name_screenshot)
        print("Screenshot is done")

    def assert_url(self, result):
        assert self.driver.current_url == result
        print("Correct url")

    def scroll_from_elm(self, elm, pix1, pix2):
        iframe = self.driver.find_element(By.XPATH, elm)
        scroll_origin = ScrollOrigin.from_element(iframe)
        ActionChains(self.driver) \
            .scroll_from_origin(scroll_origin, pix1, pix2) \
            .perform()
        time.sleep(1)

    def move_to_page(self, handle):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[handle])

    def save_text_for_comparison(self, get_xpath):
        saved_text = get_xpath.text
        return saved_text


