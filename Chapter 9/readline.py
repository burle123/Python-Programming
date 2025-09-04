f = open(r"C:\Users\sbbra\OneDrive\Desktop\Python\Chapter 9\demo_file.txt","r")
# data=f.readline()
# print(data)

line=f.readline()
while(line!=""):
    print(line)
    line=f.readline()
f.close()