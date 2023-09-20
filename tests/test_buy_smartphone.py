import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.auth_class import Auth
from pages.cartpage import CartPage
from pages.mainpage import MainPage
from pages.phones import Phones
from pages.itemcard import ItemCard


@pytest.mark.run(order=2)
def test_buy_smartphone(set_up):
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-sertificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.page_load_strategy = 'eager'
    g = Service()
    driver = webdriver.Chrome(options=options, service=g)

    login = Auth(driver)
    login.auth_on_site()

    choose_phones = MainPage(driver)
    choose_phones.open_phones()

    buy_phone = Phones(driver)
    buy_phone.buy_iphone_with_quick_view()

    checkout = CartPage(driver)
    checkout.fill_checkout_form_with_auth()

    driver.quit()


@pytest.mark.run(order=1)
def test_find_specific_smartphone(set_up):
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-sertificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.page_load_strategy = 'eager'
    g = Service()
    driver = webdriver.Chrome(options=options, service=g)

    login = Auth(driver)
    login.enter_without_auth()

    choose_phones = MainPage(driver)
    choose_phones.find_iphone13()

    buy_phone = ItemCard(driver)
    list_for_comparison_item_card = buy_phone.check_item()
    buy_phone.buy_item()

    checkout = CartPage(driver)
    list_for_comparison_checkout = checkout.check_item_and_price()
    checkout.fill_checkout_form_without_auth()

    assert list_for_comparison_checkout == list_for_comparison_item_card
    print("Item and price is ok")

    driver.quit()
