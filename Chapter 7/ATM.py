# ATM Application

#I want to check pin  max 3 times
#After 3 wrong attempts , card is blocked

pin=int(input("Enter your 4 digit PIN : "))
attempts=0
balance=10000
while attempts<3:
    if pin == 1234:
        print("PIN is correct , You can access your account")
        while True:
            print("""
1. Check Balance 
2. Withdraw Money
3. Deposit Money
4. Exit
            """ )
            choice=int(input("Enter your choice : "))
            if choice == 1:
                print(f"Your current balance is : {balance}")
            elif choice == 2:
                amount=int(input("Enter amount to withdraw : "))
                if amount>0:

                    if amount>balance:
                        print("Insufficient Balance")
                    else:
                        balance-=amount
                        print(f"Please collect your cash. Your new balance is {balance}")
                else:
                    print("Invalid amount")
            elif choice == 3:
                amount=int(input("Enter amount to deposit : "))
                if amount<=0:
                    print("Invalid amount")
                else:
                    balance+=amount
                    print(f"Amount deposited successfully. Your new balance is {balance}")

            elif choice == 4:
                print("Thank you for using our ATM. Goodbye!")
                break

        break 
    else:
        print("Wrong PIN , Try again")
        attempts+=1
        pin=int(input("Enter your 4 digit PIN : "))
    if attempts==3:
        print("Your card is blocked , Please contact your bank")
        break

