import unittest
from unittest import TestCase
from ATM import Account, ATMController


class TestAccount(TestCase):
    acct = Account()

    def test_create_user(self):
        self.fail()

    def test_verify_user(self):
        acct.verify_user(1111222233334444, 6789, 1000, "savings")



class TestATMController(TestCase):
    def test_select_account(self):
        self.fail()

    def test_see_balance(self):
        self.fail()

    def test_deposit(self):
        self.fail()

    def test_withdraw(self):
        self.fail()





if __name__ == '__main__':
    unittest.main()