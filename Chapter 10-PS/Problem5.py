import random

class ticket:
    def __init__(self,trainNo):
        self.trainNo=trainNo

    def book(self,fro,to):
        print(f"Ticket is booked in train no {self.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Train no: {self.trainNo} is running on time") 

    def getFare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {random.randint(222, 5555)}")  


t = ticket(12399)
t.book("Pune", "Mumbai")
t.getStatus()
t.getFare("Pune", "Mumbai")    
 