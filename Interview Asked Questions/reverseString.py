# string = "Hello World"
# rev_str=string[::-1]
# print(rev_str)


str = "Hello World"
rev_str = ""
for i in str:
    rev_str = i + rev_str
print(rev_str)