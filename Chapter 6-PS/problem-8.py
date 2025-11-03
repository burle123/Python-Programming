# Problem 8: College Admission Eligibility and Fee Structure


age= int(input("Enter your age : "))

if age>=18 and age<=25:
    print("you are eligible for addmission")

    marks= int(input("Enter your marks : "))
    if marks>=90:
         print("You are eligible for addmissionn")
    elif marks<=90 and marks>=70:
        print("You need to pay 2 lakh for addmission")
    elif marks<=70 and marks>=50:
        print("You need to pay 5 lakh for addmission")   
    elif marks<50 and marks>=35:  
        print("You need to pay 7 lakh for addmission")
    else:
        print("You are not eligible for addmission")
else:
    print("You are not eligible for addmission because of age")