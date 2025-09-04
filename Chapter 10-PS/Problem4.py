class calc:
    def __init__(self,n):
        self.n= n


    def square(self):
        print (f"Square of n = {self.n*self.n}")   
    def cube(self):
        print (f"Cube of n = {self.n*self.n*self.n}")   
    def squareroot(self):
        print (f"SquareRoot of n = {self.n**1/2}")  
    def greet(self):
        print("Hello there")    




a=calc(10)
a.greet()
a.square()
a.cube()
a.squareroot()
        
