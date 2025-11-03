# banking application
username = "Shantanu"
pin = "1234"  # PIN should be treated as a string for input comparison

input_username = input("Enter your username: ")
input_pin = input("Enter your password: ")

if input_username == username and input_pin == pin:
    print("Welcome to the Bank")
    print("1. Check Balance 2. Deposit Amount 3. Withdraw Amount 4. Exit")
    balance = 100000

    while True:
        
            choice = int(input("Enter your choice: "))

            if choice == 1:
                print(f"Your balance is {balance}")
            elif choice == 2:
                deposit = int(input("Enter amount to deposit: "))
                if deposit > 0:
                    balance += deposit
                    print(f"Your new balance is {balance}")
                else:
                    print("Invalid deposit amount")
            elif choice == 3:
                withdraw = int(input("Enter amount to withdraw: "))
                if withdraw > 0 and withdraw <= balance:
                    balance -= withdraw
                    print(f"Your new balance is {balance}")
                else:
                    print("Invalid withdraw amount or insufficient balance")
            elif choice == 4:
                print("Thank you for using the bank. Goodbye!")
                break
            else:
                print("Invalid choice")
         
else:
    print("Invalid username or password")

