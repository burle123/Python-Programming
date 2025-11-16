reverse=int(input("Enter a number to reverse: "))
rev=0
while(reverse>0):
    digit=reverse%10 #get last digit
    rev=rev*10+digit #append last digit to reversed number
    reverse=reverse//10 #remove last digit from original number

print("Reversed Number is: ",rev)
