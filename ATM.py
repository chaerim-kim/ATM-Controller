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
        # list of accounts
        self.account_list = defaultdict(list)

    def create_user(self, card_number, pin, acct_type, balance):
        # card number is the unique identifier
        self.account_list[card_number].append({"pin": pin, "accounts": {'account_type': acct_type, 'balance': balance}})

    # if card and pin matches, return user object
    def verify_user(self, card_number, pin):

        match_list = []

        # print(self.account_list[card_number][0]['pin'])
        for i in range(len(self.account_list)):
            if card_number in self.account_list.keys() and pin == self.account_list[card_number][i]['pin']:
                # print(self.account_list[card_number][i]['accounts'])
                match_list.append(self.account_list[card_number][i]['accounts'])

            else:
                # print("Invalid Card or PIN")
                return False

        return match_list


class ATMController:
    def __init__(self, account):
        self.Account = account
        # self.money = money

    # retrieve accounts and pass it onto next
    def select_account(self, acctlist):
        if acctlist != False:
            print( "User verified")
            # if account in acctlist:


            # return self.Account.verify_user(card_number,pin)
        else:
            print( "Invalid Card or PIN")



    # def see_balance(self):
    #     return self.account['balance']
    #
    #
    # def deposit(self, deposit_amt):
    #
    #     if deposit_amt > 0:
    #         self.account['balance'] += deposit_amt
    #
    #     else:
    #         print("Amount must be bigger than zero.")
    #
    #
    # def withdraw(self, withdraw_amt):
    #     if 0 < withdraw_amt <= self.account['balance'] :
    #         self.account['balance'] -= withdraw_amt
    #
    #     else:
    #         print("Withdraw amount exceeds the balance in your account.")


if __name__ == '__main__':
    s = Account()
    # one user mutliple acct
    s.create_user(11112222, 1234, "credit", 10)
    s.create_user(11112222, 1234, "savings", 140)
    s.create_user(29200000, 1234, "credit", 90)
    # print(s.account_list)

    acctlist = s.verify_user(11112222,1234)
    print(acctlist)

    atm = ATMController(s)
    atm.select_account(acctlist)

