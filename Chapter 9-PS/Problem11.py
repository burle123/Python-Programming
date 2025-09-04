with open(r"C:\Users\sbbra\OneDrive\Desktop\Python\Chapter 9-PS\old.txt","r") as f:
    content=f.read()


with open(r"C:\Users\sbbra\OneDrive\Desktop\Python\Chapter 9-PS\rename_by_py.txt","w") as f:
     f.write(content)    