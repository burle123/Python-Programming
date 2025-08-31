a=(1,2,3,"hello",4.5,True)
print(a)
print(type(a))
# tuples are immutable - they cannot be changed
# a[1]=20  # this will give an error

# tuple methods
print(a.count(2))  # count the number of occurrences of 2
print(a.index("hello"))  # find the index of the first occurrence of "hello"
print(len(a))  # length of the tuple
# tuples can be nested
b=(1,2,(3,4),5)
print(b)
print(b[2])
print(b[2][1]) # access the second element of the nested tuple

d=(1,2,(3,4),5,(5,4,3))
print(d)
print(d[4])
print(d[4][1]) # access the second element of the nested tuple

# tuples can be concatenated
c=a+b
print(c)
print(len(c))

# tuples can be sliced
d=c[2:5]
print(d)
print(type(d))
# tuples can be unpacked
(x,y,z,word,num,boolean)=a
print(x)
print(word)