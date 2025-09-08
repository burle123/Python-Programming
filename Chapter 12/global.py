a=10

def global_test():
    # global a
    global a
    a=5
    print("Inside function a =",a)
global_test()
print("Outside function a =",a)
