def divisible5(num):
    if num%5==0:
        return True
    else:
        return False
    
a= [12, 65, 54, 39, 102, 339, 221, 50, 70, 30]
f=filter(divisible5,a)
print(list(f))