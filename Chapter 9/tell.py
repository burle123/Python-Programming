with open(r"C:\Users\sbbra\OneDrive\Desktop\Python\Chapter 9\demo_file.txt","r") as f:
   
    data = f.read()
    curr_pos = f.tell()
    

print(curr_pos)    