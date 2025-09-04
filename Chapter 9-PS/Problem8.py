with open(r"C:\Users\sbbra\OneDrive\Desktop\Python\Chapter 9-PS\this.txt","r") as f:
    content=f.read()
 

with open(r"C:\Users\sbbra\OneDrive\Desktop\Python\Chapter 9-PS\this_copy.txt","w") as f:
    f.write(content)