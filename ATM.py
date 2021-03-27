from collections import defaultdict


# Enter Card number (Insert Card)
# Enter PIN code
# if correct, select the account.
# Then choose the menu from:
# 1. See balance
# 2. Deposit
# 3. Withdraw


# verify the user and assist with the login part
class Account:
    def __init__(self):
        self.account_list = defaultdict(list)

    def create_user(self, card_number, pin, acct_type, balance):
        # card number is the unique identifier
        self.account_list[card_number].append({"pin": pin, "accounts": {'account_type': acct_type, 'balance': balance}})
        return True


    # Verify the user and find accounts linked to that card and return them
    def verify_user(self, card_number, pin):
        match_list = []

        for i in range(len(self.account_list)):
            if card_number in self.account_list.keys() and pin == self.account_list[card_number][i]['pin']:
                match_list.append(self.account_list[card_number][i]['accounts'])

            else:
                return False
        return match_list


class ATMController:
    def __init__(self, account):
        self.Account = account

    def insert_card(self, card_number, pin):
        linked_account = self.Account.verify_user(card_number, pin)
        if linked_account != False:
            print("Account verified")
            return linked_account
        else:
            print("Invalid Card or PIN")

    # retrieve accounts and return selected account to next function
    def select_account(self, linked_account, chosen_acct):
        # if valid account, return the chosen account
        for i in range(len(linked_account)):
            if chosen_acct == linked_account[i]['account_type']:
                print(linked_account[i])
                return linked_account[i]

    def perform_tasks(self, chosen_acct, action, amount=0):
        if action == "See Balance":
            print(chosen_acct['balance'])
            return chosen_acct['balance']

        elif action == "Deposit":
            if amount > 0:
                chosen_acct['balance'] += amount
                print(chosen_acct['balance'])
            else:
                raise RuntimeError("Deposit amount must be bigger than zero")

        elif action == "Withdraw":
            if 0 < amount <= chosen_acct['balance']:
                chosen_acct['balance'] -= amount
                print(chosen_acct['balance'])
            else:
                raise RuntimeError("Withdraw amount exceeds the balance in your account")


if __name__ == '__main__':
    test_account = Account()

    # one user mutliple acct
    test_account.create_user(11112222, 1234, "credit", 100)
    test_account.create_user(11112222, 1234, "savings", 1400)
    test_account.create_user(29200000, 1111, "credit", 2500)
    # print(s.account_list)

    # choose account
    atm = ATMController(test_account) # feed list of accounts
    # insert card method will return a list of accounts
    linked_account = atm.insert_card(11112222,1234)
    chosen_acct = atm.select_account(linked_account, "credit")

    # perform task
    atm.perform_tasks(chosen_acct, "See Balance")
    atm.perform_tasks(chosen_acct, "Deposit", 100)
    atm.perform_tasks(chosen_acct, "Withdraw", 200)

    # print(s.account_list)
