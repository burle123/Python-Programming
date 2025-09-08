mylist=[1,3,4,5,6,7,3]

# squared_list=[]
# for item in mylist:
#     squared_list.append(item**2)

squared_list=[item**2 for item in mylist]  # List comprehension

print(squared_list)    