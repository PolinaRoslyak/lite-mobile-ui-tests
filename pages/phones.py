from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from base.base_class import Base


class Phones(Base):

    # Locators
    brand_apple = "/html/body/main/div[3]/div/div/div/div/div[1]/div[1]/a"
    check_apple = "/html/body/main/div[2]/div/div/div[1]/h1"
    assertion_apple_text = "Apple iPhone"
    iphone = "//img[@src='https://lite-mobile.ru/image/cache/catalog/import_files/78" \
             "/789582312a7f11ec837d00155d851b26_789582362a7f11ec837d00155d851b26-228x228.jpg']"
    iphone13 = "/html/body/main/div[3]/div/div/div/div/div[1]/div[1]/a"
    quick_view_apple = "//a[@data-id='193080']"
    cart_button_quick_view = "//*[@id='quick-view']/div/div/div[2]/div[3]/a"
    title_quick_view = "//*[@id='quick-view']/div/div/div[2]/div[2]"
    price_quick_view = "//*[@id='quick-view']/div/div/div[2]/div[3]/div/div"
    brand_samsung = "/html/body/main/div[3]/div/div/div/div/div[1]/div[12]/a"
    check_samsung = "/html/body/main/div[2]/div/div/div[1]/h1"
    assertion_samsung_text = "Смартфоны Samsung"
    price_filter_desc = "/html/body/main/div[3]/div/div/div/div/div[2]/div[2]/div/div[1]/div[1]/div[3]/label[2]/span"
    menu_bar = "/html/body/main/div[3]/div/div/div/div/div[2]/div[2]/div/div[1]/div[1]/div[3]"
    iphone13_menu_bar = "/html/body/main/div[3]/div/div[2]/div[2]/div/div[1]"
    slider_lower = "//div[@class='noUi-handle noUi-handle-lower']"
    slider_upper = "//div[@class='noUi-handle noUi-handle-upper']"
    assertion_text_sliders = "/html/body/main/div[2]/div/div/div[1]/h1"
    left_price = "//*[@id='ocfilter']/div[2]/div[2]/div/div[1]/div/span[2]"
    right_price = "//*[@id='ocfilter']/div[2]/div[2]/div/div[1]/div/span[4]"
    show_button = "#popover993471 > div.popover-content > button"
    checkout_button = "//*[@id='cart-popup']/div/div[4]/a/span[2]"

    # Getters
    def get_apple(self):
        return WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable((By.XPATH, self.brand_apple)))

    def get_check_apple(self):
        return WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable((By.XPATH, self.check_apple)))

    def get_samsung(self):
        return WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable((By.XPATH, self.brand_samsung)))

    def get_check_samsung(self):
        return WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable((By.XPATH, self.check_samsung)))

    def get_price_filter(self):
        return WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable((By.XPATH, self.price_filter_desc)))

    def get_quick_view_apple(self):
        return WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable((By.XPATH, self.quick_view_apple)))

    def get_quick_view_title(self):
        return WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, self.title_quick_view)))

    def get_quick_view_price(self):
        return WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, self.price_quick_view)))

    def get_cart_button_quick_view(self):
        return WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, self.cart_button_quick_view)))

    def get_iphone13(self):
        return WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, self.iphone13)))

    def get_checkout(self):
        return WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable((By.XPATH, self.checkout_button)))

    # Actions
    def click_apple(self):
        self.get_apple().click()
        self.assert_word(self.get_check_apple(), self.assertion_apple_text)
        print("Click apple button")

    def click_samsung(self):
        self.get_samsung().click()
        self.assert_word(self.get_check_samsung(), self.assertion_samsung_text)
        print("Click samsung button")

    def click_price_filter(self):
        self.get_price_filter().click()
        print("Click price filter")

    def move_slider_lower(self, x, y):
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(self.driver.find_element(By.XPATH, self.slider_lower), x, y).perform()
        print("move left slider")

    def move_slider_upper(self, x, y):
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(self.driver.find_element(By.XPATH, self.slider_upper), x, y).perform()
        print("move right slider")

    def move_to_iphone(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH, self.iphone)).perform()

    def check_quick_view(self):
        assert self.quick_view_apple not in self.driver.page_source
        print("quick view not found")

    def click_quick_view_apple(self):
        self.get_quick_view_apple().click()
        print("click quick view apple")

    def return_title_and_price_quick_view(self):
        text_quick_view_title = self.get_quick_view_title().text
        text_quick_view_price = self.get_quick_view_price().text
        return text_quick_view_title, text_quick_view_price

    def click_cart_button_quick_view(self):
        self.get_cart_button_quick_view().click()
        print("click cart button")

    def click_iphone13(self):
        self.get_iphone13().click()
        print("click iphone 13")

    def click_checkout_button(self):
        self.get_checkout().click()
        print("click Checkout")

    # Methods
    def buy_iphone_with_quick_view(self):
        self.get_current_url()
        self.click_apple()
        self.click_iphone13()
        self.scroll_from_elm(self.iphone13_menu_bar, 0, 450)
        self.check_quick_view()
        self.move_to_iphone()
        self.click_quick_view_apple()
        self.return_title_and_price_quick_view()
        self.click_cart_button_quick_view()
        self.click_checkout_button()
