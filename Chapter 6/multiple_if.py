#Multiple if statements
num = int(input("Enter a number: "))
if num >= 18:
    print("You can vote")   
if num == 0:
    print("You entered zero")
if num < 18 and num != 0:
    print("You cannot vote")    
    