from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.signin_button = (By.CSS_SELECTOR, ".btn.dark-btn.px-4.mbl-px-2.mx-2.cursor-point.d-none.d-lg-block")
        self.username_input = (By.CSS_SELECTOR, "input[name='email']")
        self.password_input = (By.CSS_SELECTOR, "input[name='pass']")
        self.login_button = (By.CSS_SELECTOR, "button[type='submit']")

    def open(self, url):
        self.driver.get(url)

    def signin(self):
        self.driver.find_element(*self.signin_button).click()

    def login(self, username,password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def method1(self):
        print("this is a sohail")

    def method2(self):
        print("this is a sohail")
    #
    # def is_logged_in(self):
    #     # Example: check if logout button or dashboard is visible
    #     return "Dashboard" in self.driver.page_source
