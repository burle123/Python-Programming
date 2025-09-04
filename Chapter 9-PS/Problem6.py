with  open(r"C:\Users\sbbra\OneDrive\Desktop\Python\Chapter 9-PS\file.txt","r") as f:
    content=f.read()

if("python" in content):
    print("Yes python is present")
else:
    print("No Python is not present")