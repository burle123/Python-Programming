number = int(input("Enter a number: "))

sum=0
while number > 0:
    rem = number % 10
    sum = sum + rem
    number = number // 10

print("Sum of digits is: ", sum)