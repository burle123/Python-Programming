class Employee:
    language="Python"     # This is a class attribute
    Salary =1200000


sb=Employee()
sb.name="Shantanu"          # This is a instance attribute
print(sb.name,sb.language,sb.Salary)    

rb=Employee()
rb.name="Rohan"
print(rb.name,rb.language,rb.Salary)  


# Here name is instance attribute and salary and language are class attributes as they directly belong to the class