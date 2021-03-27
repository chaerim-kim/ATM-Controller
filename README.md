# ATM-Controller
💰A controller that mimics and manipulates the ATM - an ATM Controller!


## 🎨 Features / 주요 기능
- User inserts a card and enters the PIN, which ATM then verifies.
- Once the account is verified, the user can select an account to perform tasks on.
- Users can:
  - [x] See balance
  - [x] Deposit
  - [x] Withdraw

<br/>

## ⛓ Classes
### Account Class
- A class that holds account information, represented by a list of dictionaries.
- It holds `card_number, pin, acct_type, balance` information.
```
{
  11112222: [{'pin': 1234, 'accounts': {'account_type': 'credit', 'balance': 100}},
            {'pin': 1234, 'accounts': {'account_type': 'savings', 'balance': 20000}}],
  33334444: [{'pin': 9999, 'accounts': {'account_type': 'savings', 'balance': 1400}}]
}
```
  - Two account types, 'credit' and 'savings' is associated with card number '11112222'.


The class have the following member functions:
- _**create_account()**_: Save card number as a key & pin, account type, balance information as a nested dictionary.
- _**verify_account()**_: Verify the user and return the accounts linked to the card

<br/>

### ATMController Class
- This class takes the account instance from **Account class** and performs ATM tasks.

The class have the following member functions:
- _**insert_card**_: Simulate inserting a card and validating user
- _**select_account**_: Retrieve accounts for the card and return user-selected account
- _**perform_tasks**_: Performs ATM functionalities of:
    - See Balance
    - Withdraw
    - Deposit

<br/>

## ⚒ Installation / 실행 방법
**Mac OSX and Windows**: Python 3.6+ required

### 1. Cloning the project
To clone the project directory, run:

```git clone https://github.com/chaerim-kim/ATM-Controller.git```


### 2. Running the ATM controller
However, this **won't return anything** as it does not have a user interface. Based on this code, one should be able to implement the user interface!

```python3 ATM.py```


### 3. Running tests
Instead, run the test file to provoke and test the ATM controller.

```python3 test_ATM.py -v```

<br/>

## ➰ Project Duration / 프로젝트 기간
March 2021
