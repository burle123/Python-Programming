'''
Enter any number :5
*
**
***
****
*****
'''

n=int(input("Enter any number :"))

for i in range(1,n+1):
    print("*"*i,end="")
     
    print("")



'''
Enter any number :5
*****
****
***
**
*
'''


n=int(input("Enter any number :"))

for i in range(1,n+1):
    print("*"*(n-i+1),end="")
     
    print("")    