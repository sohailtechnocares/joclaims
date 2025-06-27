import time

import pytest

from pages.login_page import LoginPage
from pages.accidents_page import AccidentsPage
from utils.generators import DataGenerator, generate_vin_number


@pytest.mark.smoke
def test_login_with_valid_credentials(driver):
    vin ="1HGCM82633A123456"
    plateNumber="AEO-3344"
    vehicleOwnerName="MUhammad Sohail"
    OwnerPhone="03434343433"
    brokerName="Sohail Sagar"
    cars_involved="2"

    serveyorName="Adnan  Thabit 1501 2500"
    login_page = LoginPage(driver)
    login_page.open("https://bhdemo.joclaims.com/")
   # Replace with actual URL
    login_page.signin()
    time.sleep(1)
    login_page.login("abdul@bahrain.com","123456")
    time.sleep(5)

# def test_accident(driver):
    # Step 2: Now go to Accidents Page
    accident_page = AccidentsPage(driver)
    time.sleep(2)
    accident_page.go_to_accident_page()
    time.sleep(2)
    accident_page.click_new_accident_button()
    time.sleep(2)

    accident_page.enter_policy_number("1234")
    accident_page.enter_claim_number("FSS-232")
    radio_button=accident_page.select_accident_type()
    # if not radio_button.is_selected():
    #     radio_button.click()

    accident_page.click_yes_option_on_confirmation()
    accident_page.checked_price_type()
    time.sleep(2)
    accident_page.click_loss_date_input()
    time.sleep(2)
    # accident_page.select_loss_date()
    # time.sleep(2)
    accident_page.click_loss_time_input("06:45:AM")
    time.sleep(1)
    random_value = DataGenerator.generate_random_5_digit()
    accident_page.click_police_number_input_and_enter_police_number(random_value)
    time.sleep(1)

    accident_page.click_of_loss_input()
    time.sleep(1)

    accident_page.enter_and_select_place("Capital")
    time.sleep(1)

    accident_page.click_of_village_input()
    time.sleep(1)
    accident_page.enter_and_select_village("Manama")

    time.sleep(2)
    accident_page.scroll_modal_form()
    time.sleep(2)

    # Loss or Damage of Vehicle
    vin_number = generate_vin_number("DEF")
    print("Generated VIN:", vin_number)
    accident_page.click_vin_field(vin_number)
    # Enter vin number
    accident_page.click_vin_input(vin)
    accident_page.click_and_enter_Plate_no(plateNumber)
    accident_page.click_and_enter_Onwer_name(vehicleOwnerName)
    accident_page.click_and_enter_Onwer_phone(OwnerPhone)
    accident_page.click_and_enter_broker_name(brokerName)
    time.sleep(2)
    accident_page.click_and_select_surveyor(serveyorName)
    time.sleep(2)
    accident_page.scroll_modal_form()
    time.sleep(2)
    accident_page.only_click()
    time.sleep(2)
    accident_page.click_and_select_surveyor_date()
    time.sleep(2)
    accident_page.click_and_select_surveyor_current_date()
    time.sleep(1)
    # accident_page.click_current_date()
    # accident_page.click_and_select_surveyor_date_button()
    # time.sleep(2)
    # accident_page.click_current_servey_date()
    # time.sleep(2)
    accident_page.click_make_input()
    time.sleep(2)
    accident_page.search_and_select_make("Cars")
    time.sleep(2)
    accident_page.click_and_select_model()
    time.sleep(2)

    accident_page.click_and_select_year("2025")
    time.sleep(2)
    accident_page.click_purchase_date()
    time.sleep(2)
    # accident_page.click_purchase_date_icon()
    time.sleep(2)

    # accident_page.click_and_enter_number_of_cars(cars_involved)

    time.sleep(2)
    accident_page.checked_engine_type()
    time.sleep(2)
    accident_page.checked_body_type()
    time.sleep(2)
    # accident_page.click_accident_pictures_icon()

    accident_page.scroll_modal_form()
    time.sleep(2)
    accident_page.scroll_modal_form()
    time.sleep(2)
    #
    # image_path = r"C:\Users\123\Desktop\car.jpg"
    #
    # accident_page.upload_car_picture(image_path)
    accident_page.click_create_button()
    time.sleep(10)




