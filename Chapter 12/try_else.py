try:
    a=int(input("Enter a number :"))
    print("You entered :",a)

except ValueError as e:  # Catching specific exception
    print(e)


else:              # This block runs if no exceptions occur in the try block
    print("No exceptions occurred. You entered a valid integer.")        