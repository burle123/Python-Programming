with open(r"C:\Users\sbbra\OneDrive\Desktop\Python\Chapter 9\demo_file.txt","w") as f:
    f.write("Hello World!!! This is a demo file for truncate method")
    f.truncate(15)


with open(r"C:\Users\sbbra\OneDrive\Desktop\Python\Chapter 9\demo_file.txt","r") as f:  
    data = f.read()
    print(data)  