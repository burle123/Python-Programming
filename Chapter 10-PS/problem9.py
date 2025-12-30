#Create student class that takesname and marks of three sub as argument in constructor.
#Then create a method to print avg marks 

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("Hello, ",self.name,"Your avg score is",sum/3)    

s1=Student("Shantanu",[78,97,65])
s1.get_avg()        