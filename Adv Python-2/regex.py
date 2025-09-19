import re

s="My fav fruits are mango, banana, orange, apple, pineapple"
res=re.findall(r'\b\w*a\b',s)
print(res)  # [' banana' ]