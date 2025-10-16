# Given a number n, find the value of n raised to the power of its own reverse.

n=int(input("Enter a number: "))
rev=int(str(n)[::-1])
result = n**rev

print(result)

 