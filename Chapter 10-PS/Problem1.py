class programmer:
    company="Microsoft"

    def __init__(self,name,salary,lang):
        self.name=name
        self.salary=salary
        self.lang=lang


sb=programmer("Shantanu",1200000,"Python")        
print(sb.name,sb.lang,sb.salary,sb.company)
rb=programmer("Rohan",1200000,"Java")      
print(rb.name,rb.lang,rb.salary,rb.company)  
        