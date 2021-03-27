from collections import defaultdict


class Account:
    def __init__(self):
        self.account_list = defaultdict(list)

    # Save card number as a key & allow for multiple accounts under one card
    def create_account(self, card_number, pin, acct_type, balance):
        self.account_list[card_number].append(
            {"pin": pin, "accounts": {'account_type': acct_type, 'balance': balance}})

    # Verify the user and find accounts linked to that card and return a list of account
    def verify_account(self, card_number, pin):
        match_account_list = []

        for i in range(len(self.account_list)):
            if card_number in self.account_list.keys() and pin == self.account_list[card_number][i]['pin']:
                match_account_list.append(
                    self.account_list[card_number][i]['accounts'])
            else:
                return False
        return match_account_list


class ATMController:
    def __init__(self, account):
        self.Account = account

    # Simulate inserting a card and validating user
    def insert_card(self, card_number, pin):
        linked_account = self.Account.verify_account(card_number, pin)
        if linked_account:
            return linked_account
        else:
            return "Invalid Card or PIN"

    # Retrieve accounts for the card and return user selected account
    def select_account(self, linked_account, chosen_account):
        for i in range(len(linked_account)):
            if chosen_account == linked_account[i]['account_type']:
                return linked_account[i]
            else:
                return "Account does not exist"

    def perform_tasks(self, chosen_account, action, amount=0):
        if action == "See Balance":
            return chosen_account['balance']

        elif action == "Deposit":
            if amount > 0:
                chosen_account['balance'] += amount
                return chosen_account['balance']
            else:
                return "Deposit amount must be bigger than zero"

        elif action == "Withdraw":
            if 0 < amount <= chosen_account['balance']:
                chosen_account['balance'] -= amount
                return chosen_account['balance']

            elif amount <= 0:
                return "Withdraw amount must be bigger than zero"

            else:
                return "Withdraw amount exceeds the balance in your account"
