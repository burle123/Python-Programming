f = open(r"C:\Users\sbbra\OneDrive\Desktop\Python\Chapter 9\demo_file.txt", "r")
print(f.read())
f.close()
# The same can be written using with statement like this:

with open(r"C:\Users\sbbra\OneDrive\Desktop\Python\Chapter 9\demo_file.txt", "r") as f:
    print(f.read())

# You dont have to explicitly close the file