#if-else ladder
num = int(input("Enter a number: "))
if num >= 18:
    print("You can vote")  
elif num == 0:
    print("You entered zero")
else:
    print("You cannot vote")