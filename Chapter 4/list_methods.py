demolist=[1,2,3,4,5,10]
print(demolist)
demolist.append(6) # add 6 to the end of the list
print(demolist)
demolist.sort()     # sort the list
print(demolist)
demolist.reverse()  # reverse the list  
print(demolist)
demolist.insert(2,2.5) # at index 2, insert 2.5
print(demolist)
demolist.remove(2.5) # remove first occurrence of 2.5
print(demolist)
demolist.pop() # remove the last element of the list
print(demolist)
demolist.append(1) # add 1 to the end of the list
print(demolist)
print(demolist.count(1))    # count the number of occurrences of 1
print(len(demolist))
demolist.clear()    # remove all elements from the list
print(demolist)
friends = ["Joseph", "Glenn", "Sally", 10,20.3,True]
print(friends)
print(friends.index("Sally")) # find the index of the first occurrence of "Sally"
print(friends.index(10))  # find the index of the first occurrence of 10
print(friends.index(True))  # True is treated as 1