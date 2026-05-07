# def greeting():
#     print("Hello! Good Morning")
# greeting()


# def avg():
#     a=int(input("Enter num for a :"))
#     b=int(input("Enter num for b :"))
#     c=int(input("Enter num for c :"))
#     average=(a+b+c)/3
#     print("Average = ",average)

# avg()    
# avg()    
# avg()    


# def Addition():
#     a=int(input("Enter num for a :"))
#     b=int(input("Enter num for b :"))
#     c=a+b
#     print("Addition = ",c)  
# Addition()


# def add(a,b):
#     print(a+b)
# result = add(4,6)
# print(result)  # None - because there is no return statement in add fn, so it returns None by default




#Duplicate fn

# def my_fun(name,age): #parameters
#     print(f"Hello {name}, you are {age} years old.")
# my_fun("SB", 21) #arguments
# my_fun("Datta", 22)


#Complex fn

# def fetch_data():
#     print("Fetching data from database...")
# def process_data():
#     print("Processing data...")
# def display_data():
#     print("Displaying data...")
#     print("Report generated successfully!")
# def main():
#     fetch_data()
#     process_data()
#     display_data()
# main()

#Readability

# def cal_bill(cups,price_per_cup):
#     return cups * price_per_cup   

# my_bill = cal_bill(3,15)     # If return is there then we should always have to store the func call in seperate variable
# print(my_bill)


#Scopes

# def serve_chai():
#     chai_type = "Masala"  #Local Scope

#     print(f"Inside Function: {chai_type}")

# chai_type = "Lemon"
# serve_chai()
# print(f"Outside Function: {chai_type}")


# def chai_counter():
#     chai_order = "Lemon" #Enclosing Scope

#     def print_order():
#         chai_order = "Ginger" #Inner Scope
#         print("Inner :" , chai_order)
#     print_order()
#     print("Outer:" ,chai_order)

# chai_order = "Tulsi" # Global Scope
# chai_counter()
# print("Global: ",chai_order)        


#Non-Local

# Use global when you need to change a variable defined outside all functions.
# Use nonlocal when you need to change a variable from an outer function inside a nested function.

# def update_order():
#     chai_type = "Elaichi"
#     print("Before kitchen update" ,chai_type)

#     def Kitchen():
#         nonlocal chai_type      #nonlocal - inside to inside fn
#         chai_type = "Kesar"

#     Kitchen()
#     print("After kitchen update ", chai_type)    
# update_order()

#Global

# x = 10  # Global variable

# def modify_global():
#     global x  # Refers to the global x
#     x = 20    # Modifies the global variable

# modify_global()
# print(x)  # Output: 20

# def login():
#     username=input("Enter your username : ")
#     password=input("Enter your password : ")
#     if username=="admin" and password=="1234":
#         print("Login Successful!!!")
#     else:
#         print("Login Failed")
# login()

# def login(username, password):
#     if username=="admin" and password=="1234":
#         return True
#     else:
#         return False

# def main():
#     user=input("Enter your username : ")
#     pwd=input("Enter your password : ")
#     if login(user, pwd):
#         print("Login Successful!!!")
#     else:
#         print("Login Failed")
# main()      