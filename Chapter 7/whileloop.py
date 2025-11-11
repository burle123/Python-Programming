# i=1

# while(i<6):
#     print("SB")
#     i+=1
 

# i=1

# while True:
#     print("SB",i)
#     i+=1
#     if i == 10:
#         break

# i=1
# while i<=50:
#     if i%2==0:
#         print(i)
#     i+=1

# i=1
# while i<=50:
#     if i%2==1:
#         print(i)
#     i+=1

# i=1
# while i<=50:
#     if i%3==0:
#         print(i)
#     i+=1

# i=1
# total=0
# while i<=100:
#     if i%2==0:
#         total=total+i
#     i+=1
# print("Sum of even numbers from 1 to 100 is :",total)
 

i=1
count=0
while i<=100:
    if i%3==0 and i%5==0:
        count+=1
        print(i)
    i+=1
print("Count of numbers divisible by 3 and 5 from 1 to 100 is :",count)

