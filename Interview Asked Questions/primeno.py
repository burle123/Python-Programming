#The no which is divisible no itself or by 1

# start = 2
# end = 20

# for num in range(start, end + 1):
#     if num > 1:
#         for i in range(2, int(num ** 0.5) + 1):
#             if num % i == 0:
#                 break
#         else:
#             print(num, end=" ")



# num=int(input("Enter any Number : "))

# if num>1:
#     for i in range(2,num):
#         if num % i == 0:
#             print("Not a prime number!!!")
#             break
#     else:
#         print("Prime number!!!")        


#Print all prime numbers from 1 to 100


# for i in range(2, 101):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i,end=' ')


#Addition of all prime numbers between 1 to n
n=int(input("Enter any Number : "))
total=0
for i in range(2, n):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        total=total+i
print("Addition of all prime numbers between 1 to n is :",total)