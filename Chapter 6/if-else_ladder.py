# #if-else ladder
# num = int(input("Enter a number: "))
# if num >= 18:
#     print("You can vote")  
# elif num == 0:
#     print("You entered zero")
# else:
#     print("You cannot vote")


# student addmission based on marks

age= int(input("Enter your age : "))

if age>=18:
    print("you are eligible for addmission")

    marks= int(input("Enter your marks : "))
    if marks>=90:
         print("You are eligible for Science stream")
    elif marks>=80:
        print("You are eligible for Commerce stream")
    elif marks>=70:
        print("You are eligible for Arts stream")   
    else:
        print("You are not eligible for any stream")

else:
    print("You are not eligible for addmission")        