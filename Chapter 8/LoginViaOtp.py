# Login Via OTP

import random

OTP=""

def generate_otp():
    global OTP
    # OTP=str(random.randint(10000,99999))
    for i in range(6):
        OTP+=str(random.randint(0,9))
    print("Your OTP is :", OTP)

def verify_otp(user_otp):
    if user_otp==OTP:
        return True
    else:
        return False    
    
def main():
    generate_otp()
    user_otp=input("Enter the OTP sent to your registered mobile number/email: ")
    if verify_otp(user_otp):
        print("Login Successful!!!")
    else:
        print("Invalid OTP. Login Failed.")    
main()