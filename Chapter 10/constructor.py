class Employee:
    lang="Python"     # This is a class attribute
    salary =1200000

    def __init__(self,name,salary,lang):      # dunder method which Call itself automatically
        self.name=name
        self.salary=salary
        self.lang=lang
        print("I am creating an obj")

    def greet(self):
        print("Hello, Good Morning!!!")    

    def getInfo(self):
        print(f"Employee Name = {self.name} \nEmployee Fav Lang = {self.lang} \nEmployee Salary = {self.salary}")


sb=Employee("Shantanu",1500000,"Java")
# sb.lang ="JAVASCRIPT"
sb.greet()
sb.getInfo()    
    
# Employee.getInfo(sb)
