import time

import pytest
import bank

class Test:
    @staticmethod
    @pytest.mark.parametrize("customer1, customer2, deposit_amount", [('Ron Weasly', 'Hermoine Granger', 100)])
    def test_case_first(customer1, customer2, deposit_amount):
        BankHomepage = bank.BankHomepage()
        BankHomepage.go_to_login_page()
        BankHomepage.choose_customer(customer1)
        BankHomepage.choose_customer(customer2)
        BankHomepage.login_as_customer()
        BankHomepage.create_deposit(deposit_amount)
        BankHomepage.check_last_deposit(deposit_amount)
        BankHomepage.logout()

    @staticmethod
    @pytest.mark.parametrize("customer, amount", [('Harry Potter', 100)])
    def test_case_second(customer, amount):
        BankHomepage = bank.BankHomepage()
        BankHomepage.go_to_login_page()
        BankHomepage.choose_customer(customer)
        BankHomepage.login_as_customer()
        BankHomepage.create_withdrawl(amount)
        assert 'Transaction Failed' in BankHomepage.get_success_message()
        BankHomepage.create_deposit(amount)
        BankHomepage.check_last_deposit(amount)
        BankHomepage.logout()


