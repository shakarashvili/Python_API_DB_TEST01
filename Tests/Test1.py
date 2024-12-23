import unittest
import time
from telnetlib import EC

from urllib3.util import wait

from Data.Data1 import Data1

class Test1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Initialize the Data1 class
        cls.data = Data1()

    def test_home_page_title(self):
        """Test the home page title"""
        expected_title = "Automation Exercise"
        actual_title = self.data.get_home_page_title()
        self.assertEqual(expected_title, actual_title, "Home page title does not match!")

    def test_click_contact_us(self):
        """Test clicking on 'Contact us' button"""
        self.data.click_contact_us()
        self.assertIn("Contact", self.data.driver.title, "Failed to navigate to Contact Us page")

    def test_click_login(self):
        """Test clicking on 'Signup / Login' button"""
        self.data.click_login()
        self.assertIn("Login", self.data.driver.title, "Failed to navigate to Signup/Login page")

    def test_Register_user(self):
       self.data.click_login()
       # Verify that the 'New User Signup!' text is displayed
       self.assertEqual("New User Signup!", self.data.get_new_user_sign_up().text, "New User Signup! - Failed to navigate")
       #შევიყვანოთ მონაცემები
       self.data.send_user_name_action(self.data.word_George)
       self.data.send_email_action(self.data.word_mail_Shaqarashvili25)
       assert  self.data.get_sing_up_button_element().is_displayed()
       self.data.click_sing_up_button()
       # რეგისტრაციის ვრცელ გვერდზე დავიწყოთ მონაცემების შეყვანა
       self.assertEqual("ENTER ACCOUNT INFORMATION", self.data.get_Enter_Account_Information_title().text,"Enter Account Information - Failed to navigate ")

       self.data.select_Title_Enter_Account_page_action()
       self.data.send_name_Enter_Account_page_action(self.data.word_George)
       #self.data.send_email_Enter_Account_page_action(self.data.word_mail_Shaqarashvili25)
       self.data.send_password_Enter_Account_page_action(self.data.word_password)
       self.data.select_days_Enter_Account_page_action()
       self.data.select_months_Enter_Account_page_action()
       self.data.select_years_Enter_Account_page_action()
       self.data.select_newsletter_Enter_Account_page_action()
       self.data.select_special_offer_Enter_Account_page_action()
       self.data.select_first_name_Address_Information_action(self.data.word_George)
       self.data.select_last_name_Address_Information_action(self.data.word_shakarshvili)
       self.data.select_company_Address_Information_action(self.data.word_company)
       self.data.select_address1_Address_Information_action(self.data.word_address1)
       self.data.select_address2_Address_Information_action(self.data.word_address2)
       self.data.select_country_dropdown_Address_Information_action()
       self.data.select_state_Address_Information_action(self.data.word_state)
       self.data.select_city_Address_Information_action(self.data.word_city)
       self.data.select_zipCode_Address_Information_action(self.data.zipCode)
       self.data.select_mobile_numer_input_Address_Information(self.data.mobileNumber)
       self.data.click_create_account_button_Address_Information_action()
       self.data.click_Account_Created_action()
       assert self.data.click_delete_account_action().is_displayed()
       self.data.click_delete_account_action()
       self.data.alert_dismiss()
       self.data.account_deleted_message_text_action()


       time.sleep(1)


    @classmethod
    def tearDownClass(cls):
        # Close the browser after all tests
        cls.data.close_browser()
