a=(1,2,3,"hello")
print(a)
print(type(a))
a[3]="hi" # This will give error because tuples are immutable
print(a)