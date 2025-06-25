from selenium import webdriver
print("First Print Setup")

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://bhdemo.joclaims.com/")