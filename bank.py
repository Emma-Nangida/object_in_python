#  2. Create 3 files in the classes directory car.py, fruit.py, and bank.py. Define the following classes in each module respectively. 
# Car
# Fruit
# Account
# Each class should have one class attribute and three instance variables.

# Discuss in your group and come up with the attributes and three 
#methods (behaviours) for each class and implement them

# hence do the following in the interpreter 
# Create two instances of each class.
# Call each of the methods you defined.

class Account:
    num_accounts = 0
   
    def __init__(self, account_number, balance, owner):
        self.account_number = account_number
        self.balance = balance
        self.owner = owner
       
        Account.num_accounts += 1
       
    def deposit(self, amount):
        self.balance += amount
       
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds.")
           
    def get_account_number(self):
        return self.account_number
   
    def get_balance(self):
        return self.balance
   
    def get_owner(self):
        return self.owner