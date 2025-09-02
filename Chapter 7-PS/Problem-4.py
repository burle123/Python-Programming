#No is Prime or Not

n=int(input("Enter any number :"))

for i in range(2,n):
    if(n%i)==0:
        print("Not Prime No")
        break
else:
    print("Prime No")        