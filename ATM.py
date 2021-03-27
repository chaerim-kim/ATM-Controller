from collections import defaultdict


# Enter Card number (Insert Card)
# Enter PIN code
# if correct, choose the menu from:
# 1. See balance
# 2. Deposit
# 3. Withdraw
# If not correct, move to 1


# verify the user and assist with the login part
class Account:
    def __init__(self):
        self.account_list = defaultdict(list)

    def create_user(self, card_number, pin, acct_type, balance):
        # card number is the unique identifier
        self.account_list[card_number].append({"pin": pin, "accounts": {'account_type': acct_type, 'balance': balance}})

    # if card and pin matches, return list of accounts associated with that card no.
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
        # self.money = money

    # retrieve accounts and pass it onto next
    def select_account(self, acctlist, chosen_acct):
        if acctlist != False:
            print("User verified")

            # if valid account, return the chosen account
            for i in range(len(acctlist)):
                if chosen_acct == acctlist[i]['account_type']:
                    print(acctlist[i])
                    return acctlist[i]
        else:
            print("Invalid Card or PIN")


    def perform_tasks(self, chosen_acct, action, amount=0):
        if action == "See Balance":
            print(chosen_acct['balance'])
            return chosen_acct['balance']

        elif action == "Deposit":
            if amount > 0:
                chosen_acct['balance'] += amount
                print(chosen_acct['balance'])
            else:
                print("Deposit amount must be bigger than zero")

        elif action == "Withdraw":
            if 0 < amount <= chosen_acct['balance']:
                chosen_acct['balance'] -= amount
                print(chosen_acct['balance'])
            else:
                print("Withdraw amount exceeds the balance in your account")


if __name__ == '__main__':
    bankaccount = Account()
    # one user mutliple acct
    bankaccount.create_user(11112222, 1234, "credit", 10)
    bankaccount.create_user(11112222, 1234, "savings", 140)
    bankaccount.create_user(29200000, 1234, "credit", 90)
    # print(s.account_list)

    acctlist = bankaccount.verify_user(11112222, 1234)
    # print(acctlist)

    # choose account
    atm = ATMController(bankaccount) # feed list of accounts
    chosen_acct = atm.select_account(acctlist, "savings")

    atm.perform_tasks(chosen_acct, "See Balance")
    atm.perform_tasks(chosen_acct, "Deposit", 100)
    atm.perform_tasks(chosen_acct, "Withdraw", 200)

    # print(s.account_list)
