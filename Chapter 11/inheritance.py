class Employee:
    def __init__(self):
        print("This is Parent Class")

class Programmer(Employee):        #Single Inheritance
    print("This is Child Class")



o = Programmer()    