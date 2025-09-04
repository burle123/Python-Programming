words=["Donkey","bad","ganda"]

with  open(r"C:\Users\sbbra\OneDrive\Desktop\Python\Chapter 9-PS\file.txt","r") as f:
    content=f.read()

for word in words:

    content= content.replace(word,"#"*len(word))


with  open(r"C:\Users\sbbra\OneDrive\Desktop\Python\Chapter 9-PS\file.txt","w") as f:
    f.write(content)