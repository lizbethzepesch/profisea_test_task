import os
from selectors import Selector

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from datetime import datetime
import time

load_dotenv()


class BankHomepage:
    url = os.getenv('URL')

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver = webdriver.Chrome("chromedriver.exe")
        self.driver.get(os.getenv('URL'))
        self.wait = WebDriverWait(self.driver, 10)

    def go_to_customer_login_page(self):
        self.wait.until(EC.presence_of_element_located(("xpath", Selector.customer_login_button))).click()

    def choose_customer(self, name):
        self.wait.until(EC.presence_of_element_located(("xpath", Selector.user_select)))
        Select(self.driver.find_element("xpath", Selector.user_select)).select_by_visible_text(name)

    def login_as_customer(self):
        self.driver.find_element("xpath", Selector.login_button).click()

    def create_deposit(self, amount):
        self.wait.until(EC.presence_of_element_located(("xpath", Selector.deposit_button))).click()
        self.wait.until(EC.presence_of_element_located(("xpath", Selector.input_field)))
        time.sleep(2)
        self.driver.find_element("xpath", Selector.input_field).send_keys(amount)
        self.driver.find_element("xpath", Selector.submit_button).click()

    def create_withdrawl(self, amount):
        self.wait.until(EC.presence_of_element_located(("xpath", Selector.withdrawl_button))).click()
        self.wait.until(EC.presence_of_element_located(("xpath", Selector.input_field))).send_keys(amount)

        self.driver.find_element("xpath", Selector.submit_button).click()

    def get_success_message(self):
        success_message = self.wait.until(EC.presence_of_element_located(("xpath", Selector.success_message)))
        return success_message.text

    def check_last_deposit(self, amount):
        self.driver.find_element("xpath", Selector.transactions_button).click()

        sort_by_date_transactions = self.wait.until(EC.presence_of_element_located((
            "xpath", Selector.sort_by_date_transactions)))
        sort_by_date_transactions.click()

        assert int(self.wait.until(EC.presence_of_element_located(("xpath", Selector.first_transaction_amount))).text) == amount
        assert self.driver.find_element("xpath", Selector.first_transaction_type).text == 'Credit'

    def logout(self):
        self.driver.find_element("xpath", Selector.logout_button).click()

    def go_to_manager_login(self):
        self.wait.until(EC.presence_of_element_located(("xpath", Selector.manager_login_button))).click()

    def go_to_add_customer_tab(self):
        self.wait.until(EC.presence_of_element_located(("xpath", Selector.add_customer_button))).click()

    def add_customer(self, customer_name, customer_lastname, postal_code):
        self.wait.until(EC.presence_of_element_located(("xpath", Selector.name_customer_field)))
        self.driver.find_element("xpath", Selector.name_customer_field).send_keys(customer_name)

        self.wait.until(EC.presence_of_element_located(("xpath", Selector.lastname_customer_field)))
        self.driver.find_element("xpath", Selector.lastname_customer_field).send_keys(customer_lastname)

        self.wait.until(EC.presence_of_element_located(("xpath", Selector.postal_code_field)))
        self.driver.find_element("xpath", Selector.postal_code_field).send_keys(postal_code)

        self.wait.until(EC.presence_of_element_located(("xpath", Selector.submit_button))).click()

        self.wait.until(EC.alert_is_present())
        self.driver.switch_to.alert.accept()

    def show_customers_list(self):
        self.wait.until(EC.presence_of_element_located(("xpath", Selector.customers_list_button))).click()

    def check_if_new_customer_in_list(self, customer_name, customer_lastname, postal_code):
        self.wait.until(EC.presence_of_element_located(("xpath", Selector.search_customer_input)))
        self.driver.find_element("xpath", Selector.search_customer_input).\
            send_keys(customer_lastname)

        self.wait.until(EC.presence_of_element_located(("xpath", Selector.customers_table_name)))
        assert self.wait.until(EC.presence_of_element_located(("xpath", Selector.customers_table_name))).text == customer_name
        assert self.wait.until(EC.presence_of_element_located(("xpath", Selector.customers_table_last_name))).text == customer_lastname
        assert int(self.wait.until(EC.presence_of_element_located(("xpath", Selector.customers_table_postal_code))).text) == postal_code

    def go_to_new_account_page(self):
        self.wait.until(EC.presence_of_element_located(("xpath", Selector.open_account_button))).click()

    def create_new_account(self, customer, currency):
        self.wait.until(EC.presence_of_element_located(("xpath", Selector.user_select)))
        Select(self.driver.find_element("xpath", Selector.user_select)).select_by_visible_text(customer)

        self.wait.until(EC.presence_of_element_located(("xpath", Selector.currency_select)))
        Select(self.driver.find_element("xpath", Selector.currency_select)).select_by_visible_text(currency)

        self.wait.until(EC.presence_of_element_located(("xpath", Selector.submit_button))).click()

        self.wait.until(EC.alert_is_present())
        self.driver.switch_to.alert.accept()

    def go_home(self):
        self.wait.until(EC.presence_of_element_located(("xpath", Selector.home_button))).click()

    def check_account_presence(self, currency):
        self.wait.until(EC.presence_of_element_located(("xpath", Selector.account_bar)))
        print(self.driver.find_element("xpath", Selector.account_bar).text)
        assert currency in self.driver.find_element("xpath", Selector.account_bar).text
