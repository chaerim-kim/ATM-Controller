
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
        self.account_list = {}

    def create_user(self, card_number, pin, acct_type, balance):
        # card number is the unique identifier
        self.account_list[card_number] = {"pin": pin, "accounts": {'account_type': acct_type, 'balance': balance}}


    # if card and pin matches, return user object
    def verify_user(self, card_number, pin):
        # return self.account_list[card_number]['accounts'] to the customer once the pin verifies

        # self.account_list[card_number]['pin'] -> password
        # but this only returns one sksdksfjkdsfj
        for key, value in self.account_list.items():
            if card_number == key and pin == value['pin']:
                return True
                # return self.account_list[card_number]['accounts']

            else:
                return False


class ATMController:
    def __init__(self, account):
        self.Account = account
        # self.money = money


    # retrieve accounts and pass it onto next
    def select_account(self, card_number, pin):
        if self.Account.verify_user(card_number,pin) == True:
            print( "User verified")
            return self.Account.verify_user(card_number,pin)
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
    s.create_user(11112222, 1234, "savings", 140)
    s.create_user(11112222, 1234, "credit", 10)
    # s.create_user(29200000, 1234, "credit", 90)

    # print(s.account_list)
    # print(s.verify_user(11112222,1234))

    atm = ATMController(s)
    atm.insert_and_verify(11112222,1234)

