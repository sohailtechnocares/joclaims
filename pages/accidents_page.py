import datetime
import os
import random
import string
import time
from datetime import datetime
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.waits import wait_for_element_clickable
from utils.helpers import get_current_date



class AccidentsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

        # Locators
        self.accident_button = (By.XPATH, "//span[normalize-space()='Accidents']")
        self.new_accident_button = (By.XPATH, "//i[@class='fas fa-plus text-white scale']")

        self.policy_number = (By.CSS_SELECTOR, "input[name='PolicyNumber']")
        self.claim_no = (By.ID, "Accident_No")
        self.accident_type = (By.XPATH, "//span[normalize-space()='Comprehensive']")
        self.acceipt_confirmmation=(By.XPATH,"//button[normalize-space()='Yes']")
        self.responsibility_at_fault = (By.XPATH, "//span[@class='label-text'][normalize-space()='At Fault']")
        self.price_type = (By.ID, "purchasing")
        self.priority = (By.ID, "lowpriorityCheckbox")
        self.total_loss = (By.ID, "totalLossCheckbox")

        # Claim Circumstances
        self.loss_date = (By.ID, "accident_happend")
        self.select_date=(By.XPATH,"//div[@class='btn-light bg-primary text-white ng-star-inserted']")
        self.loss_time = (By.ID, "accident_happend_time")
        self.police_report_number = (By.ID, "Poilce_Report_Number")
        self.place_of_loss = (By.XPATH, "//ng-select[@id='governorate_place_loss']//input[@role='combobox']")
        self.governorate_place_loss = (By.XPATH,"//ng-select[@id='governorate_place_loss']//input[@role='combobox']")
        self.city_or_village = (By.XPATH, "//ng-select[@id='city_place_loss']//input[@role='combobox']")
        self.select_City=(By.XPATH,"//ng-select[@id='city_place_loss']//input[@role='combobox']")

        # Faulty Policy
        self.faulty_insurance_company = (By.XPATH, "//ng-select[@id='FaultyCompanyID']//input[@role='combobox']")
        self.faulty_insurance_company = (By.ID, "faulty_policy_number")
        self.faulty_plate_no = (By.ID, "faulty_plate_no")
        self.faulty_insurance_company = (By.XPATH, "//ng-select[@id='faulty_make_id']//input[@role='combobox']")
        self.year = (By.XPATH, "//ng-select[@name='year_id'][1]")


        # Loss or Damage of Vehicle
        self.vin_no = (By.ID, "vin_no")
        self.plate_no = (By.ID, "plate_no")
        self.vehicle_owner_name=(By.ID,"VehicleOwner_Name")
        self.owner_phone = (By.ID, "Owner_PhoneNo")
        self.broker_name = (By.ID, "Broker_Name")
        self.surveyor_name = (By.XPATH, "(//input[@role='combobox'])[8]")
        self.servey_date = (By.XPATH, "//input[@id='surveyor_appointment']")

        # self.select_servey_date=(By.XPATH,"//div[contains(text(),'20')]")
        self.select_servey_date = (By.XPATH, "(//button[@type='button'])[8]")
        self.select_current_date=By.XPATH, "(//div[contains(text(),'23')])[1]"
        self.make = (By.XPATH, "(//input[@role='combobox'])[9]")
        self.make_input=(By.XPATH, "(//div[@class='ng-input'])[9]//input[@role='combobox']")
        self.click_model =(By.XPATH,"(//input[@role='combobox'])[10]")
        self.model = (By.XPATH, "(//ng-select[@id='model_id']//div[@class='ng-select-container ng-has-value']//input[@role='combobox']")
        self.year = (By.XPATH, "(//input[@role='combobox'])[11]" )
        self.purchase_date=(By.ID,"purchase_date")
        self.cars_involved = (By.XPATH, "//input[@id='cars_involved']")
        self.purchase_date = (By.ID, "purchase_date")
        self.cars_involved232 = (By.ID, "ICWorkshop_id")

         # Engine Type
        self.engine_type = (By.XPATH, "//input[@id='Hybrid1']")

        # Body Type
        self.cars_body_type = (By.ID, "Sedan1")

        # Car Notes
        self.cars_involved = (By.ID, "Important_Note")

        # Car Accident Pictures
        self.car_accident_pictures = (By.XPATH, "//img[@src='../../../../../../assets/images/input_image.png']")

        self.upload_input=(By.XPATH, "//input[@type='file']")
        # Accident Makers
        self.FR_lamp = (By.ID, "FR lamp0")
        self.RR_door3 = (By.ID, "RR door3")
        self.RR_door3 = (By.ID, "R bumper5")

        # Create button
        self.model = (By.CSS_SELECTOR, "button[type='submit']")
        # AccidentsPage locators

        self.accidents_menu_button = (By.XPATH, "//span[normalize-space()='Accidents']")

        self.new_accident_button = (By.XPATH, "//i[@class='fas fa-plus text-white scale']")

        self.policy_number_input = (By.CSS_SELECTOR, "input[name='PolicyNumber']")
        self.claim_number_input = (By.ID, "Accident_No")

        self.accident_type_option = (By.XPATH, "//span[normalize-space()='Comprehensive']")
        self.confirmation_yes_button = (By.XPATH, "//button[normalize-space()='Yes']")

        self.fault_at_fault_radio = (By.XPATH, "//span[@class='label-text'][normalize-space()='At Fault']")
        self.purchasing_type_checkbox = (By.ID, "purchasing")
        self.low_priority_checkbox = (By.ID, "lowpriorityCheckbox")
        self.total_loss_checkbox = (By.ID, "totalLossCheckbox")

        # Claim Circumstances
        self.loss_date_picker = (By.XPATH,
                                 "//div[@class='col-md-4 col-sm-6 floating-label my-2']//button[@type='button']")
        self.loss_date_option = (By.XPATH, "(//div[@class='btn-light bg-primary text-white ng-star-inserted'])[1]")

        self.loss_time_input = (By.ID, "accident_happend_time")
        self.police_report_input = (By.ID, "Poilce_Report_Number")

        self.governorate_dropdown_input = (By.XPATH,
                                           "//ng-select[@id='governorate_place_loss']//input[@role='combobox']")
        self.city_dropdown_input = (By.XPATH, "//ng-select[@id='city_place_loss']//input[@role='combobox']")

        # Faulty Policy
        self.faulty_company_dropdown_input = (By.XPATH, "//ng-select[@id='faulty_make_id']//input[@role='combobox']")
        self.faulty_policy_number_input = (By.ID, "faulty_policy_number")
        self.faulty_plate_number_input = (By.ID, "faulty_plate_no")

        # Vehicle Details
        self.vin_input = (By.ID, "vin_no")
        self.plate_number_input = (By.ID, "plate_no")
        self.vehicle_owner_name_input = (By.ID, "VehicleOwner_Name")
        self.owner_phone_input = (By.ID, "Owner_PhoneNo")
        self.broker_name_input = (By.ID, "Broker_Name")

        self.surveyor_dropdown_input = (By.XPATH, "(//input[@role='combobox'])[8]")
        self.surveyor_date_field = (By.XPATH, "(//input[@id='surveyor_appointment'])[1]")
        self.surveyor_date_option_button = (By.XPATH, "(//button[@type='button'])[8]")
        self.current_date_option = (By.XPATH, "(//div[contains(text(),'19')])[1]")

        self.make_dropdown_input = (By.XPATH, "(//div[@class='ng-input'])[9]//input[@role='combobox']")
        self.model_dropdown_input = (By.XPATH, "(//input[@role='combobox'])[10]")
        self.year_dropdown_input = (By.XPATH, "(//input[@role='combobox'])[11]")

        self.cars_involved_input = (By.XPATH, "//input[@id='cars_involved']")
        self.purchase_date_input = (By.ID, "purchase_date")
        self.workshop_id_input = (By.ID, "ICWorkshop_id")

        # Engine & Body
        self.engine_type_checkbox = (By.XPATH, "//span[normalize-space()='Hybrid']")
        self.body_type_checkbox = (By.ID, "Sedan1")

        # accident markers locaters

        # Final Actions
        self.submit_button = (By.CSS_SELECTOR, "button[type='submit']")k

    # def wait_for_alert(self, timeout=10):
    #     return WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
    #
    # def accept_alert(self):
    #     alert = self.wait_for_alert()
    #     alert.accept()

    # Actions
    def go_to_accident_page(self):
        self.wait.until(EC.element_to_be_clickable(self.accident_button)).click()


    def click_new_accident_button(self):

        self.wait.until(EC.element_to_be_clickable(self.new_accident_button)).click()

    def enter_policy_number(self,policyNumber):
        self.driver.find_element(*self.policy_number_input).send_keys(policyNumber)

    def enter_claim_number(self,claimNumber):
        sss=self.driver.find_element(*self.claim_number_input)
        sss.click()
        sss.send_keys(claimNumber)

    def select_accident_type(self):
         # self.driver.find_element(*self.accident_type_option).click()
         self.wait.until(EC.element_to_be_clickable(self.accident_type_option)).click()

    def click_loss_date_input(self):
     date_field=self.driver.find_element(*self.loss_date)
     date_field.click()
     date_field.clear()
     date_field.send_keys(get_current_date())

    #
    def click_loss_time_input(self,time):
      elment = self.driver.find_element(*self.loss_time)
      elment.click()
      elment.send_keys(time)

    def click_police_number_input_and_enter_police_number(self, policeReportNumber):
      police_report_number2 = self.driver.find_element(*self.police_report_number)
      police_report_number2.click()
      police_report_number2.send_keys(policeReportNumber)

    # def select_loss_date(self):
    #   self.driver.find_element(*self.select_date).click()

    def click_of_loss_input(self):
      # self.driver.find_element(*self.place_of_loss).click()
      self.wait.until(EC.element_to_be_clickable(self.place_of_loss)).click()

    def click_yes_option_on_confirmation(self):

        # self.driver.find_element(*self.acceipt_confirmmation).click()

         wait_for_element_clickable(self.driver, self.confirmation_yes_button).click()


    def enter_and_select_place(self,Governorate):
        select_governorate=self.driver.find_element(*self.governorate_place_loss)
        select_governorate.click()
        select_governorate.send_keys(Governorate)
        select_governorate.send_keys(Keys.ENTER)

    def enter_and_select_village(self,villagename):
        select_village=self.driver.find_element(*self.select_City)
        select_village.click()
        select_village.send_keys(villagename)
        select_village.send_keys(Keys.ENTER)


    def click_faulty_insurance_company(self):
      # self.driver.find_element(*self.faulty_insurance_company).click()
      self.wait.until(EC.element_to_be_clickable(self.faulty_insurance_company)).click()

    def scroll_modal_form(self):
        # Find the modal form container
       modal_section = self.driver.find_element(By.XPATH, "//section[contains(@class, 'side-form-right')]")

        # Scroll it using JavaScript
       self.driver.execute_script("arguments[0].scrollBy(0, 500);", modal_section)

    import random

    import string

    # def vin_number(self):
    # # Allowed characters for VIN (exclude I, O, Q)
    #     allowed_chars = string.ascii_uppercase.replace('I', '').replace('O', '').replace('Q', '') + string.digits
    def checked_price_type(self):
         self.driver.find_element(*self.responsibility_at_fault).click()
    #
    #     # Generate a 17-character VIN
    #     vin_number = ''.join(random.choices(allowed_chars, k=17))
    #
    #     # Print or use the variable
    #     print("Generated VIN:", str(vin_number))
    #
    #     vin_no_field = self.driver.find_element(*self.vin_no)
    #
    #     vin_no_field.click()
    #     vin_no_field.send_keys(vin_no_field)
    def click_vin_input(self,vinNumber):
         vin_no_field=self.driver.find_element(*self.vin_no)
         vin_no_field.click()
         vin_no_field.send_keys(vinNumber)

    def click_vin_field(self, vinNumber):
        vin_no_field = self.driver.find_element(*self.vin_no)
        vin_no_field.click()
        vin_no_field.send_keys(vinNumber)

    def click_and_enter_Plate_no(self,plateNo):
         vin_no_field=self.driver.find_element(*self.plate_no)
         vin_no_field.click()
         vin_no_field.send_keys(plateNo)

    # def click_vin_field(self,vinNumber):
    #      vin_no_field=self.driver.find_element(*self.vin_no)
    #      vin_no_field.click()
    #      vin_no_field.send_keys(vinNumber)

    def click_and_enter_Onwer_name(self,ownerName):
         vin_no_field=self.driver.find_element(*self.vehicle_owner_name)
         vin_no_field.click()
         vin_no_field.send_keys(ownerName)

    def click_and_enter_Onwer_phone(self,ownerPhone):
         vin_no_field=self.driver.find_element(*self.owner_phone)
         vin_no_field.click()
         vin_no_field.send_keys(ownerPhone)


    def click_and_enter_broker_name(self,brokerName):
         vin_no_field=self.driver.find_element(*self.broker_name)
         vin_no_field.click()
         vin_no_field.send_keys(brokerName)

    def click_and_select_surveyor(self, surveyorName):
        select_surveyor = self.driver.find_element(*self.surveyor_name)
        select_surveyor.click()
        select_surveyor.send_keys(surveyorName)
        select_surveyor.send_keys(Keys.ENTER)

    # def click_and_select_surveyor_name(self,surveyorName):
    #      vin_no_field=self.driver.find_element(*self.surveyor_name)
    #      vin_no_field.click()
    #      vin_no_field.send_keys(surveyorName)

    def only_click(self):
        self.driver.find_element(*self.servey_date).click()

    #
    # def click_and_select_surveyor_date(self):
    #     select_surveyor_date_field = self.driver.find_element(*self.servey_date)
    #     select_surveyor_date_field.click()
    #     # select_surveyor_date_field.clear()
    #     select_surveyor_date_field.send_keys(get_current_date())


    def click_and_select_surveyor_date(self):
     date_field=self.driver.find_element(*self.select_servey_date)
     date_field.click()



    def click_and_select_surveyor_current_date(self):
        date_field = self.driver.find_element(*self.select_current_date)
        date_field.click()

    def click_make_input(self):
      self.driver.find_element(*self.make).click()




    # def click_current_date(self):
    #     self.driver.find_element(*self.select_current_date).click()


    # def click_and_select_surveyor_date_button(self):
    #     select_surveyor_date_button = self.driver.find_element(*self.select_servey_date)
    #     select_surveyor_date_button.click()
        # select_surveyor_date_button.send_keys(Keys.ENTER)

    # def scroll_modal_form(self):
    #     # Find the modal form container
    #    modal_section = self.driver.find_element(By.XPATH, "//section[contains(@class, 'side-form-right')]")
    #
    #     # Scroll it using JavaScript
    #    self.driver.execute_script("arguments[0].scrollBy(0, 600);", modal_section)
    #
    # def click_current_servey_date(self):
    #   self.driver.find_element(*self.select_current_date).click()

    def search_and_select_make(self,make2):
      make=self.driver.find_element(*self.make_input)
      make.click()
      make.send_keys(make2)
      make.send_keys(Keys.ENTER)

    def click_of_village_input(self):
      self.driver.find_element(*self.city_or_village).click()

    def click_and_select_model(self):
        sssmmm=self.driver.find_element(*self.click_model)
        sssmmm.click()
        sssmmm.send_keys(Keys.ENTER)

    def click_and_select_year(self,accidentYear):
       year = self.driver.find_element(*self.year )
       # wait_for_element_clickable(self.driver, self.year).click()

       year.click()
       year.send_keys(accidentYear)
       year.send_keys(Keys.ENTER)

    def click_and_enter_number_of_cars(self,nocars):
      car_involed=self.driver.find_element(*self.cars_involved)
      car_involed.click()
      car_involed.send_keys(nocars)


    def click_purchase_date(self ):
        current_date = datetime.now().strftime("%d/%m/%Y")
        # purchaseDateicon = self.driver.find_element(*self.purchase_date_input)
        purchaseDateicon2=self.wait.until(EC.element_to_be_clickable(self.purchase_date_input))
        purchaseDateicon2.click()
        purchaseDateicon2.clear()
        purchaseDateicon2.send_keys(current_date)


    def checked_engine_type(self):
         # self.driver.find_element(*self.engine_type_checkbox).click()

         self.wait.until(EC.element_to_be_clickable(self.engine_type_checkbox)).click()

      # wait_for_element_clickable(self.driver, self.engine_type_checkbox).click()

    def checked_body_type(self):
         # self.driver.find_element(*self.cars_body_type).click()

         self.wait.until(EC.element_to_be_clickable(self.cars_body_type)).click()


    def click_accident_pictures_icon(self):
         # self.driver.find_element(*self.car_accident_pictures).click()

         self.wait.until(EC.element_to_be_clickable(self.car_accident_pictures)).click()

    def upload_car_picture(self, image_file_name):
        # Absolute path of the image (placed in test_data folder)
        image_path = os.path.abspath(f"test_data/{image_file_name}")
        self.driver.find_element(*self.car_accident_pictures).send_keys(image_path)


    def click_create_button(self):
        self.driver.find_element(*self.submit_button).click()





















