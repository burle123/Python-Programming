f = open(r"C:\Users\sbbra\OneDrive\Desktop\Python\Chapter 9-PS\poem.txt","r")
content =f.read()
 
if("twinkle" in content):
    print("The word twinkle is present in the poem")
else:
    print("The word twinkle is not present in the poem")
f.close()