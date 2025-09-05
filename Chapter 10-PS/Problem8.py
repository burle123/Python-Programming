class Account:
    def __init__(self,bal,accno):
        self.bal=bal
        self.accno=accno

    def debit(self,amount):
        self.bal-=amount    
        print(f"Rs {amount} was debited ")
        print(f"Total balance = {self.getbalance()}")
        
    def credit(self,amount):
        self.bal+=amount    
        print(f"Rs {amount} was credited ")
        print(f"Total balance = {self.getbalance()}")

    def getbalance(self):
        print("Balance Amount = ",self.bal)    

a1=Account(1000,1234)


a1.getbalance()     
a1.debit(500)
a1.credit(100)
   