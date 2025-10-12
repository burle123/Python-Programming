# Using Set

# a = [1,1,2,3,4,5,3,3]
# b = list(set(a))
# print(b)

# Using Loop

a = ['a','a','b','b','c','z']

unique=[]

for i in range(len(a)):
    duplicate = False
    for j in range(len(unique)):
        if a[i] == unique[j]:
            duplicate =True
            
    if not duplicate:
        unique.append(a[i])

print(unique)



 