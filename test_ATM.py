import unittest
from ATM import Account, ATMController


class TestAccount(unittest.TestCase):
    def setUp(self):
        self.test_account = Account()
        self.test_account.create_account(11112222, 1234, "credit", 100)
        self.test_account.create_account(11112222, 1234, "savings", 20000)
        self.test_account.create_account(33334444, 9999, "savings", 1400)

    def test_verify_account(self):
        # Test with correct pin and account
        valid_user = self.test_account.verify_account(11112222, 1234)
        self.assertEqual(valid_user,
                         [{'account_type': 'credit', 'balance': 100}, {'account_type': 'savings', 'balance': 20000}])

        # Test wrong pin
        invalid_user = self.test_account.verify_account(33334444, 0000)
        self.assertFalse(invalid_user)

        # Test account that doesnt exist
        nonexistent_user = self.test_account.verify_account(88889999, 0000)
        self.assertFalse(nonexistent_user)


class TestATMController(unittest.TestCase):
    def setUp(self):
        self.test_account = Account()
        self.test_account.create_account(11112222, 1234, "credit", 100)
        self.test_account.create_account(11112222, 1234, "savings", 20000)
        self.test_account.create_account(33334444, 9999, "savings", 1400)

        self.test_ATM = ATMController(self.test_account)

    def test_insert_card(self):
        # Test wrong pin
        wrong_pin = self.test_ATM.insert_card(11112222, 8888)
        self.assertEqual(wrong_pin, "Invalid Card or PIN")

        # Test if it retrieves all accounts
        valid_pin = self.test_ATM.insert_card(11112222, 1234)
        self.assertEqual(valid_pin,
                         [{'account_type': 'credit', 'balance': 100}, {'account_type': 'savings', 'balance': 20000}])

    def test_select_account(self):
        selected_account = self.test_ATM.select_account(
            [{'account_type': 'credit', 'balance': 100}, {'account_type': 'savings', 'balance': 20000}], "credit")
        self.assertEqual(selected_account, {
                         'account_type': 'credit', 'balance': 100})

        # Test account that doesnt exist
        nonexistent_account = self.test_ATM.select_account(
            [{'account_type': 'credit', 'balance': 100}, {'account_type': 'savings', 'balance': 20000}], "boop")
        self.assertEqual(nonexistent_account, "Account does not exist")

    def test_perform_tasks(self):
        # prints correct balance
        correct_balance = self.test_ATM.perform_tasks(
            {'account_type': 'credit', 'balance': 100}, "See Balance")
        self.assertEqual(correct_balance, 100)

        # Test valid deposit
        valid_deposit = self.test_ATM.perform_tasks(
            {'account_type': 'credit', 'balance': 100}, "Deposit", 100)
        self.assertEqual(valid_deposit, 200)

        # Test negative deposit
        invalid_deposit = self.test_ATM.perform_tasks(
            {'account_type': 'credit', 'balance': 100}, "Deposit", -1000)
        self.assertEqual(
            invalid_deposit, "Deposit amount must be bigger than zero")

        # Test valid withdraw
        valid_withdraw = self.test_ATM.perform_tasks(
            {'account_type': 'credit', 'balance': 100}, "Withdraw", 40)
        self.assertEqual(valid_withdraw, 60)

        # Test excessive withdraw - banned
        invalid_withdraw = self.test_ATM.perform_tasks(
            {'account_type': 'credit', 'balance': 100}, "Withdraw", 20000)
        self.assertEqual(invalid_withdraw,
                         "Withdraw amount exceeds the balance in your account")

        # Test withdraw amount = 0
        zero_withdraw = self.test_ATM.perform_tasks(
            {'account_type': 'credit', 'balance': 100}, "Withdraw", 0)
        self.assertEqual(
            zero_withdraw, "Withdraw amount must be bigger than zero")


if __name__ == '__main__':
    unittest.main()
