def my_generator():
    for i in range(5):
        yield i

gen=my_generator()
print(next(gen)) #next() function is used to get the next value from the generator        
print(next(gen))         
print(next(gen))         
print(next(gen))         
         

