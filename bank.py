import os

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime
import time

load_dotenv()


class BankHomepage:
    url = os.getenv('URL')

    customer_login_button = '//button[contains(text(), "Customer")]'
    user_select = '//select[@id="userSelect"]'
    login_button = '//button[contains(text(), "Login")]'
    logout_button = '//button[@class="btn logout"]'

    transactions_button = '//button[@ng-class="btnClass1"]'
    deposit_button = '//button[@ng-class="btnClass2"]'
    withdrawl_button = '//button[@ng-class="btnClass3"]'
    success_message = '//span[@class="error ng-binding"]'

    submit_button = '//button[@type="submit"]'
    input_field = '//div[@class="form-group"]/input'

    first_transaction_amount = '//tbody/tr[1]/td[2]'
    first_transaction_type = '//tbody/tr[1]/td[3]'
    sort_by_date_transactions = '//a[contains(text(), "Date-Time")]'


    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver = webdriver.Chrome("chromedriver.exe")
        self.driver.get(os.getenv('URL'))
        self.wait = WebDriverWait(self.driver, 10)

    def go_to_login_page(self):
        self.wait.until(EC.presence_of_element_located(("xpath", self.customer_login_button))).click()

    def choose_customer(self, name):
        self.wait.until(EC.presence_of_element_located(("xpath", self.user_select)))
        Select(self.driver.find_element("xpath", self.user_select)).select_by_visible_text(name)

    def login_as_customer(self):
        self.driver.find_element("xpath", self.login_button).click()

    def create_deposit(self, amount):
        self.wait.until(EC.presence_of_element_located(("xpath", self.deposit_button))).click()
        self.wait.until(EC.presence_of_element_located(("xpath", self.input_field)))
        time.sleep(2)
        self.driver.find_element("xpath", self.input_field).send_keys(amount)
        self.driver.find_element("xpath", self.submit_button).click()

    def create_withdrawl(self, amount):
        self.wait.until(EC.presence_of_element_located(("xpath", self.withdrawl_button))).click()
        withdrawl_field = self.wait.until(EC.presence_of_element_located(("xpath", self.input_field)))
        withdrawl_field.send_keys(amount)

        self.driver.find_element("xpath", self.submit_button).click()

    def get_success_message(self):
        success_message = self.wait.until(EC.presence_of_element_located(("xpath", self.success_message)))
        return success_message.text

    def check_last_deposit(self, amount):
        self.driver.find_element("xpath", self.transactions_button).click()

        sort_by_date_transactions = self.wait.until(EC.presence_of_element_located((
            "xpath", self.sort_by_date_transactions)))
        sort_by_date_transactions.click()

        assert int(self.wait.until(EC.presence_of_element_located(("xpath", self.first_transaction_amount))).text) == amount
        assert self.driver.find_element("xpath", self.first_transaction_type).text == 'Credit'

    def logout(self):
        self.driver.find_element("xpath", self.logout_button).click()
