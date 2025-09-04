class Employee:
    language="Python"     # This is a class attribute
    Salary =1200000

    def greet(self):
        print("Hello, Good Morning!!!")    

    def getInfo(self):
        print(f"Employee Fav Lang = {self.language} and \nEmployee Salary = {self.Salary}")


sb=Employee()
sb.language="JAVASCRIPT"
sb.greet()
sb.getInfo()    
    
# Employee.getInfo(sb)
