word = "Donkey"

with  open(r"C:\Users\sbbra\OneDrive\Desktop\Python\Chapter 9-PS\file.txt","r") as f:
    content=f.read()


newContent= content.replace(word,"######")


with  open(r"C:\Users\sbbra\OneDrive\Desktop\Python\Chapter 9-PS\file.txt","w") as f:
    f.write(newContent)