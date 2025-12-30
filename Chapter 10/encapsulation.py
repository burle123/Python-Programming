class Account:
    def __init__(self,balance,account_number):
        self.balance=balance
        self.account_number=account_number

    def debit(self,amount):
        if amount>self.balance:
            print("Insufficient balance")
        else:
            self.balance-=amount
            print(f"Debited {amount}. New balance is {self.balance}")
    def credit(self,amount):
        self.balance+=amount
        print(f"Credited {amount}. New balance is {self.balance}")
    def get_balance(self):
        return self.balance

acc=Account(5000,"1234")
acc.credit(2000)
acc.debit(1000)
print("Current Balance:",acc.get_balance()) # Accessing balance via public method

# Trying to access private attributes will raise an AttributeError
