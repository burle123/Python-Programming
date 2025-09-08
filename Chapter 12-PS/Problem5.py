n = int(input("Enter a number: "))

table = [n*i for i in range(1, 11)]
with open(r"C:\Users\sbbra\OneDrive\Desktop\Python\Chapter 12-PS\tables.txt","a") as f:
    f.write(f"Table of {n}: {str(table)} \n")