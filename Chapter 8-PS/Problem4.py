'''
sum(1) = 1
sum(2) = 1 + 2
sum(3) = 1 + 2 + 3
sum(4) = 1 + 2 + 3 + 4
sum(5) = 1 + 2 + 3 + 4 + 5

sum(n) = 1 + 2 + 3 + 4.... n -1 + n
sum(n) = sum(n-1) + n
'''
def sum(n):
    if(n==1):
        return 1
    return(n-1)+n

print(sum(10))

def fact(n):
    if(n==0 or n==1):
        return 1
    return n*fact(n-1)

print(fact(5))