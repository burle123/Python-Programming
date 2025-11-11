# def get_num():
#     return 100,200,300
# # print("Returned Value is :",get_num())
#          #OR
# num=get_num()
# print("Returned Value is :",num)



# def get_data():
#     return 100,"SB",300.5,True
# print("Returned Value is :",get_data())

def get_name():
    
    return "Shantanu"
    return "Sahil"      #This will never execute as the function exits after first return statement because of which second return is unreachable.


name=get_name()
print("Returned Name is :",name)