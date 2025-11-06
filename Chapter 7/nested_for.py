#print the tables from 2 to 10

# for i in range(1,11):             #ROW
#     for j in range(2,11):         #COLUMN
#         print(f"{j} X {i} = {j*i}",end=" \t")


# for i in range(1,6):
#     for j in range(1,6):
#         if i==3:
#             print(" # ",end=" ")
#         else:

#             print(" * ",end=" ")
#     print("\n")


for i in range(1,6):
    for j in range(1,6):
        if j==5:
            print(" # ",end=" ")
        elif j==2:
            print(" @ ",end=" ")
        elif i==3:
            print(" $ ",end=" ")
        elif i==1:
            print(" * ",end=" ")
        else:
            print(" w ",end=" ")        


    print("\n")   