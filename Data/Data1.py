from pydoc import describe
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib3.util import wait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

class Data1:
    def __init__(self):
        # Initialize the driver
        self.driver = webdriver.Chrome(service=webdriver.chrome.service.Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://www.automationexercise.com/")

    # Elements
    def get_home_page_title(self):
        return self.driver.title


    def get_contact_us_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, "a[href='/contact_us']")

    def get_login_button(self):
        return self.driver.find_element(By.LINK_TEXT, "Signup / Login")

    def get_new_user_sign_up(self):
         return self.driver.find_element(By.XPATH, "//*[text()='New User Signup!']")

    def get_user_name_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input[data-qa='signup-name']")
    def get_email_element(self):
        return self.driver.find_element(By.XPATH, "//input[@data-qa='signup-email']")
    def get_sing_up_button_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, "button[data-qa='signup-button']")
    def get_Enter_Account_Information_title(self):
        return self.driver.find_element(By.XPATH, "//b[text()='Enter Account Information']")


    def get_Title_MR_Enter_Account_page_element(self):
       return self.driver.find_element(By.XPATH, "//label[@for='id_gender1' ]")
    def get_Name_Enter_Account_page_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input[data-qa='name']")
    def get_email_Enter_Account_page_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input[data-qa='email']")
    def get_password_Enter_Account_page_element(self):
        return self.driver.find_element(By.ID, "password")
    def get_days_Enter_Account_page_element(self):
        return  self.driver.find_element(By.ID, "days")
    def get_days_25_Enter_Account_page_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, "select[data-qa='days'] option[value='25']")
    def get_months_Enter_Account_page_element(self):
        return  self.driver.find_element(By.CSS_SELECTOR, "select[data-qa='months']")
    def get_months_June_Enter_Account_page_element(self):
        return  self.driver.find_element(By.CSS_SELECTOR, "select[data-qa='months'] option[value='6']")
    def get_years_Enter_Account_page_element(self):
        return  self.driver.find_element(By.ID, "years")
    def get_years_1995_Enter_Account_page_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, "select[data-qa='years'] option[value='1995']")


    def get_newsletter_Enter_Account_page_element(self):
        return self.driver.find_element(By.CSS_SELECTOR,"input[type='checkbox'][name='newsletter'][id='newsletter'][value='1']")
    def get_special_offers_Enter_Account_page_element(self):
       return  self.driver.find_element(By.ID, "optin")

    def get_first_name_Address_Information_element(self):
        return  self.driver.find_element(By.ID, "first_name")
    def get_last_name_Address_Information_element(self):
        return  self.driver.find_element(By.ID, "last_name")
    def get_company_Address_Information_element(self):
        return  self.driver.find_element(By.ID, "company")
    def get_address1_Address_Information_element(self):
        return  self.driver.find_element(By.ID, "address1")
    def get_address2_Address_Information_element(self):
        return  self.driver.find_element(By.ID, "address2")
    def get_country_dropdown_Address_Information_element(self):
        return  self.driver.find_element(By.ID, "country")

    def get_country_dropdown_Canada_Address_Information_element(self):
        return self.driver.find_element(By.XPATH, "//option[. = 'Canada']")
    def get_state_Address_Information_element(self):
        return self.driver.find_element(By.XPATH,"/html/body/section/div/div/div/div[1]/form/p[7]/input")
    def get_city_Address_Information_element(self):
        return self.driver.find_element(By.XPATH,"/html/body/section/div/div/div/div[1]/form/p[8]/input")
    def get_zipcode_Address_Information_element(self):
        return self.driver.find_element(By.ID, "zipcode")
    def get_mobile_numer_input_Address_Information_element(self):
        return self.driver.find_element(By.ID, "mobile_number")
    def get_create_account_button_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, "button[data-qa='create-account']")
    def get_create_account_button_Address_Information_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, "button[data-qa='create-account']")
    def get_Account_Created_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, "a[data-qa='continue-button']")
    def get_delete_account_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, "a[href='/delete_account']")
    def get_account_deleted_message_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, "h2.title.text-center[data-qa='account-deleted']")


    # continue_button = driver.find_element(By.CSS_SELECTOR, "a[data-qa='continue-button']")
#delete_account_link = driver.find_element(By.CSS_SELECTOR, "a[href='/delete_account']")
    # account_deleted_message = driver.find_element(By.CSS_SELECTOR, "h2.title.text-center[data-qa='account-deleted']")


    #Words
    word_George = "George"
    word_mail_Shaqarashvili25 = "shaqarashvili255@gmail.com"
    word_password = "12341234"
    word_full_name = "George Shakarashvili"
    word_shakarshvili = "Shakarashvili"
    word_company = "Liberty Bank"
    word_address1 = "Tbilisi chavchavadze"
    word_address2 = "street number 37N"
    word_state = "kartli"
    word_city = "Tbilisi"
    zipCode = "0193"
    mobileNumber = "571090909"

    # Actions
    def click_contact_us(self):
        self.get_contact_us_button().click()

    def click_login(self):
        self.get_login_button().click()
    def send_user_name_action(self, name ):
        self.get_user_name_element().send_keys(name)
    def send_email_action(self, email):
        self.get_email_element().send_keys(email)
    def click_sing_up_button(self):
        self.get_sing_up_button_element().click()

    def select_Title_Enter_Account_page_action(self):
        self.get_Title_MR_Enter_Account_page_element().click()
        self.get_Title_MR_Enter_Account_page_element().is_selected()

    def send_name_Enter_Account_page_action(self, name):
        self.get_Name_Enter_Account_page_element().clear()
        self.get_Name_Enter_Account_page_element().send_keys(name)


    def send_email_Enter_Account_page_action(self, email):
        self.get_email_Enter_Account_page_element().send_keys(email)

    def send_password_Enter_Account_page_action(self,password):
        self.get_password_Enter_Account_page_element().send_keys(password)

    def select_days_Enter_Account_page_action(self):
        self.get_days_Enter_Account_page_element().click()
        self.get_days_25_Enter_Account_page_element().click()
        self.get_days_25_Enter_Account_page_element().is_selected()
    def select_months_Enter_Account_page_action(self):
        self.get_months_Enter_Account_page_element().click()
        self.get_months_June_Enter_Account_page_element().click()
        self.get_months_June_Enter_Account_page_element().is_selected()
    def select_years_Enter_Account_page_action(self):
        self.get_years_Enter_Account_page_element().click()
        self.get_years_1995_Enter_Account_page_element().click()
        self.get_years_1995_Enter_Account_page_element().is_selected()

    def select_newsletter_Enter_Account_page_action(self):
        self.get_newsletter_Enter_Account_page_element().click()

    def select_special_offer_Enter_Account_page_action(self):
        self.get_special_offers_Enter_Account_page_element().click()
    def select_first_name_Address_Information_action(self, first_name):
        self.get_first_name_Address_Information_element().send_keys(first_name)
    def select_last_name_Address_Information_action(self, last_name):
        self.get_last_name_Address_Information_element().send_keys(last_name)

    def select_company_Address_Information_action(self, company):
        self.get_company_Address_Information_element().send_keys(company)
    def select_address1_Address_Information_action(self, address1):
        self.get_address1_Address_Information_element().send_keys(address1)
    def select_address2_Address_Information_action(self, address2):
        self.get_address2_Address_Information_element().send_keys(address2)
    def select_country_dropdown_Address_Information_action(self):
        self.get_country_dropdown_Address_Information_element().click()

        self.get_country_dropdown_Canada_Address_Information_element().click()
        self.get_country_dropdown_Canada_Address_Information_element().is_selected()
        self.get_country_dropdown_Address_Information_element().click()

    def select_state_Address_Information_action(self,state):
        self.get_state_Address_Information_element().send_keys(state)
    def select_city_Address_Information_action(self,city):
        self.get_city_Address_Information_element().send_keys(city)
    def select_zipCode_Address_Information_action(self,zipCode):
        self.get_zipcode_Address_Information_element().send_keys(zipCode)
    def select_mobile_numer_input_Address_Information(self,mobile_number):
        self.get_mobile_numer_input_Address_Information_element().send_keys(mobile_number)
    def click_create_account_button_Address_Information_action(self):
        self.get_create_account_button_Address_Information_element().click()

    def click_Account_Created_action(self):
        self.get_Account_Created_element().click()
    def click_delete_account_action(self):
        self.get_delete_account_element().click()
    def account_deleted_message_text_action(self):
        self.get_account_deleted_message_element().is_displayed()
    def alert_dismiss(self):
        alert = self.driver.switch_to.alert

        # Accept the alert
        alert.dismiss()






#def get_country_dropdown_Address_Information_element(self):
 #   return self.driver.find_element(By.ID, "country")


#def get_country_dropdown_Canada_Address_Information_element(self):
 #   return self.driver.find_element(By.CSS_SELECTOR, "select[data-qa='country'] option[value='Canada']")


def close_browser(self):
        self.driver.quit()
