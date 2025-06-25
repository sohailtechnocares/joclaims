import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    options = Options()
    options.add_experimental_option("prefs", {
        "profile.default_content_setting_values.notifications": 1  # Allow notifications
    })
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
# if you want to run testcase without open brower this uncomment below code
# conftest.py
# import pytest
# from selenium import webdriver
#
# @pytest.fixture(scope="function")
# def driver():
#     options = webdriver.ChromeOptions()
#     options.add_argument("--headless")  # ✅ Run in headless mode
#     options.add_argument("--disable-gpu")
#     options.add_argument("--window-size=1920,1080")
#     driver = webdriver.Chrome(options=options)
#     yield driver
#     driver.quit()
