import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.auth_class import Auth


@pytest.mark.run(order=1)
def test_fail_auth_email(set_up):
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-sertificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.page_load_strategy = 'eager'
    g = Service()
    driver = webdriver.Chrome(options=options, service=g)

    fail_login_email = Auth(driver)
    fail_login_email.fail_email()

    driver.quit()


@pytest.mark.run(order=2)
def test_fail_auth_password(set_up):
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-sertificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.page_load_strategy = 'eager'
    g = Service()
    driver = webdriver.Chrome(options=options, service=g)

    fail_login_password = Auth(driver)
    fail_login_password.fail_password()

    driver.quit()


def test_logout_process(set_up):
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-sertificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.page_load_strategy = 'eager'
    g = Service()
    driver = webdriver.Chrome(options=options, service=g)

    logout_process = Auth(driver)
    logout_process.auth_on_site()
    logout_process.logout()
def test_check_social_media():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-sertificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.page_load_strategy = 'eager'
    g = Service()
    driver = webdriver.Chrome(options=options, service=g)

    check_social_media = Auth(driver)
    check_social_media.enter_without_auth()
    check_social_media.check_social_medias()

    driver.quit()

