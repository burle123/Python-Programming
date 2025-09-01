a=int(input("Enter no 1 :"))
b=int(input("Enter no 2 :"))
c=int(input("Enter no 3 :"))
d=int(input("Enter no 4 :"))

if(a>b and a>c and a>d):
    print("Greatest no is a",a)
elif(b>a and b>c and b>d):
    print("Greatest no is b",b)
elif(c>a and c>b and c>d):
    print("Greatest no is c",c)
elif(d>a and d>b and d>c):
    print("Greatest no is d",d)