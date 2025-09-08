from functools import reduce 
l= [12, 65, 54, 39, 102, 339, 221, 50, 70, 30]

def greater(a,b):
    if  a>b:
        return a
    else:
        return b
    
print(reduce(greater,l))

