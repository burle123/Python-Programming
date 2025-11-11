# def goodday(name):
#     print("Good Day," +name)

# goodday("Shantanu")    
# goodday("Sahil")    
# goodday("Yash")    
# goodday("Datta")    


# def add(a,b):
#     c=a+b
#     print(c)

# add(4,6)    

def prime(n):
    for i in range(2,n):
        if n%i==0:
            print("Not a Prime Number")
            break
        else:
            print("Prime Number")  
            break  
prime(82)            