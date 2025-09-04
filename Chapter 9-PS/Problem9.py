
with open(r"C:\Users\sbbra\OneDrive\Desktop\Python\Chapter 9-PS\this.txt","r") as f:
    content1=f.read()
  

with open(r"C:\Users\sbbra\OneDrive\Desktop\Python\Chapter 9-PS\this_copy.txt","r") as f:
    content2 = f.read()

if(content1 == content2):
    print("Yes these files are identical")  #identical - same

else: 
    print("No these files are not identical")