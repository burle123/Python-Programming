# for i in range(1,5):
#     print(i)


# for i in range(1,101):
#     if i%3==0 and i%5==0:
#         print(f"{i} is divisible by 3 and 5")
    
# sum=0
# for i in range(1,101):
#     if i%3==0 and i%5==0:
#         sum+=i
# print(sum)

num=int(input("Enter a number: "))
if num<=0:
    print("Enter positive no")
else:
   
    for i in range(1,11):
        print(f"{num} x {i} = {num*i}")