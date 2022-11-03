import pytest
import bank
from dotenv import load_dotenv

class Test:
    @staticmethod
    @pytest.mark.parametrize("customer1, customer2, deposit_amount", [('Ron Weasly', 'Hermoine Granger', 100)])
    def test_first(customer1, customer2, deposit_amount):
        BankHomepage = bank.BankHomepage()
        BankHomepage.go_to_login_page()
        BankHomepage.choose_customer(customer1)
        BankHomepage.choose_customer(customer2)
        BankHomepage.login_as_customer()
        BankHomepage.create_deposit(deposit_amount)
        BankHomepage.check_last_deposit(deposit_amount)
        BankHomepage.logout()
