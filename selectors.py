class Selector:
    manager_login_button = '//button[contains(text(), "Manager")]'
    add_customer_button = '//button[contains(text(), "Add Customer")]'
    open_account_button = '//button[contains(text(), "Open Account")]'
    customers_list_button = '//button[contains(text(), "Customers")]'
    home_button = '//button[contains(text(), "Home")]'

    name_customer_field = '//input[@placeholder="First Name"]'
    lastname_customer_field = '//input[@placeholder="Last Name"]'
    postal_code_field = '//input[@placeholder="Post Code"]'

    search_customer_input = '//input[@placeholder="Search Customer"]'
    customers_table_name = '//tbody//td[1]'
    customers_table_last_name = '//tbody//td[2]'
    customers_table_postal_code = '//tbody//td[3]'

    account_bar = '//div[@ng-hide="noAccount"]/strong[3]'

    customer_login_button = '//button[contains(text(), "Customer")]'
    user_select = '//select[@id="userSelect"]'
    currency_select = '//select[@id="currency"]'
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