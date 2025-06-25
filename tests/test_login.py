import time
from pages.login_page import LoginPage

def test_login_with_valid_credentials(driver):
    login_page = LoginPage(driver)
    login_page.open("https://bhdemo.joclaims.com/")
   # Replace with actual URL
    login_page.signin()
    time.sleep(1)
    login_page.login("abdul@bahrain.com","123456")
    time.sleep(5)


    # assert "Invalid username or password" in login_page.get_error_message()



