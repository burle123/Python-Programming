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

def login():
    username=input("Enter your username : ")
    password=input("Enter your password : ")
    if username=="admin" and password=="1234":
        print("Login Successful!!!")
    else:
        print("Login Failed")
login()