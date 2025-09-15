with open(r"C:\Users\sbbra\OneDrive\Desktop\Python\Chapter 9\demo_file.txt","r") as f:
    f.seek(10)
    data = f.read(8)
print(data)