s1={1,2,3,4,5,5,5,6,7,8,9}

# Set methods
s1.add(10)  # Adding an element
print(s1)
s1.remove(3)  # Removing an element
print(s1)
s1.discard(9)  # Removing an element (no error if not found)
print(s1)
print(s1.pop())  # Removing and returning an arbitrary element
print(s1)
print(len(s1))  # Getting the number of elements
print(5 in s1)  # Checking membership (returns True or False)

print("*******************************************")

s2={5,6,7,8,9,10,11,12}
print(s1.union(s2))  # Union of two sets
print(s1.intersection(s2))  # Intersection of two sets
print(s1.difference(s2))  # Difference of two sets
print(s1.symmetric_difference(s2))  # Symmetric difference of two sets
s1.clear()  # Clearing the set
print(s1)