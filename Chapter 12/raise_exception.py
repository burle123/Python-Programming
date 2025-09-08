a=int (input("Enter number a :"))
b=int (input("Enter number b :"))

if b==0:
    raise ZeroDivisionError("Denominator cannot be zero!")
else:
    print("Result :",a/b) 