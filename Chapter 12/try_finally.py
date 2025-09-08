try:
    a=int(input("Enter a number :"))
    print("You entered :",a)

except ValueError as e:  # Catching specific exception
    print(e)

finally:           # This block always runs, regardless of exceptions
    print("Execution completed.")